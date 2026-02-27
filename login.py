from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC 
import time
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")    

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user-name")))
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# 等待登录成功后的页面加载
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

# 验证登录成功
assert "inventory" in driver.current_url
print("登录成功！")

time.sleep(3)  # 让你看到结果
driver.quit()