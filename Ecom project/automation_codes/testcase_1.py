from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("demo@gmail.com")  #email
password_field=(driver.find_element(By.ID,"Password"))   #password
password_field.send_keys("demo123")
driver.find_element(By.XPATH,"//span[@class='password-eye']").click()  #show password button

field_type = password_field.get_attribute("type")

if field_type == "text":
    # Password is visible, so we can "copy" the value directly
    copied_password = password_field.get_attribute("value")
    print("Password visible. Copied value:", copied_password)
else:
    print("Password is still hidden. Copy not allowed.")


driver.quit()