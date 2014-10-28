import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from slides.forms import EmailUserCreationForm, SearchForm
from haystack.query import SearchQuerySet

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from slides.forms import EmailUserCreationForm, ResourceForm
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
            slides_results = []
            resource_results = []
            for result in search_results:

                if re.search(r"haystack_static_pages.staticpage", result.id):
                    soup = BeautifulSoup(result.content)

                    slide_title = soup.find('h2').get_text().strip()
                    slide_content = soup.find_all(text=re.compile(search_text))
                    slides_results.append({'result': result, 'title': slide_title, 'content': slide_content})

                elif re.search(r"slides.resource", result.id):
                    resource_results.append(result)
                    print result.creator
            print slides_results
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


@csrf_exempt
def add_resource(request):
    if request.method == 'GET':
        print "Sending Form"
        form = ResourceForm()
        return render(request, "add_resource.html", {'form': form})
    else:
        form = ResourceForm()
        return HttpResponse(json.dumps(form), content_type='application.json')


@csrf_exempt
def save_resource(request):
    if request.method == 'POST':
        form = ResourceForm()
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

