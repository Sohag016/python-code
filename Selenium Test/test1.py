import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=options)
# driver.get('http://localhost/apurbo/admin.php')
driver.get('http://localhost/apurbo/index.php')
driver.maximize_window()


# Wait for the page to load and the modal button to be clickable
wait = WebDriverWait(driver, 10)
modal_button = wait.until(EC.element_to_be_clickable((By.NAME, 'reg_form')))
time.sleep(1)  # Introduce a delay of 1 second

# Click the button to open the modal
modal_button.click()

# Wait for the modal to be visible
modal = wait.until(EC.visibility_of_element_located((By.ID, 'myModal')))
time.sleep(1)  # Introduce a delay of 1 second

# Fill in the form fields inside the modal
student_id_field = modal.find_element(By.NAME, 's_id')
student_id_field.send_keys('CS 2102032')
time.sleep(1)  # Introduce a delay of 1 second

# The password field is disabled and pre-filled in this example
# password_field = modal.find_element(By.NAME, 's_password')
# password_field.send_keys('1234')

# Select an option from the 'Department' dropdown
department_dropdown = Select(modal.find_element(By.NAME, 's_department'))
department_dropdown.select_by_visible_text('CSE')
time.sleep(1)  # Introduce a delay of 1 second

# Fill in more fields as necessary
name_field = modal.find_element(By.NAME, 's_name')
name_field.send_keys('John Doe')
time.sleep(1)  # Introduce a delay of 1 second

gender_dropdown = Select(modal.find_element(By.NAME, 's_gender'))
gender_dropdown.select_by_visible_text('Male')
time.sleep(1)  # Introduce a delay of 1 second

age_field = modal.find_element(By.NAME, 's_age')
age_field.send_keys('25')
time.sleep(1)  # Introduce a delay of 1 second

blood_dropdown = Select(modal.find_element(By.NAME, 's_blood'))
blood_dropdown.select_by_visible_text('A+')
time.sleep(1)  # Introduce a delay of 1 second

total_donated_field = modal.find_element(By.NAME, 's_total_donated')
total_donated_field.send_keys('5')
time.sleep(1)  # Introduce a delay of 1 second

last_donated_field = modal.find_element(By.NAME, 's_last_donated')
last_donated_field.send_keys('2024-07-01')
time.sleep(1)  # Introduce a delay of 1 second

city_field = modal.find_element(By.NAME, 's_city')
city_field.send_keys('New York')
time.sleep(1)  # Introduce a delay of 1 second

number_field = modal.find_element(By.NAME, 's_number')
number_field.send_keys('1234567890')
time.sleep(1)  # Introduce a delay of 1 second

# Wait for the submit button within the modal to be clickable
submit_button = wait.until(EC.element_to_be_clickable((By.NAME, 'r_submit')))
time.sleep(1)  # Introduce a delay of 1 second

# Click the submit button
submit_button.click()

# You can add additional actions here, like waiting for the next page to load
wait.until(EC.title_contains('Expected Title After Submission'))
time.sleep(2)  # Introduce a longer delay of 2 seconds

print("Form submitted successfully!")

# Close the browser
driver.quit()