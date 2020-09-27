from Page.MinePage import MinePage
from common.read_yaml import read_locator


class Login_page_qq(MinePage):
    def __init__(self, driver):
        MinePage.__init__(self, driver)
        self.goto_login_page_qq()


class Login_page_weibo(MinePage):

    path = r'D:\PycharmProjects\appium_qq\Page\page_element\Login_page_element.yaml'
    elements = read_locator(path)
    phone_type = elements['phone']['type']
    phone_value = elements['phone']['value']
    password_type = elements['password']['type']
    password_value = elements['password']['value']
    text_phone = elements['phone']['text']
    text_password = elements['password']['text']
    login_button_type = elements['login_button']['type']
    login_button_value = elements['login_button']['value']

    def __init__(self, driver):
        MinePage.__init__(self, driver)
        self.goto_login_page_weibo()

    def send_phone_number(self):
        self.send_text((self.phone_type, self.phone_value), text=self.text_phone)

    def send_password_number(self):
        self.send_text((self.password_type, self.password_value), text=self.text_password)

    def click_login_button(self):
        self.click_element(loc=(self.login_button_type, self.login_button_value))

# true?
# driver = App.xueqiu()
# s = Login_page_weibo(driver)
# s.send_password_number()
# s.send_phone_number()
# s.click_login_button()

# false ?
# driver = App.xueqiu()
# Login_page_weibo(driver).send_phone_number()
# Login_page_weibo(driver).send_password_number()