from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
def switch_window(window_to_switch):
    d_c = {'appTopLevelWindow': window_to_switch, 'platformName': "Windows", 'deviceName': "WindowsPC"}
    return webdriver.Remote("http://127.0.0.1:4723", d_c)
def click_by_name(t_driver, button):
    t_driver.create_web_element(t_driver.find_element(by=AppiumBy.NAME, value=button).get('ELEMENT')).click()
def multi_click_by_name(t_driver, button,i):
    for j in range(i):
        t_driver.create_web_element(t_driver.find_element(by=AppiumBy.NAME, value=button).get('ELEMENT')).click()
def click_by_name_multi(t_driver, button, index):
    t_driver.create_web_element(t_driver.find_elements(by=AppiumBy.NAME, value=button)[index].get('ELEMENT')).click()
def click_by_id(t_driver, button):
    t_driver.create_web_element(t_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=button).get('ELEMENT')).click()
def click_by_id_multi(t_driver, button, index):
    t_driver.create_web_element(t_driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value=button)[index].get('ELEMENT')).click()
def create_web_element_by_name(t_driver, button):
    return t_driver.create_web_element(t_driver.find_element(by=AppiumBy.NAME, value=button).get('ELEMENT'))
def create_web_element_by_name_multi(t_driver, button, index):
    return t_driver.create_web_element(t_driver.find_elements(by=AppiumBy.NAME, value=button)[index].get('ELEMENT'))
def create_web_element_by_id(t_driver,text_box):
    return t_driver.create_web_element(t_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=text_box).get('ELEMENT'))
def is_selected_by_name(t_driver, button):
    return t_driver.create_web_element(t_driver.find_element(by=AppiumBy.NAME, value=button).get('ELEMENT')).is_selected()
def select_by_name(t_driver, button):
    if not t_driver.create_web_element(t_driver.find_element(by=AppiumBy.NAME, value=button).get('ELEMENT')).is_selected():
        t_driver.create_web_element(t_driver.find_element(by=AppiumBy.NAME, value=button).get('ELEMENT')).click()
def is_selected_by_id(t_driver, button):
    return t_driver.create_web_element(t_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=button).get('ELEMENT')).is_selected()
def set_element_value(element,value):
    element.clear() ; element.send_keys(value)
def set_element_value_by_id(t_driver,text_box,value):
    element = create_web_element_by_id(t_driver, text_box)
    element.clear() ; element.send_keys(value)
def get_element_value_by_id(t_driver,element_name):
    return create_web_element_by_id(t_driver, text_box).text

