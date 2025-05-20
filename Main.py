#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

wait = WebDriverWait(driver,10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys("admin")

password = "admin123"
wait.until(EC.presence_of_element_located((By.NAME,"password"))).send_keys(password)

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
login_btn.click()

confirmation_status = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']//h6[text()='Dashboard']"))).text

print(f"Webpage title is : {driver.title}")
if "Dashboard" in confirmation_status:
    print("TC_01 passed ")
else:
    print("TC_01 failed")

driver.quit()
