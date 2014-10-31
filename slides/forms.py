from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import Person


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Person
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

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

class EditAccountForm(UserChangeForm):
    username = None
    password = None
    real_name = forms.CharField(label='Real Name', max_length=200)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password Again'}))

    class Meta:
        model = Person
        fields = ("real_name", "email", "password1", "password2")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class UploadPhotoForm(forms.Form):
    photo = forms.ImageField()


class SearchForm(forms.Form):
    search_text = forms.CharField(label='', initial='Search', max_length=200)

class SearchResults(forms.Form):
    search_text = forms.CharField(label='', initial='Search', max_length=200)


class ResourceForm(forms.Form):
    text = forms.CharField()
    file = forms.FileField
#     # slide = forms.URLField(label="slide")




