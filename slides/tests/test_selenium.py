from time import sleep
from django.core.urlresolvers import reverse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import LiveServerTestCase, TestCase
from slides.models import SearchForm, EmailUserCreationForm, UploadPhotoForm
from slides.models import Person,Resource, Slide


class SeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_user_flow(self):
        username = 'test-user'
        password = 'test-pw'
        Person.objects.create(username=username, password=password)

        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('login')))

        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_id('id_username').send_keys(username)
        password_input = self.selenium.find_element_by_id('id_password')
        password_input.send_keys(password)

        # Submit the form
        password_input.send_keys(Keys.RETURN)
        sleep(1)

    def admin_login(self):
        # Create a superuser
        Person.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')

        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))

        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('superuser')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('mypassword')

        # Submit the form
        password_input.send_keys(Keys.RETURN)


    def test_login_and_search(self):
        username = 'user3'
        password = 'pass3'
        self.student = Person.objects.create_user(username=username, email='user3@test.com', password=password)
        self.selenium.get("{}{}".format(self.live_server_url, reverse('login')))
        self.selenium.find_elements_by_link_text('Login')[0].click()
        sleep(0.8)
        self.selenium.find_element_by_name('username').send_keys(username)
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys(password)
        sleep(0.8)
        password_input.send_keys(Keys.RETURN)
        sleep(0.8)
        self.selenium.find_elements_by_id("SearchImg")[0].click()
        sleep(.8)
        self.selenium.get("{}{}".format(self.live_server_url, reverse('search_page')))
        sleep(4)
        search = self.selenium.find_elements_by_id("id_search_text")[0].click()
        sleep(.8)
        search.send_keys('django')
        sleep(.8)
        search.send_keys(Keys.RETURN)
        body=self.selenium.find_element_by_tag_name('from_slides')
        self.assertIn('Django Models', body.text)
        sleep(4)