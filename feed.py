import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:/Python/Chromedriver.exe")
# driver.maximize_window ()

# driver.get('https://facebook.com/')
# time.sleep(0.1)
# elem = driver.find_element_by_name("email")
# elem.send_keys("tathilang@stempmail.com")
# time.sleep(3)
# elem = driver.find_element_by_name("pass")
# elem.send_keys("haianh251007")
# time.sleep(0.1)
# elem = driver.find_element_by_name("login").click()
# time.sleep(3)
# # driver.get('https://www.facebook.com/profile.php?id=100069940740767&sk=friends')
# # time.sleep(0.1)

elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/div/button").click()
elem.send_key("C:/Python/Anh/download(1).jpg")
time.sleep(1)