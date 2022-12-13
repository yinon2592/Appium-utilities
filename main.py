import pyperclip
from appium import webdriver
from appium.webdriver.common import appiumby
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from helper import *
from time import sleep
import sys
desired_caps = {'app': <path to app file><file name>.exe', 'platformName': "Windows",'deviceName': "WindowsPC"}
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)


new_window_driver = switch_window(driver.window_handles[0])
new_window_driver.save_screenshot('<path to save in>''filename.png')
new_window_driver.close()


