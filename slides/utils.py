import urllib2
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from bs4 import BeautifulSoup
from slides.models import Slide


def crawl_static_pages(urls):
    """ Function crawls static pages of each url that is given as a list parameter
        In order to use it in the shell, import django.conf.settings and call the
        function with the parameter settings.STATIC_PAGES"""

    count = 0

    for url in urls:
        slide_count = 0
        soup = get_page_soup(url)
        try:
            main_title = soup.find('h1').get_text(strip=True)
        except AttributeError:
            main_title = 'Untitled'

        section = soup.find('section')

        while next_section(section):
            if next_section(section) != 'spacing':
                slide_count += 1
            else:
                print 'skipped section'
                section = next_section(section)
                continue
            if check_secondary(next_section(section)):
                sub_slide = 0
                try:
                    sub_section = section.find('section')
                except AttributeError:
                    print 'continued'
                    continue
                while sub_section:
                    if sub_section != 'spacing':
                        sub_slide += 1
                    else:
                        print 'skipped next subsection'
                        sub_section = next_section(sub_section)
                        continue
                    print '='*10, sub_slide, '='*10, slide_count
                    slide_url = get_slide_url(url, slide_count, sub_slide)
                    title = get_slide_title(sub_section)
                    text = get_slide_text(sub_section)
                    content = sub_section
                    create_slide(main_title, title, slide_url, text, content)
                    count += 1
                    sub_section = next_section(sub_section)


                section = next_section(section)
            else:
                slide_url = get_slide_url(url, slide_count)
                title = get_slide_title(next_section(section))
                text = get_slide_text(next_section(section))
                content = next_section(section)
                create_slide(main_title, title, slide_url, text, content)
                count += 1
                section = next_section(section)

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
    try:
        next_section = section.next_sibling
    except AttributeError:
        print 'No more sections'
        return False
    try:
        print 'had a sibling, looking for h2'
        next_section.find('h2')
    except AttributeError:
        print 'Just spacing'
        return 'spacing'
    # try:
    #     return next_section = next_section.next_sibling
    # except AttributeError:
    #     return False
    return next_section


def get_slide_title(section):
    try:
        title = section.find('h2').get_text(' ', strip=True)
    except AttributeError:
        print 'No such title'
        title = ""
    return title


def check_secondary(section):
    if section:
        return section
    else:
        try:
            section.find('section')
        except AttributeError:
            print 'no such subsection'
            return False
    return True


def get_slide_text(section):
    stripped = []
    try:
        for text in section.h2.find_next_siblings():
            text_list = text.get_text(strip=True).split('\n')
            for item in text_list:
                stripped.append(item.strip())
    except AttributeError:
        print 'No further sections'
    return " ".join(stripped)


def get_slide_url(url, count, subcount=""):
    return '{}#/{}/{}'.format(url, count, subcount)


def create_slide(pres_title, slide_title, url, text, content):
    slide, created = Slide.objects.update_or_create(
        pres_title=pres_title,
        slide_title=slide_title,
        url=url,
        text=text,
        content=content
    )
    if created:
        print '{} was created in the index'.format(slide.slide_title)
        pass
    else:
        print '{} already exists in the index, updating...'.format(slide.slide_title)
    return slide

