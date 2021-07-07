import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Python/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://fb.vieclamonline.org/login')
time.sleep(5)
elem = driver.find_element_by_name("username")
elem.send_keys("sptabesttalon2")
time.sleep(5)
elem = driver.find_element_by_name("password")
elem.send_keys("haianh251007")
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div/button/span").click()
time.sleep(3)
driver.get('https://fb.vieclamonline.org/account/manager/instagram')
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(180)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(180)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(180)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(180)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(180)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(180)
