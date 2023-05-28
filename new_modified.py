from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
import os
from selenium.webdriver import Firefox, FirefoxOptions
from testing import text_to_speech
audio_1 = "/home/tyrafero/Downloads/ara.wav"
audio_2 = "/home/tyrafero/Downloads/onichan.wav"
options = FirefoxOptions()
options.add_argument('-headless')
options.set_capability('marionette', False)
driver = Firefox(options=options)

filename = "output.mp3"


# Create a new Firefox browser instance using the FirefoxDriver executable file
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://www.777aoya.com/?a=login")

# Wait until the username and password fields are visible
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

# Fill in the username and password fields
username_field.send_keys("turafura")
password_field.send_keys("aashutosh1")

# Find the submit button and click it
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
submit_button.click()

time.sleep(5)

# Wait for the confirm button to appear and click it
confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='layui-layer100001']/div[3]/a")))
confirm_button.click()

# Click on the PK10 button and wait for the Speed PK10 button to appear
pk10_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='home-content']/div[2]/div[6]/div/div[1]/header/div[3]/div")))
pk10_button.click()
speed_pk10_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='div3']/li[3]/div")))
speed_pk10_button.click()

# Click on the Junior Speed PK10 button and wait for the slider button to appear
junior_speed_pk10_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/a[4]/div")))
junior_speed_pk10_button.click()


time.sleep(4)

target_time_str = "04:20"  # Define the target time for comparison
iteration =  0
while True:
    
    # WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="time"]/i'), 'drawing...'))
    # Get the time value from the field
    field_time_str = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="time"]/i'))).text
    if field_time_str == "drawing...":
        time.sleep(2)
        continue

    # Split the field time string into minutes and seconds
    minutes, seconds = field_time_str.split(":")
    # Convert minutes and seconds to integers
    minutes = int(minutes)
    seconds = int(seconds)

    # Create a timedelta object for the field time
    field_time = timedelta(minutes=minutes, seconds=seconds)

    print(field_time)

    # Create a timedelta object for the target time
    target_minutes, target_seconds = target_time_str.split(":")
    target_minutes = int(target_minutes)
    target_seconds = int(target_seconds)
    target_time = timedelta(minutes=target_minutes, seconds=target_seconds)

    # If the time in the field is not the target time, wait and continue to check again
    if field_time != target_time:
        time.sleep(1)
        continue

    if os.path.exists(audio_2):
        os.system(f"aplay {audio_2}")

    # Click on the top big button
    top_big_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="game"]/div[1]/div[1]/a[1]')))
    top_big_button.click()

    # Wait for the slider to appear
    slider = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]')))

    # Wait for the money field to become clickable, then send the desired value
    money_field = WebDriverWait(slider, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="money"]')))
    money_field.clear() # to clear the field before sending new value
    money_field.send_keys("4709")

    # Click the "send" button and wait for the confirmation alert to appear
    send_button = slider.find_element(By.XPATH, '//*[@id="send"]')
    send_button.click()
    time.sleep(3)
    confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/a')))
    confirm_button.click()

    # Unpress the top_big_button
    top_big_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="game"]/div[1]/div[1]/a[1]')))
    driver.execute_script("arguments[0].setAttribute('class', 'button')", top_big_button)

    time.sleep(2)

    # Click on the slider button to open the slider
    small_big_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="game"]/div[1]/div[1]/a[2]')))
    small_big_button.click()

    # Wait for the slider to appear
    slider = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]')))

    # Wait for the money field to become clickable, then send the desired value
    money_field = WebDriverWait(slider, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="money"]')))
    money_field.clear() # to clear the field before sending new value
    money_field.send_keys("5291")

    # Click the "send" button and wait for the confirmation alert to appear
    send_button = slider.find_element(By.XPATH, '//*[@id="send"]')
    send_button.click()

    time.sleep(3)
    confirm_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/a')))
    confirm_button.click()

    # Unpress the top_big_button
    small_big_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="game"]/div[1]/div[1]/a[2]')))
    driver.execute_script("arguments[0].setAttribute('class', 'button')", small_big_button)

    time.sleep(1)
    iteration = iteration + 1
    voice= f"{iteration} Iteration Completed"
    print(iteration)
    if os.path.exists(audio_1):
        os.system(f"aplay {audio_1}")
    
    text_to_speech(voice, filename )
    



    