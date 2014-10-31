from bs4 import BeautifulSoup
from django.test import TestCase
from slides.models import Slide
from slides.utils import crawl_static_pages, get_page_soup, next_section, create_slide, get_slide_title, \
    get_slide_url, get_slide_text, check_secondary


class UtilTestCase(TestCase):
    def setUp(self):
        self.html_doc = """
        <div>
            <section>
                <h1>Big Testing Title</h1>
                <section>
                    <h2>testing nested section<h2>
                </section>
            </section>
            <section>
                <h2>Small Testing Title</h2>
                <p>
                    Testing text content Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Fusce id lacus vulputate tellus tincidunt egestas. Nulla eget tempus ligula.
                </p>
                <p>
                    Ut quis mattis quam, eu mollis mauris. Nunc at commodo orci. Duis eget bibendum elit.
                    Aenean tincidunt eros sit amet quam fermentum, non consequat odio tristique.
                </p>
            </section>
        </div>
        """
        self.url = 'http://127.0.0.1:8000/week1/4_pm/'
        self.soup = BeautifulSoup(self.html_doc)
        self.section = self.soup.find('section')
        self.next = next_section(self.section)


    def tearDown(self):
        pass


    def test_crawler(self):
        # This test will need to move to a live server test case
        bad_url = 'http://127.0.0.1:8000/wiggle/wiggle/test'
        bad_soup = get_page_soup(bad_url)
        good_soup = get_page_soup(self.url)

        self.assertIsInstance(good_soup, BeautifulSoup)
        self.assertEqual(bad_soup, "Error while reading '{}'".format(bad_url))


    def test_next_section(self):
        self.assertIn(self.next.find('h2'), self.next)
        self.assertEqual(self.next, self.soup.find_all('section')[2])


    def test_create_slide(self):
        total = Slide.objects.all().count()

        pres_title = 'Big Testing Title'
        slide_title = 'Small Testing Title'
        url = 'http://127.0.0.1:8000/week1/4_pm/'
        text = 'Testing text content Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

        slide = create_slide(pres_title, slide_title, url, text)
        get_slide = Slide.objects.get(url=url)
        new_count = Slide.objects.all().count()

        self.assertGreater(new_count, total)
        self.assertIsInstance(slide, Slide)
        self.assertEqual(slide, get_slide)


    def test_check_secondary(self):
        self.assertTrue(check_secondary(self.section))
        self.assertFalse(check_secondary(self.next))


    def test_get_slide_title(self):
        title = get_slide_title(self.next)
        self.assertIsInstance(title, unicode)
        self.assertEqual(title, 'Small Testing Title')


    def test_get_slide_url(self):
        primary_slide = get_slide_url(self.url, 3)
        secondary_slide = get_slide_url(self.url, 3, 1)
        self.assertEqual(primary_slide, "{}#/{}/".format(self.url, 3))
        self.assertEqual(secondary_slide, "{}#/{}/{}".format(self.url, 3, 1))

    def test_get_slide_text(self):
        text = get_slide_text(self.next)
        self.assertIn('Aenean tincidunt eros', text)

    def test_crawl_static_pages(self):
        # Needs further testing but this seems like it is working
        # empty_result = crawl_static_pages([])
        good_result = crawl_static_pages([self.url])
        # self.assertEqual(empty_result, "")
        self.assertEqual(good_result, 'Object-Oriented Python II: Methods')