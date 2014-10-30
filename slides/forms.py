from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Person


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Person
        fields = ("first_name", "last_name", "username", "email", "profile_picture", "password1", "password2")

    def clean_username(self):

        username = self.cleaned_data["username"]
        try:
            Person.objects.get(username=username)
        except Person.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )



class SearchForm(forms.Form):
    search_text = forms.CharField(label='', initial='Search', max_length=2000)

class SearchResults(forms.Form):
    search_text = forms.CharField(label='', initial='Search', max_length=2000)

class PasswordForm(forms.Form):
    search_text = forms.CharField(label='', initial='************', max_length=200)


class ResourceForm(forms.Form):
    text = forms.CharField()
    file = forms.FileField
#     # slide = forms.URLField(label="slide")




