import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from slides.forms import EmailUserCreationForm, ResourceForm
from slides.models import Resource, Person


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
    return render(request, 'search_page.html')


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
        return render(request, "add_resource.html", {'form': form})


def save_resource(request):
    if request.method == 'POST':
        form = ResourceForm()
        print "Receiving Resource"
        data = json.loads(request.body)
        print data

        resources = Resource.objects.create(
            creator=data['creator'],
            date=data['date'],
            text=data['text'],
            slide=data['slide'],
        )

