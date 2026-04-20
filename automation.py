from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("file:///D:/Python workspace/Reg page/registration.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.ID, "fname"))).send_keys("Prakash")
driver.find_element(By.ID, "lname").send_keys("Mandwal")
driver.find_element(By.ID, "email").send_keys("prakash@email.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "designation").send_keys("QA Engineer")

# Click Register Button
driver.find_element(By.ID, "register").click()

input("Press Enter to close browser...")

driver.quit()