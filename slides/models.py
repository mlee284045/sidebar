from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


student = "0"
instructor = "1"

role_choices = (
    (student, 'student'),
    (instructor, 'instructor'),
)


class Person(AbstractUser):
    photo = models.ImageField(upload_to='profile/pictures', blank=True, null=True)
    role = models.CharField(choices=role_choices, null=True, blank=True, max_length=1)

    def __unicode__(self):
        return unicode(self.username)