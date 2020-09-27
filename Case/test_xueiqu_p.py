from Page.LoginPage import Login_page_weibo
from app.app import App
from common.read_yaml import read_locator


driver = App.xueqiu()
s = Login_page_weibo(driver)
s.send_phone_number()
s.send_password_number()
driver.close_app()

# 执行不成功
# drivr = App.xueqiu()
# Login_page_weibo(drivr).send_phone_number()
# Login_page_weibo(drivr).send_password_number()



# 查看参数是否正确
# path = r'D:\PycharmProjects\appium_qq\Page\page_element\Login_page_element.yaml'
# elements = read_locator(path)
# phone_type = elements['phone']['type']
# phone_value = elements['phone']['value']
# password_type = elements['password']['type']
# password_value = elements['password']['value']
# text_phone = elements['phone']['text']
# text_password = elements['password']['text']
#
# print(password_type)
# print(password_value)
# print(text_password)