from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):

    Header = (By.CSS_SELECTOR, "h1.dashboard-selector_title")
    Account_Name = (By.CSS_SELECTOR, "account_name")
    Setting_icon = (By.ID,"navSetting")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_visible(self.Setting_icon)

    def get_header_value(self):
        if self.is_visible(self.Header):
            return self.get_element_text(self.Header)


    def get_account_Name_value(self):
        if self.is_visible(self.Account_Name):
            return self.get_element_text(self.Account_Name)