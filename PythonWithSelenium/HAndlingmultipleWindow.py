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

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.ID,"openwindow").click()
# handles  = driver.window_handles
# parent_handle = driver.current_window_handle
# print(parent_handle.title())
# size = len(handles)
# print(size)
# driver.switch_to.window(parent_handle)
# driver.close()
# for i in range(size):
#     if handles[i] != parent_handle:
#         driver.switch_to.window(handles[i])
#         title = driver.title
#         print(title)
#         driver.close()
#         break
#

#example for iframe

driver.get("https://demoqa.com/frames")
driver.maximize_window()
driver.switch_to.frame("frame2")
text = driver.find_element(By.ID,"sampleHeading").text
print(text)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.switch_to.default_content()
print(driver.title)
