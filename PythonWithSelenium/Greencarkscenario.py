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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)

#search for items
driver.find_element(By.XPATH,'//form[@class="search-form"]/input[@class="search-keyword"]').send_keys("be")
btn_search = driver.find_element(By.CSS_SELECTOR,'button[class="search-button"]')
time.sleep(5)
btn_search.click()


#adding prod to cart
btn_add_to_cart = driver.find_elements(By.XPATH,'//div[@class="product-action"]/button[text()="ADD TO CART"]')
for btn in btn_add_to_cart:
    btn.click()
    time.sleep(5)

#click on cart
cart = driver.find_element(By.XPATH,'//a[@class="cart-icon"]/img').click()

#check for btn is clickable
chkout_btn = driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()
time.sleep(5)

#wait till url changes
# wait = WebDriverWait(driver,)
# wait.until(expected_conditions.url_contains("cart"))

#selecting total  from table
price_in_tbl = driver.find_elements(By.XPATH,'//table[@id="productCartTables"]/tbody/tr/td[5]')
sums = []
for price in price_in_tbl:
    sums.append(int(price.text))
    total_sum = (sum(sums))

#asserting value
value = driver.find_element(By.CSS_SELECTOR,'span[class="totAmt"]').text
exp_val = int(value)
print("Total Sum : ",total_sum)
print("Actual sum : ",exp_val)

#asserting tol value with sum
assert total_sum == exp_val

#click on place order btn
driver.find_element(By.XPATH,'//button[text()="Place Order"]').click()
exp_url = "https://rahulshettyacademy.com/seleniumPractise/#/country"
act_url = driver.current_url

#assert url
assert act_url == exp_url
time.sleep(5)

#select country from drop-down
dd_ele = driver.find_element(By.CSS_SELECTOR,'select[style="width: 200px;"]')
drop_down = Select(dd_ele)
drop_down.select_by_visible_text("India")

#click on checkbox
chk_box = driver.find_element(By.CSS_SELECTOR,'input[type="checkbox"]').click()

#click on procced btn
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
url = driver.current_url

#get text from page
webpg_txt = driver.find_element(By.XPATH,"//span[contains(text(),'Thank you,')]")
print(webpg_txt.text)

