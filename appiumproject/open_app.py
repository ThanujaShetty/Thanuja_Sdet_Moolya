from typing import Dict, Any

from appium.options.common import AppiumOptions
from appium.webdriver import webdriver

def opennew():
    cap : Dict[str, Any] = {
        "deviceName": "Thanu",
        "platformName": "Android",
        "appPackage":"com.androidsample.generalstore",
        "appActivity": "com.androidsample.generalstore.SplashActivity"
    }


    webdriver.Remote(r"http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(cap))








