from asyncio import wait
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=options)
# driver.get('http://localhost/apurbo/admin.php')
driver.get('http://localhost/apurbo/index.php')
driver.maximize_window()

# Admin Site
# driver.find_element(By.ID, value="email").send_keys("ashik@test.com")
# driver.find_element(By.ID, value="password").send_keys("1234")

# driver.find_element(By.NAME,value="s_submit").click()

# Student Site

# driver.find_element(By.ID, value="s_id").send_keys("CS 2102073")
# driver.find_element(By.ID, value="s_password").send_keys("#@1234a")

# driver.find_element(By.NAME,value="reg_form").click()

# open modal

modal_button = wait.until(EC.element_to_be_clickable((By.NAME, 'reg_form')))
modal_button.click()

modal = wait.until(EC.visibility_of_element_located((By.ID, 'myModal')))

student_id_field = modal.find_element(By.NAME, 's_id')
student_id_field.send_keys('CS 2102032')


time.sleep(100)


driver.close()