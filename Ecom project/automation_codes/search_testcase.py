from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

dr = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("demo12@gmail.com")
driver.find_element(By.ID,"Password").send_keys("demo123")
driver.find_element(By.ID,"RememberMe").click()

#login
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

#search
driver.find_element(By.ID,"small-searchterms").send_keys("Asus N551JK")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()

driver.save_screenshot("screenshot.png")


driver.quit()
