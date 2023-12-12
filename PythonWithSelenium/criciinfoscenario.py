from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
serivce_obj = Service()
driver = webdriver.Chrome(service=serivce_obj)

#navigate to url
driver.get("https://www.espncricinfo.com/")
driver.maximize_window()

#scroll to element
ele = driver.find_element(By.XPATH,'//span[text()="Trending Players"]')
time.sleep(5)

# Action = ActionChains(driver)
# Action.scroll_to_element(ele).perform()
# Action.key_down(Keys.PAGE_DOWN).perform()
#
# driver.find_element(By.XPATH,"//span[text()='Virat Kohli']").click()
# time.sleep(10)


#using Js
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"//span[text()='Virat Kohli']").click()
time.sleep(15)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(5)