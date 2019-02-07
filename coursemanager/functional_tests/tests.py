# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost:8000/admin/login"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_valid_login(self):
        """
        Logging into the application with a valid username and password should
        present the default admin dashboard with the Coursemanager application displayed.

        :return:
        """
        driver = self.driver
        driver.get("http://localhost:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()

        self.assertTrue(self.is_element_present(By.LINK_TEXT, "COURSEMANAGER"))
        driver.find_element(By.LINK_TEXT, "LOG OUT").click()

    def test_invalid_login(self):
        """
        Logging into the application with an INVALID username and password should
        display an error message.

        :return:
        """
        driver = self.driver
        driver.get("http://localhost:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("wrongpassword")

        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()

        errordiv = driver.find_element_by_class_name("errornote")

        driver.save_screenshot('invalid_login.png')

        self.assertTrue("enter the correct username and password" in errordiv.text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
