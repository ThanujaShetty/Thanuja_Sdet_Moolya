from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):


    """BY Locators =Or"""
    Email = (By.ID, "username")
    Password = (By.ID, "password")
    Login_button = (By.ID, "LoginBtn")
    SignUP_Link = (By.LINK_TEXT, "sign up")

    """Constrictor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_URl)

    """page Actions for Login Page"""

    """this is used to get the page title"""
    def get_Login_page_title(self, title):
        return self.get_title(title)

        """this is used to check sign_up link"""
    def is_signUP_link_exist(self):
        return self.is_visible(self.SignUP_Link)

        """this is used to login to app"""
    def do_login(self,username,password):
        self.do_send_key(self.Email,username)
        self.do_send_key(self.Password, password)
        self.do_click(self.Login_button)
        return HomePage(self.driver)     #chaining -
