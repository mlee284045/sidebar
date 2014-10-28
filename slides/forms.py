from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from models import Person, Resource


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Person
        fields = ("first_name", "last_name", "username", "email", "user_type", "profile_picture", "password1", "password2")

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
    search_text = forms.CharField(label='Search', max_length=200)


class ResourceForm(forms.Form):
    text = forms.CharField()
#     # slide = forms.URLField(label="slide")


