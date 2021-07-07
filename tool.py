import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Code/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://www.facebook.com/login')
time.sleep(0.1)
elem = driver.switch_to.active_element
elem = driver.find_element_by_name("email").click()
elem.send_keys("haikatori2510@gmail.com")
time.sleep(2)
elem = driver.find_element_by_name("pass").click()
elem.send_keys("haianh251007@")
time.sleep(2)
elem = driver.find_element_by_name("sigin").click()
time.sleep(2)
# driver.quit()