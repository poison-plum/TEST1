from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        return WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(EC.presence_of_element_located(loc))

    # 点击：
    def click_element(self, loc):
        self.find_element(loc).click()

    # tap
    def tap_action(self, bounce):
        self.driver.tap(bounce, duration=1000)

    # touch_action tap
    def tap_touch_action(self, loc):
        TouchAction(self.driver).tap(element=self.find_element(loc)).perform()

    # 元素位置点击，相对定位
    def tap_position_touch_action(self, position, last_position):
        x = position[0] / last_position[0]
        y = position[1] / last_position[1]
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        TouchAction(self.driver).tap(x=width * x, y=height * y).perform()

    # 长按
    def long_press_action(self, loc):
        TouchAction(self.driver).press(e1=self.find_element(loc)).wait(5000).release().perform()

    # 移动:(x1,y1) (x2,y2)
    def move_element_action(self, position1, position2, last_position):
        x1 = position1[0] / last_position[0]
        y1 = position1[1] / last_position[1]

        x2 = position2[0] / last_position[0]
        y2 = position2[1] / last_position[1]

        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['heigth']

        TouchAction(self.driver).press(x=width * x1, y=height * y1).move_to(x=width * x2, y=height * y2).wait(
            4000).release().perform()

    # 上下移动
    def move_element_up_down_action(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        time.sleep(2)
        TouchAction(self.driver).long_press(x=int(width/2), y=int(height*4/5)).move_to(x=int(width/2), y=int(height/7)).release().perform()
        time.sleep(2)

    # 输入值：
    def send_text(self, loc, text):
        e = self.find_element(loc)
        # 清楚
        e.clear()
        e.send_keys(text)

    # 获取text值
    def get_text(self, loc):
        e = self.find_element(loc)
        return e.text

    # 获取属性值
    def get_attribute(self, loc, attr):
        e = self.find_element(loc)
        return e.get_attribute(attr)

    # 一组元素获取
    def find_elements(self, loc):
        return WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
            EC.presence_of_all_elements_located(loc))

    # click
    def click_elements(self, loc, number):
        list_ex = self.find_elements(loc)
        list_ex[number].click()
