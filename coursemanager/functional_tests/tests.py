from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class LoginTests(StaticLiveServerTestCase):
    fixtures = ['users.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        """ It is possible to login using the set username and password """
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.implicitly_wait(1000)

        self.selenium.save_screenshot('LoginTests.png')

        # Post login asserts
        self.assertTrue(self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/h1').text, 'Site administration')


class CourseLoadTests(StaticLiveServerTestCase):
    """ The courses have been correctly loaded from the fixtures"""
    fixtures = ['users.json', 'courses.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_course_load_count(self):
        """The total number of courses loaded using the test dataset should be 11"""
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.implicitly_wait(1000)

        # Courses
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[3]/th/a').click()
        self.selenium.save_screenshot('CourseLoadTests_test_login.png')

        total_courses = self.selenium.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/p').text
        self.assertTrue(total_courses == '11 courses')

class AddPresentation(StaticLiveServerTestCase):

    # fixtures = ['users.json', 'courses.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_course_load_count(self):
        """The total number of courses loaded using the test dataset should be 11"""
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.implicitly_wait(1000)

        # Courses
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[3]/th/a').click()
        self.selenium.save_screenshot('CourseLoadTests_test_login.png')

        total_courses = self.selenium.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/form/p').text
        self.assertTrue(total_courses == '11 courses')
