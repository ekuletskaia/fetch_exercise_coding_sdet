from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=20)

# open the url
driver.get('http://sdetchallenge.fetch.com/')


# First weighing
# left bowl
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="left_0"]')))
left_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="left_0"]')
left_bowl_0_grid.send_keys('0')

left_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="left_1"]')
left_bowl_0_grid.send_keys('1')

left_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="left_2"]')
left_bowl_0_grid.send_keys('2')

# second bowl
right_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="right_0"]')
right_bowl_0_grid.send_keys('3')

right_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="right_1"]')
right_bowl_0_grid.send_keys('4')

right_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="right_2"]')
right_bowl_0_grid.send_keys('5')

# weigh the bars
driver.find_element(By.CSS_SELECTOR, '[id="weigh"]').click()

# get the result
sleep(2)
result = driver.find_element(By.CSS_SELECTOR, '.result .button').text
print(f'First weighing result: {result}')

# reset
driver.find_element(By.XPATH, '//div[@class="game"]//div[4]//button[@id="reset"]').click()

# Second Weighing
# determine the fake bar
if result == '=':
    offset = 6
    # first bowl
    left_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="left_0"]')
    left_bowl_0_grid.send_keys('6')
    # second bowl
    right_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="right_0"]')
    right_bowl_0_grid.send_keys('7')

    # weigh the bars
    driver.find_element(By.CSS_SELECTOR, '[id="weigh"]').click()

    # get the result
    sleep(3)
    result_2 = driver.find_element(By.CSS_SELECTOR, '.result .button').text

    if result_2 == '=':
        print(f'{offset + 2} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_8').click()
    elif result_2 == '<':
        print(f'{offset + 0} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_6').click()
    else:
        print(f'{offset + 1} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_7').click()

elif result == '>':
    offset = 3
    # first bowl
    left_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="left_0"]')
    left_bowl_0_grid.send_keys('3')
    # second bowl
    right_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="right_0"]')
    right_bowl_0_grid.send_keys('4')

    # weigh the bars
    driver.find_element(By.CSS_SELECTOR, '[id="weigh"]').click()

    # get the result
    sleep(3)
    result_2 = driver.find_element(By.CSS_SELECTOR, '.result .button').text

    if result_2 == '=':
        print(f'{offset + 2} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_5').click()
    elif result_2 == '<':
        print(f'{offset + 0} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_3').click()
    else:
        print(f'{offset + 1} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_4').click()

else:
    offset = 0
    # first bowl
    left_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="left_0"]')
    left_bowl_0_grid.send_keys('0')
    # second bowl
    right_bowl_0_grid = driver.find_element(By.CSS_SELECTOR, '[id="right_0"]')
    right_bowl_0_grid.send_keys('1')

    # weigh the bars
    driver.find_element(By.CSS_SELECTOR, '[id="weigh"]').click()

    # get the result
    sleep(3)
    result_2 = driver.find_element(By.CSS_SELECTOR, '.result .button').text

    if result_2 == '=':
        print(f'{offset + 2} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_2').click()
    elif result_2 == '<':
        print(f'{offset + 0} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_0').click()
    else:
        print(f'{offset + 1} is the fake bar')
        driver.find_element(By.CSS_SELECTOR, 'button#coin_1').click()


# Get the alert message
alert = driver.switch_to.alert
actual_message = alert.text
alert.accept()
print(actual_message)

# Verify Fake bar was found
assert "Yay! You find it!" in actual_message, f"Oops! Try Again! - this is not a fake gold bar"

# Quit the browser
driver.quit()
