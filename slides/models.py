import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    TEACHER = 0
    STUDENT = 1
    TYPE = (
        (TEACHER, "Teacher"),
        (STUDENT, "Student")
    )
    user_type = models.PositiveSmallIntegerField(choices=TYPE, default=0)
    profile_picture = models.ImageField(upload_to='profile/pictures', blank=True, null=True)


    def __unicode__(self):
        return unicode(self.username)


class Resource(models.Model):
    creator = models.ForeignKey(Person, related_name='resources')
    date = models.DateField(default=datetime.date.today())
    text = models.TextField(max_length=200)
    slide = models.URLField(blank=True)
