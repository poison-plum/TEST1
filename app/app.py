from selenium.webdriver.common.by import By

from common import read_yaml
from appium import webdriver


class App:
    @classmethod
    def xueqiu(cls):
        _path = r'D:\PycharmProjects\appium_qq\app\config_xueqiu'
        config = read_yaml.read_config(_path)
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def close_xueqiu(cls):
        cls.driver.close_app()


# find_element 用法
# driver = App.xueqiu()
# print(type(driver))
# driver.implicitly_wait(10)
# driver.find_element('xpath', "//*[@text='我的']").click()

