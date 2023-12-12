import pytest
from selenium import webdriver

from Config.config import TestData

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.Chrome_ExecutablePath)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FireFox_ExecutablePath)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
