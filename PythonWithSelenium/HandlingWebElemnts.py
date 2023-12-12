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



driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#select option from dropdown
drop_down_ele = driver.find_element(By.ID,"dropdown-class-example")
drop_down = Select(drop_down_ele)
# drop_down.select_by_index("1")
drop_down.select_by_visible_text("Option1")
# drop_down.select_by_value("option2")

# dynamic_dd = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Type to Select Countries"]')
# dynamic_dd.send_keys("India")
# time.sleep(5)
# countries = driver.find_elements(By.CLASS_NAME,"li[class='ui-menu-item']")
#
# for country in countries:
#     if country == "India":
#         country.click()

# ele_dis = driver.find_element(By.ID,"autocomplete").is_displayed()
# print(ele_dis)
# value= driver.find_element(By.ID,"autocomplete").get_attribute("value")
# print(value)
# assert value == "India"

 #select value fro checkbox
cb = driver.find_element(By.CSS_SELECTOR,'input[value="option2"]')
cb.click()
value = cb.is_selected()
print(value)

#to check how many checkbox are there
len_cb = driver.find_elements(By.CSS_SELECTOR,'input[type="checkbox"]')
value = len(len_cb)
print(value)

#select one elemnt from cb and asseert it
for ele in len_cb:
    if ele.get_attribute("Value") =="Option2":
        ele.click()
        assert ele.is_selected()



