#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(5)

driver.find_element(by=By.NAME,value="username").send_keys("admin")
sleep(3)
password = "admin123"
driver.find_element(by=By.NAME,value="password").send_keys(password)
sleep(3)
login_btn = driver.find_element(by=By.XPATH,value="//button[@type='submit']")
sleep(3)
login_btn.click()
sleep(5)

sleep(3)
print("browser opened successfully")
driver.quit()
