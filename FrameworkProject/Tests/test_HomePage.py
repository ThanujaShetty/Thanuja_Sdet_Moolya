from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage=LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.User_Name, TestData.Password)
        title = homePage.get_home_page_title(TestData.Home_page_title)
        assert title == TestData.Home_page_title

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.User_Name, TestData.Password)
        header = homePage.get_header_value()
        assert header == TestData.Home_page_header


    def test_home_page_account(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.User_Name, TestData.Password)
        account_name = homePage.get_account_Name_value()
        assert account_name == TestData.Account_Name

    def test_setting_icon(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.User_Name, TestData.Password)
        assert homePage.is_setting_icon_exist()
