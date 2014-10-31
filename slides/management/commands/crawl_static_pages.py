from django.core.management import BaseCommand
from slides.utils import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        urls = settings.STATIC_PAGES
        crawl_static_pages(urls)