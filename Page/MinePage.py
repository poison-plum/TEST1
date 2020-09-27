from Page import BasePage
from Page.MainPage import MainPage
from app.app import App
from common.read_yaml import read_locator


class MinePage(MainPage):
    _path = r'D:\PycharmProjects\appium_qq\Page\page_element\Mine_page_element.yaml'
    elements = read_locator(_path)
    # qq
    qq_type = elements['locator']['QQ']['type']
    qq_value = elements['locator']['QQ']['value']
    # weibo
    weibo_type = elements['locator']['WEIBO']['type']
    weibo_value = elements['locator']['WEIBO']['value']
    # seting
    seting_type = elements['locator']['setting']['type']
    seting_value = elements['locator']['setting']['value']

    def __init__(self, driver):
        MainPage.__init__(self, driver)
        self.goto_mine_page()

    def goto_login_page_qq(self):
        self.click_element((self.qq_type, self.qq_value))

    def goto_login_page_weibo(self):
        self.click_element((self.weibo_type, self.weibo_value))

    def click_setting(self):
        self.click_element(loc=(self.seting_type, self.seting_value))




