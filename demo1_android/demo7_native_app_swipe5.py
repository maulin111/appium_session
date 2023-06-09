import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Swipe using appium default method with 50%"""

class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            # "automationName":"UiAutomator2"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestArts(AppiumConfig):

    def swipe_and_click_element(self,xpath):
        size_dic = self.driver.get_window_size()
        print(size_dic)
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.XPATH, xpath)) == 0:
            self.driver.swipe(x1, y1, x2, y2, 1000)

        self.driver.find_element(AppiumBy.XPATH, xpath).click()
        self.driver.implicitly_wait(30)

    def test_the_himalayas_topics(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        size_dic=self.driver.get_window_size()
        print(size_dic)
        x1=size_dic['width']*(50/100)
        y1=size_dic['height']*(75/100)

        x2=size_dic['width']*(50/100)
        y2=size_dic['height']*(25/100)
        print(x1)
        print(y1)
        print(x2)
        print(y2)

        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Art of Asia']")) == 0:
            self.driver.swipe(x1, y1, x2, y2, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Art of Asia']").click()
        self.driver.implicitly_wait(30)

        self.swipe_to_element("//*[contains(@text,'Himal')]")