import urllib2
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from bs4 import BeautifulSoup
from slides.models import StaticPage


def crawl_static_pages():
    count = 0

    for url in settings.STATIC_PAGES:
        if not url.startswith('http://'):
            url = 'http://%s%s' % (Site.objects.get_current().domain, reverse(url))

        print 'Analyzing %s...' % url

        try:
            page = StaticPage.objects.get(url=url)
            print '%s already exists in the index, updating...' % url
        except StaticPage.DoesNotExist:
            print '%s is new, adding...' % url
            page = StaticPage(url=url)

        try:
            html = urllib2.urlopen(url)
        except urllib2.URLError:
            print "Error while reading '%s'" % url
            continue

        soup = BeautifulSoup(html)
        try:
            page.title = soup.find('h1')
        except AttributeError:
            page.title = 'Untitled'

        page.content = soup.prettify()
        page.save()
        count += 1

    print 'Crawled %d static pages' % count
