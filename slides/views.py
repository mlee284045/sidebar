import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
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



def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(data=request.POST)
        form.save()
    else:
        form = ResourceForm()
    return render(request, "add_resource.html", {'form': form})

