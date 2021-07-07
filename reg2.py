import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Code/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://facebook.com/reg')
time.sleep(3) #ok
elem = driver.find_element_by_name("lastname")
elem.send_keys("Nea ")
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input")
elem.send_keys("Nopro")
time.sleep(1) #ok
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]").click()
time.sleep(1) #năm
webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).send_keys("2000").perform()
time.sleep(1)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input")
elem.send_keys("neanopro1712@stempmail.com")
time.sleep(1)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input")
elem.send_keys("neanopro1712@stempmail.com")
time.sleep(1)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input").click()
time.sleep(1) #giới tính nam
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input")
elem.send_keys("haianh251007")
time.sleep(1)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[10]/button").click() #đang kí
time.sleep(1)
