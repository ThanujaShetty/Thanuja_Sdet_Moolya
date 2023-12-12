import time

from appium.options.common import AppiumOptions
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By

Capabilities = dict(
        deviceName= "Thanu",
        platformName= "Android",
        appPackage="com.androidsample.generalstore",
        appActivity = "com.androidsample.generalstore.SplashActivity"
)
order_item = "Converse All Star"
appium_server_url= "http://127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(appium_server_url,options=AppiumOptions().load_capabilities(Capabilities))
time.sleep(10)
dd = driver.find_element("id",'android:id/text1').click()
i=1
while i > 0:
        country_list = driver.find_elements('xpath', '//android.widget.TextView')
        for ele in country_list:
                if ele.text == 'Brazil':
                        ele.click()
                        i -=1
                        break
        else:
                driver.swipe(535, 2054, 389, 676, 500)

#clear and send keys
driver.find_element("id",'com.androidsample.generalstore:id/nameField').clear()
txt_box = driver.find_element("id",'com.androidsample.generalstore:id/nameField').send_keys('Thanuja')

#click on radio button
chk_box = driver.find_element('id','com.androidsample.generalstore:id/radioFemale').click()

#click on button
btn_ = driver.find_element('id','com.androidsample.generalstore:id/btnLetsShop').click()
time.sleep(5)

#get product list
i=1
while i > 0:
        country_list = driver.find_elements('xpath', '//android.widget.TextView')
        for ele in country_list:
                if ele.text == order_item:
                        ele.click()
                        time.sleep(3)
                        driver.swipe(825, 2011, 990, 2007, 500)
                        time.sleep(4)
                        i -= 1
                        break
        else:
                driver.swipe(535,2054,389,676,500)



driver.find_element('id',"com.androidsample.generalstore:id/appbar_btn_cart").click()
time.sleep(2)
price = driver.find_element('id',"com.androidsample.generalstore:id/productPrice").text
time.sleep(3)
print(price)
bill_amount = driver.find_element('id',"com.androidsample.generalstore:id/totalAmountLbl").text
print(bill_amount)
time.sleep(3)
driver.find_element(By.CLASS_NAME,"android.widget.CheckBox").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
time.sleep(5)
driver.quit()


