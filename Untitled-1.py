#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
import random
import time

driver=webdriver.Chrome()
# driver=webdriver.Edge()
driver.get("http://passport.takungpao.com/user/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))

driver.save_screenshot("c:/shot.png")
code_element=driver.find_element_by_id("ImgCodeLabelID")
top=code_element.location['y']
left=code_element.location['x']
right=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open("c:/shot.png")
img=im.crop((left,top,right,height))
img.save("c:/shot1.png")
# EC.visibility_of_element_located
# locator=(By.CLASS_NAME,"123")
# WebDriverWait(driver.5).until(locator)



driver.close