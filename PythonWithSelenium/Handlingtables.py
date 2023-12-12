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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.ID,"product")
city = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table//tr[2]/td[3]").text
print(city)
Name = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table//tr[2]/td[1]/../td[1]").text
print(Name)

# entire_table = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table").text
# print(entire_table)

#using js printing
entire_table = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table")
print(driver.execute_script("return arguments[0].innerText;",entire_table))
