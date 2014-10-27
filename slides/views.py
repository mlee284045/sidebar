from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
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


# def add_resource(request):
#     data = {"resource_form": ResourceForm()}
#     if request.method == 'POST':
#         form = ResourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("resources")
#
#         else:
#             data = {"comment_form": ResourceForm(request.POST)}
#             return render(request, "add_ressource.html", data)
#
#     else:
#         return render(request, "add_ressource.html", data)
#
# def resource_view(request):
#     if request.method == 'POST':
#         form = ResourceForm(request.POST)
#         if form.is_valid():
#             date = request.POST['date']
#             print date
#             resources = Resource.objects.filter(date=date)
#             students = []
#             for resource in resources:
#                 user = resource.user.username
#                 if user not in students:
#                     students.append(user)
#             return render(request, "teacher_home.html", {'students': students, "date": date})
#     else:
#         form = ResourceForm()
#
#     return render(request, "resource_view.html", {'form': form})