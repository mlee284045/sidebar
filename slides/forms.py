
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

class ResourceForm(forms.Form):
    text = forms.CharField(label="text area content")


    def save(self):
        text = self.cleaned_data["text"]
        try:
            Resource.objects.get(text=text)
        except Resource.DoesNotExist:
            return text
        raise forms.ValidationError(
            self.error_messages['duplicate_text'],
            code='duplicate_text',
        )











