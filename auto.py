import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Code/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://facebook.com/')
time.sleep(0.1) #ok
elem = driver.switch_to.active_element
elem = driver.find_element_by_id("email")
elem.send_keys("haikatori2510@gmail.com")
time.sleep(0.1)
elem = driver.find_element_by_id("pass")
elem.send_keys("haianh251007@")
time.sleep(0.1)
elem = driver.find_element_by_name("login").click()
time.sleep(0.1)

# driver.quit()