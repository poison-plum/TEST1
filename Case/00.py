from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

from app.app import App
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = App.xueqiu()
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
time.sleep(5)
el1 = WebDriverWait(driver, timeout=10, poll_frequency=0.5).until(EC.presence_of_element_located(locator=('xpath', '//*[@text="我的"][@resource-id="com.xueqiu.android:id/tab_name"]')))
TouchAction(driver).tap(el1).perform()
time.sleep(2)
TouchAction(driver).press(x=int(width/2), y=int(height*4/5)).wait(3000).move_to(x=int(width/2), y=int(height/7)).release().perform()


print("this is test two")