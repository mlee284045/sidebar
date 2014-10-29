import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from slides.forms import EmailUserCreationForm, SearchForm, ResourceForm
from haystack.query import SearchQuerySet
from slides.models import Resource, Person
from bs4 import BeautifulSoup
import re


def slides_home(request):
        if request.method == 'POST':
            form = EmailUserCreationForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password1']
                form.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("schedule")
        else:
            form = EmailUserCreationForm()

        return render(request, "home.html", {'form': form})


def index(request):
    return render(request, 'index.html')


def search_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_text']  # strip out value from search form
            search_results = SearchQuerySet().filter(content=search_text)  # process woosh query using search+text
            print search_results
            print search_results[0].id
            slides_results = []     # empty list for slide results
            resource_results = []   # empty list for resource results
            for result in search_results:   # loop over results

                if re.search(r"slides.slide", result.id):  # if its a static page
                    print '='*10, result, '='*10
                    # soup = BeautifulSoup(result.content)
                    # print result.text, result.pres_title, result.slide_title
                    # print result.url
                    # slide_title = soup.find('h2').get_text().strip()  # grab slide title
                    # slide_content = soup.find_all(text=re.compile(search_text))
                    slides_results.append({'result': result, 'title': result.slide_title, 'content': result.content, 'pres_title': result.pres_title})

                elif re.search(r"slides.resource", result.id):  # if its a resource
                    first_name = re.search(r"(\w+) (\w+)", result.creator).group(1)
                    last_name = re.search(r"(\w+) (\w+)", result.creator).group(2)
                    print first_name
                    print "="*10
                    first = result.creator.split()[0]
                    last = result.creator.split()[1]
                    # print result.text
                    # print result.text
                    #print result.creator.first_name
                    #first_name = re.search(r" ", result.creator)  # grab first name
                    print first_name
                    #last_name = re.search(r" ", result.creator)  # grab last name
                    print last_name
                    person = Person.objects.get(first_name=first, last_name=last)  # find all the people
                    print '='*80
                    print person
                    print person.Type
                    print person.profile_picture.url
                    resource_results.append({'date': result.date, 'slide': result.slide, 'file': result.file, 'creator': person, 'content': result.content})  # append resource result to results list
            data = {'slides_results': slides_results, 'resource_results': resource_results}
            return render(request, "search_results.html",  data)

    else:
        form = SearchForm()
    data = {'form': form}

    return render(request, 'search_page.html', data)


def search_results(request):
    return render(request, 'search_results.html')


def profile(request):
    return render(request, 'profile.html')


def sidebar(request):

    collection = []

    everyone = Person.objects.all()

    for i in range(len(everyone)):
        tmp_people_obj = everyone[i]
        for j in tmp_people_obj.resources.all():
            collection.append({
                'creator': str(j.creator),
                'date': str(j.date),
                'slide': j.slide,
                'text': j.text
            })

    return HttpResponse(json.dumps(collection),content_type='application.json')

@csrf_exempt
def add_resource(request):
    if request.method == 'GET':
        print "Sending Form"
        # form = ResourceForm()
        return render(request, "add_resource.html")
    else:
        form = ResourceForm()
        return HttpResponse(json.dumps(form), content_type='application.json')


@csrf_exempt
def save_resource(request):
    if request.method == 'POST':
        # form = ResourceForm()
        print "Receiving Resource"
        print request.body
        data = json.loads(request.body)
        print data

        resources = Resource.objects.create(
            creator=request.user,
            text=data['text'],
            slide=data['slide'],
        )
        return HttpResponse("success")