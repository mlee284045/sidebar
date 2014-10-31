import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from slides.forms import EmailUserCreationForm, SearchForm, ResourceForm, SearchResults, EditAccountForm
from haystack.query import SearchQuerySet
from slides.models import Resource, Person, Slide
from bs4 import BeautifulSoup
import re


def slides_home(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            user = form.save()
            user.profile_picture = '/static/img/default-profile-photo.png'
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
        return redirect("index")
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
            slides_results = []     # empty list for slide results
            resource_results = []   # empty list for resource results
            for result in search_results:   # loop over results

                if re.search(r"slides.slide", result.id):  # if its a static page
                    slides_results.append({
                        'result': result,
                        'title': result.slide_title,
                        'content': result.content,
                        'pres_title': result.pres_title
                    })

                elif re.search(r"slides.resource", result.id):  # if its a resource
                    first = result.creator.split()[0]
                    last = result.creator.split()[1]

                    person = Person.objects.get(first_name=first, last_name=last)  # find all the people

                    resource_results.append({
                        'date': result.date,
                        'slide': result.slide,
                        'title': result.title,
                        'file': result.file,
                        'creator': person,
                        'content': result.content
                    })  # append resource result to results list
                    form = SearchForm()
            data = {'slides_results': slides_results, 'resource_results': resource_results,'form':form,
                    'search_text':search_text}
            return render(request, "search_results.html",  data)
    else:
        form = SearchForm()
    data = {'form': form}

    return render(request, 'search_results.html', data)


def search_results(request):
    # if request.method == 'POST':
    #     form = SearchResults(request.POST)
    #     if form.is_valid():
    #         search_text = form.cleaned_data['search_text']  # strip out value from search form
    #         search_results = SearchQuerySet().filter(content=search_text)  # process whoosh query using search+text
    #         slides_results = []     # empty list for slide results
    #         resource_results = []   # empty list for resource results
    #         for result in search_results:   # loop over results
    #             if re.search(r"slides.slide", result.id):  # if its a static page
    #                 soup = BeautifulSoup(result.content)
    #                 slide_title = soup.find('h2').get_text().strip()  # grab slide title
    #                 slide_content = soup.find_all(text=re.compile(search_text))
    #                 slides_results.append({'result': result, 'title': slide_title, 'content': slide_content})
    #
    #             elif re.search(r"slides.resource", result.id):  # if its a resource
    #                 #print result.creator.first_name
    #                 #first_name = re.search(r" ", result.creator)  # grab first name
    #                 #print first_name
    #                 #last_name = re.search(r" ", result.creator)  # grab last name
    #                 #print last_name
    #                 #person = Person.objects.filter(first_name__Miguel) # find all the people
    #                 resource_results.append({'result': result})  # append resource result to results list
    #
    #         data = {'slides_results': slides_results, 'resource_results': resource_results,'form': form }
    #         return render(request, "search_results.html",  data)
    #
    # else:
    form = SearchForm()
    data = {'form': form}
    return render(request, 'search_results.html', data)


def edit_account(request):
    user = Person.objects.get(pk=request.user.id)
    form = EditAccountForm(instance=user)
    data = {'form': form, 'image': request.user.profile_picture}

    return render(request, 'edit_account.html', data)

@csrf_exempt
def update_account(request):
    user = Person.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved new password')
        else:
            name = request.POST['real_name']
            user.real_name = name
            user.save()
        return HttpResponse('Saved real name')
    else:
        return HttpResponse('No new information')

@csrf_exempt
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
                'text': j.text,
                'title': j.title,
            })

    return HttpResponse(json.dumps(collection),content_type='application.json')

@csrf_exempt
def get_resource_info(request):

    collection = []
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        # slide_resource = Resource.objects.filter(slide=data)
        slide_resource = Resource.objects.filter(slide=data)
        print slide_resource
        for resource in slide_resource:
            collection.append({
                'creator': resource.creator,
                'date': resource.date,
                'slide': resource.slide,
                'text': resource.text,
                'title': resource.title,
            })

    return HttpResponse(json.dumps(collection), content_type='application.json')

@csrf_exempt
def get_slide_info(request):

    collection = []

    if request.method == 'POST':
        data = json.loads(request.body)
        all_slides = Slide.objects.filter(pres_title=data)

        for slide in all_slides:

            slide_resources = Resource.objects.filter(slide=slide.url)

            temp_slide = {'pres_title': slide.pres_title, 'slide_title': slide.slide_title,'url': slide.url,'text': slide.text, 'resource':[]}


            for slide_resource in slide_resources:
                temp_slide.resource.append({
                    'resource_creator': slide_resource.creator,
                    'resource_date': slide_resource.date,
                    'resource_text': slide_resource.text,
                    'resource_title': slide_resource.title,
                    })
            collection.append(temp_slide)

    return HttpResponse(json.dumps(collection), content_type='application.json')

@csrf_exempt
def add_resource(request):

    if request.method == 'GET':
        return render(request, "add_resource.html")
    else:
        form = ResourceForm()
        return HttpResponse(json.dumps(form), content_type='application.json')


@csrf_exempt
def save_resource(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        resources = Resource.objects.create(
            creator=request.user,
            text=data['text'],
            slide=data['slide'],
            title=data['title'],
        )
        print resources
        return HttpResponse("success")