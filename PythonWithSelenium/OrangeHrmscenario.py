from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
serivce_obj = Service()
driver = webdriver.Chrome(service=serivce_obj)


#launching browser
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

#DO Login
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,'password').send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,'.oxd-button').click()
time.sleep(5)

#click on PIM
driver.find_element(By.XPATH,"//a[contains(@href,'pim')]").click()
time.sleep(5)

#enter input
driver.find_element(By.XPATH,'//div//input[@placeholder="Type for hints..."][1]').send_keys('a')

#select value from drop down
driver.find_element(By.XPATH,'//span[text()="Burak Maria İkinci"]').click()
time.sleep(5)

# Select job title
