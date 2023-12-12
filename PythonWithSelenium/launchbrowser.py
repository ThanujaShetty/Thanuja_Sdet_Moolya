from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serivce_obj = Service()
driver = webdriver.Chrome(service=serivce_obj)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,'input').click()
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-tab").click()
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-link").click()
time.sleep(5)
