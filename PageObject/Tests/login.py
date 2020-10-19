import sys

from selenium import webdriver
import time
import unittest
import sys
import os
from PageObject.Pages.loginPage import LoginPAge
from PageObject.Pages.homePage import HomePage


class logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/suler/PycharmProjects/seleniumPythonProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPAge(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Tests Completed!")

