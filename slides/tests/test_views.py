from django.core.exceptions import ValidationError
from slides.forms import ResourceForm, EmailUserCreationForm
from slides.models import Person


class RegisterTest(TestCase):
    def test_clean_username_exception(self):
        Person.objects.create_user(username='Bob')
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'Bob'}

        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username_pass(self):
        Person.objects.create_user(username='haha')
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'unique'}
        form.clean_username()

class FormTest(TestCase):
    def test_add_resource_form(self):
        form = ResourceForm(data={'creator': 'testcreator', 'text': 'blabla', 'slide':'1', 'title':'testtitle'})
        self.assertTrue(form.is_valid())

        


