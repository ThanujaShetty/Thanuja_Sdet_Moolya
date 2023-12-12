from selenium import webdriver
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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
name = driver.find_element(By.NAME,"username")
driver.execute_script("arguments[0].value='Admin';",name)
time.sleep(3)

password = driver.find_element(By.CSS_SELECTOR,"input.oxd-input--active")
driver.execute_script("arguments[0].value='admin123';",password)

logn_btn = driver.find_element(By.XPATH,"*//button[@type='submit']")
driver.execute_script("arguments[0].click();",logn_btn)
time.sleep(5)


