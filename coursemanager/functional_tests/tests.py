from selenium import webdriver
import unittest


class PlainDjangoRunning(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_dj_landing_page(self):
        """Test the django loading page loads ok"""

        self.browser.get('http://localhost:8000')
        self.assertTrue('Django' in self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()