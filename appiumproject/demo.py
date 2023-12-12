from appium.options.common import AppiumOptions
from appium.webdriver import webdriver

Capabilities = dict(
        deviceName= "Thanu",
        platformName= "Android",
        appPackage="com.androidsample.generalstore",
        appActivity = "com.androidsample.generalstore.SplashActivity"
)
appium_server_url= "http://localhost:4723/wd/hub"
driver = webdriver.Remote(appium_server_url,options=AppiumOptions().load_capabilities(Capabilities))
