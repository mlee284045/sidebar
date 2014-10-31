
from django.test import TestCase
from slides.models import Slide, Person, Resource
from slides.utils import crawl_static_pages


class ModelTestCase(TestCase):

    def test_slide_creation(self):
        count = Slide.objects.all().count()
        url = 'http://127.0.0.1:8000/week1/4_pm/'
        crawl_static_pages([url])
        new_count = Slide.objects.all().count()
        one_slide = Slide.objects.all().first()

        self.assertGreater(new_count, count)
        self.assertIsInstance(one_slide, Slide)