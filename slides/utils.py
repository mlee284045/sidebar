import urllib2
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from bs4 import BeautifulSoup
from slides.models import  Slide


def crawl_static_pages():
    count = 0

    for url in settings.STATIC_PAGES:
        soup = get_page_soup(url)

    try:
        main_title = soup.find('h1').get_text(strip=True)
    except AttributeError:
        main_title = 'Untitled'

    section = soup.find('section')

    while section:
        
        slide_title = section.find('h2')
        slide, created = Slide.objects.get_or_create(slide_title=slide_title)
        if created:
            pass
        slide.pres_title = main_title.get_text(strip=True)

        page.text = soup.prettify()
        page.save()
    count += 1

    print 'Crawled %d static pages' % count
    return main_title

def get_page_soup(url):
    if not url.startswith('http://'):
        url = 'http://%s%s' % (Site.objects.get_current().domain, reverse(url))
    print 'Analyzing %s...' % url
    try:
        html = urllib2.urlopen(url)
        return BeautifulSoup(html)
    except urllib2.URLError:
        return "Error while reading '%s'" % url


def next_section(section):
    return section.next_sibling.next_sibling


def get_slide_title(section):
    return section.find('h2').get_text(' ', strip=True)

def check_secondary(section):
    return section.find('section')



def get_slide_text(section):
    stripped = []

    for text in section.h2.find_next_siblings():
        text_list = text.get_text(strip=True).split('\n')
        for item in text_list:
            stripped.append(item.strip())
    return " ".join(stripped)


def get_slide_url(url, count, subcount=""):
    return '{}{}/{}'.format(url, count, subcount)


def create_slide(pres_title, slide_title, url, text):
    slide, created = Slide.objects.get_or_create(
        pres_title=pres_title,
        slide_title=slide_title,
        url=url,
        text=text
    )
    if created:
        pass
    else:
        print '{} already exists in the index, updating...'.format(slide.slide_title)
    return slide

