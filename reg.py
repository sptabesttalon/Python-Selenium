#Tool reg fb chạy bằng m.fb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Code/Chromedriver.exe")
driver.maximize_window ()

driver.get('https://m.facebook.com/')
time.sleep(3) #ok
elem = driver.switch_to.active_element
elem = driver.find_element_by_id("signup-button").click()
time.sleep(3)#ok
elem = driver.find_element_by_id("firstname_input")
elem.send_keys("Lam Ngân")
time.sleep(5)
elem = driver.find_element_by_id("lastname_input")
elem.send_keys("Hoang")
time.sleep(5) #ok
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]").click()
time.sleep(5)#ok
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/select").click()
time.sleep(5) #năm
webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).send_keys("2000").perform()
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]").click()
time.sleep(5) #tiếp
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[11]/div/a[1]").click()
time.sleep(5) #=email
elem = driver.find_element_by_id("contactpoint_step_input")
elem.send_keys("vosoxis523@awinceo.com")
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]").click() #tiếp
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[6]/div[3]/div/div/div[3]/div/label[2]/div/div/div[2]/input").click()
time.sleep(5) #giới tính nam
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]").click()#tiếp
time.sleep(5)
elem = driver.find_element_by_id("password_step_input")
elem.send_keys("haianh251007")
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[4]").click() #đang kí
time.sleep(5)
