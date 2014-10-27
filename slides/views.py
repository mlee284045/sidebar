from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from slides.forms import EmailUserCreationForm, SearchForm
from haystack.query import SearchQuerySet


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
            search_text = form.cleaned_data['search_text']
            search_results = SearchQuerySet().filter(content=search_text)

            print search_results[0].creator
            print search_results[0].date
            print search_results[0].text2
            print search_results[0].slide

            return render(request, "search_results.html",  {'search_results': search_results})

    else:
        form = SearchForm()
    data = {'form': form}

    return render(request, 'search_page.html', data)



def search_results(request):
    return render(request, 'search_results.html')


def profile(request):
    return render(request, 'profile.html')