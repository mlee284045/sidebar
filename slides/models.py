import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Person(AbstractUser):
    Student = 0
    Instructor = 1
    Type = (
        (Student, 'Student'),
        (Instructor, 'Instructor'),
    )
    user_type = models.PositiveSmallIntegerField(choices=Type, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile/pictures', blank=True, null=True)

    def __unicode__(self):
        return unicode("{} {}".format(self.first_name, self.last_name))


# class User(AbstractUser):
#     profile_picture = models.FileField(upload_to='profile/pictures', blank=True, null=True)
#     name = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.name


class Document(models.Model):
    file = models.FileField(upload_to='media/document', blank=True, null=True)

    def __unicode__(self):
        return self.pk

class Resource(models.Model):
    creator = models.ForeignKey(Person, related_name='resources')
    date = models.DateField(default=datetime.date.today())
    text = models.TextField(max_length=200)
    slide = models.URLField(blank=True)

    def __unicode__(self):
        return unicode("Resource created by {} on {}".format(self.creator, self.date))


class StaticPage(models.Model):
    pres_title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    content = models.TextField()

    def __unicode__(self):
        return "{}".format(self.pres_title)

    def get_absolute_url(self):
        return self.url

    # user = models.ForeignKey(User, related_name="resources")
    # documents = models.ForeignKey(Document, related_name="resources", blank=True, null=True)

