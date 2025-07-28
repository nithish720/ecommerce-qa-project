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
driver.find_element(By.ID,"small-searchterms").send_keys("Asus laptop")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Add to cart']").click()

driver.find_element(By.XPATH,"//span[@class='cart-label']").click()

dr.until(EC.element_to_be_clickable((By.XPATH,"//a[@id='open-estimate-shipping-popup']"))).click()
driver.find_element(By.XPATH,"//option[@value='104']").click()
driver.find_element(By.XPATH,"//option[@value='874']").click()
driver.find_element(By.XPATH,"//input[@id='ZipPostalCode']").send_keys("400005")
driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()

driver.find_element(By.XPATH,"//input[@id='termsofservice']").click()

driver.find_element(By.XPATH,"//button[@id='checkout']").click()

#billing
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_City']").send_keys("hyderabad")
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_Address1']").send_keys("hyderabad")
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_ZipPostalCode']").send_keys("400005")
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_PhoneNumber']").send_keys("1234567898")

driver.find_element(By.XPATH,"//button[@onclick='if (!window.__cfRLUnblockHandlers) return false; Billing.save()']").click()

#shipping add
driver.find_element(By.XPATH,"//*[@id='shipping-method-buttons-container']/button").click()

#payment method
driver.find_element(By.XPATH,"//*[@id='payment-method-buttons-container']/button").click()

driver.find_element(By.XPATH,"//*[@id='payment-info-buttons-container']/button").click()

driver.find_element(By.XPATH,"//*[@id='confirm-order-buttons-container']/button").click()


driver.close()