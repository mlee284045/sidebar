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
        return unicode("{} {}, {}".format(self.first_name, self.last_name, self.user_type))


class Resource(models.Model):
    creator = models.ForeignKey(Person, related_name='resources')
    date = models.DateField(default=datetime.date.today())
    text = models.TextField(max_length=200)
    slide = models.URLField(blank=True)

    def __unicode__(self):
        return unicode("Resource created by {} on {}".format(self.creator, self.date))
