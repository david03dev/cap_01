#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

sleep(3)
print("browser opened successfully")
driver.quit()

