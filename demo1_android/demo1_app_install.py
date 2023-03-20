from appium import webdriver

desc_cap = {
    "platformName": "android",
    "platformVersion": "oneplus",
    "app": r"C:\Backup Folders\Proposal\Python skills\khan-academy-7-3-2.apk"
}

webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desc_cap)