import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signUP_link_exist()
        assert flag


    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.Login_page_title)
        assert title == TestData.Login_page_title

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.User_Name, TestData.Password)

""" 
To generate  HTML Report

1. Instal Html = pip install pytest-html 
2. give cmd in terminal = pytest test_LoginPage.py -v --html=./hubspot.html
"""

"""
To do parallel Execution

1. Instal xdist = pip install pytest-xdist
2. cmd in terminal to do parallel testing as well as to generate report = pytest test_LoginPage.py -v -n 3 --html=./hubspot.html
"""