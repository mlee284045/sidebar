from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import haystack_static_pages
from haystack_static_pages.models import StaticPage
import re
from slides.forms import EmailUserCreationForm, SearchForm
from haystack.query import SearchQuerySet
from slides.models import Resource
from bs4 import BeautifulSoup


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
                    slides_results.append([result, slide_title])

                elif re.search(r"slides.resource", result.id):
                    resource_results.append(result)
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