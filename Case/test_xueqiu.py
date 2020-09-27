import unittest
from app.app import App
from Page import MainPage,MinePage,LoginPage
import time


class TestXueqiu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = App.xueqiu()
        time.sleep(2)



    def tearDown(self) -> None:
        time.sleep(2)
        App.close_xueqiu()

    def test_swipe_mainpage(self):
        s = MainPage.MainPage(self.driver)
        time.sleep(5)
        s.move_element_up_down_action()

    def test_swipe_minepage(self):
        s = MinePage.MinePage(self.driver)
        s.move_element_up_down_action()

    def test_click_setting_minepage(self):
        s = MinePage.MinePage(self.driver)
        s.move_element_up_down_action()
        s.click_setting()

    def test_login_weibo_loginpage(self):
        s = LoginPage.Login_page_weibo(self.driver)
        s.send_phone_number()
        s.send_password_number()
        s.click_login_button()


if __name__ == '__main__':
    unittest.main()