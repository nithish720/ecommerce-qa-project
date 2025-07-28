from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("demo@gmail.com")
driver.find_element(By.ID,"Password").send_keys("demo123")
driver.find_element(By.ID,"RememberMe").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

driver.close()



