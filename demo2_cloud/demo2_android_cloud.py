import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": "bs://06bfe1f20d3bfaa46575fd2c9d5520780c440d18",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "maulindesai_TAIrXi",
                "accessKey": "HeMRrqWSFKatQtUxP2pX"
            }
        }
        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceCloud(AppiumConfig):

    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        print(self.driver.page_source)