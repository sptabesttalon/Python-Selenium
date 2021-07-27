import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Python/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://facebook.com/reg')
time.sleep(5) #ok
elem = driver.find_element_by_name("lastname")
elem.send_keys("Katori")
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input")
elem.send_keys("Thoeo")
time.sleep(5) #ok
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]").click()
time.sleep(5) #năm
webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).send_keys("2000").perform()
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input")
elem.send_keys("katorithoeo1@stempmail.com")
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input")
elem.send_keys("katorithoeo1@stempmail.com")
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input").click()
time.sleep(5) #giới tính nam
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input")
elem.send_keys("haianh251007")
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[10]/button").click() #đang kí
time.sleep(360)
driver.get('https://www.facebook.com/profile.php?id=100071156294459&sk=friends')
time.sleep(5)
