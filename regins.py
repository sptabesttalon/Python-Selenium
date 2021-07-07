import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Python/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://www.instagram.com/')
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]").click()
time.sleep(5) #Đăng nhập bằng fb
elem = driver.find_element_by_name("email")
elem.send_keys("khang.tuan.tran112")
time.sleep(1)
elem = driver.find_element_by_name("pass")
elem.send_keys("haianh251007")
time.sleep(1)
elem = driver.find_element_by_name("login").click()
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/form/div/div[1]/div[1]/div/div/div[3]/button[1]").click()
time.sleep(10) #Tiếp tục với fb
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div[2]/div/div/div/div/div[2]/button").click()
time.sleep(10) #Đồng ý vs ...
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/form/div[2]/div/label/input")
elem.send_keys("a100070482240579")
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/form/div[3]/div/label/input")
elem.send_keys("haianh251007")
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/form/div[4]/div/button").click()
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div[2]/div/div/div[2]/button").click()
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(10)
driver.get('https://www.instagram.com/a100070482240579')
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/div/button").click()
elem.send_keys("C:/Python/Anh/download(2).jpg")
time.sleep(10)
driver.get('https://www.instagram.com/p/CAPg34mAxl7/')
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
elem.send_key("frp19x4ckk9mk2dze1kfayoq7qx0fnyq")
time.sleep(10)
elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]").click()
time.sleep(10)
