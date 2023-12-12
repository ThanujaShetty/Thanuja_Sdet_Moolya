from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
serivce_obj = Service()
driver = webdriver.Chrome(service=serivce_obj)

#handling alert
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.get("https://demoqa.com/elements")
driver.maximize_window()

Action = ActionChains(driver)
# Action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#
# #action right click
# reight = Action.move_to_element(driver.find_element(By.ID,"mousehover"))
# reight.double_click(driver.find_element(By.ID,"mousehover")).perform()

time.sleep(15)
ele_ = driver.find_element(By.XPATH,'//div[text()="Elements"]')
ele_.click()
