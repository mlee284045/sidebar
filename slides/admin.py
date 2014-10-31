from django.contrib import admin
from slides.models import Person, Resource, Slide

# Register your models here.
from slides.search_indexes import SlideIndex

admin.site.register(Person)
admin.site.register(Resource)
admin.site.register(Slide)