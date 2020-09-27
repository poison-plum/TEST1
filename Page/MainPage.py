from app.app import App
from common.read_yaml import read_locator
from Page.base import BasePage


class MainPage(BasePage):
    path = r'D:\PycharmProjects\appium_qq\Page\page_element\Main_page_element.yaml'
    elements = read_locator(path)
    mine_value = elements['xueqiu']['locators'][0]['value']
    mine_type = elements['xueqiu']['locators'][0]['type']

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_mine_page(self):
        self.click_element((self.mine_type, self.mine_value))






