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


# Function to perform a weighing
def perform_weighing(left_bars, right_bars):

    # Place bars on the left bowl
    for i, bar in enumerate(left_bars):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="left_{i}"]'))).send_keys(str(bar))

    # Place bars on the left bowl
    for i, bar in enumerate(right_bars):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="right_{i}"]'))).send_keys(str(bar))

    # Perform the weighing
    driver.find_element(By.CSS_SELECTOR, '[id="weigh"]').click()
    sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, '.result .button').text
    return result


# First weighing
first_result = perform_weighing([0,1,2],[3,4,5])
print(f'First weighing result: [0,1,2]{first_result}[3,4,5]')

# Reset the scale
driver.find_element(By.XPATH, '//div[@class="game"]//div[4]//button[@id="reset"]').click()


# Function to determine fake bar
def second_weighing(offset):
    if offset == 0:
        left_bars = [0]
        right_bars = [1]
    elif offset == 3:
        left_bars = [3]
        right_bars = [4]
    else:
        left_bars = [6]
        right_bars = [7]

    second_result = perform_weighing(left_bars, right_bars)
    print(f'Second weighing result: {left_bars} {second_result} {right_bars}')

    if second_result == '=':
        fake_bar = offset + 2
    elif second_result == '<':
        fake_bar = offset
    else:
        fake_bar = offset + 1

    return fake_bar


# Check the first weighing result and finding fake bar
if first_result == '=':
    fake_bar = second_weighing(6)
elif first_result == '>':
    fake_bar = second_weighing(3)
else:
    fake_bar = second_weighing(0)

print(f'The fake bar is: {fake_bar}')

# Click the button for the fake bar
driver.find_element(By.CSS_SELECTOR, f'button#coin_{fake_bar}').click()

# Get the alert message
alert = driver.switch_to.alert
alert_message = alert.text
alert.accept()
print(alert_message)

# Verify Fake bar was found
assert "Yay! You find it!" in alert_message, f"Oops! Try Again! - this is not a fake gold bar"

# Quit the browser
driver.quit()
