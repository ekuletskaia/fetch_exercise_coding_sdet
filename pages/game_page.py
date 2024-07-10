from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class GamePage(Page):
    WEIGH_BTN = (By.CSS_SELECTOR, '[id="weigh"]')
    RESULT = (By.CSS_SELECTOR, '.result .button')
    RESET_BTN = (By.XPATH, '//div[@class="game"]//div[4]//button[@id="reset"]')
    FAKE_BAR_BTN_TEMPLATE = 'button#coin_{}'

    def __init__(self, driver):
        super().__init__(driver)
        self.alert_message = None

    def perform_first_weighing(self):
        def perform_weighing(self, left_bars, right_bars):
            # Place bars on the left bowl
            for i, bar in enumerate(left_bars):
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="left_{i}"]'))).send_keys(
                    str(bar))

            # Place bars on the left bowl
            for i, bar in enumerate(right_bars):
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="right_{i}"]'))).send_keys(
                    str(bar))

            # Perform the weighing
            self.driver.find_element(*self.WEIGH_BTN).click()
            sleep(2)
            result = self.driver.find_element(*self.RESULT).text
            return result

        # First weighing
        self.first_result = perform_weighing(self, [0, 1, 2], [3, 4, 5])
        print(f'First weighing result: [0,1,2]{self.first_result}[3,4,5]')

    def click_reset(self):
        self.find_element(*self.RESET_BTN).click()

    def perform_second_weighing(self):
        def perform_weighing(left_bars, right_bars):
            # Place bars on the left bowl
            for i, bar in enumerate(left_bars):
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="left_{i}"]'))).send_keys(
                    str(bar))

            # Place bars on the right bowl
            for i, bar in enumerate(right_bars):
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[id="right_{i}"]'))).send_keys(
                    str(bar))

            # Perform the weighing
            self.driver.find_element(*self.WEIGH_BTN).click()
            sleep(2)
            result = self.driver.find_element(*self.RESULT).text
            return result

        first_result = self.first_result

        if first_result == '=':
            offset = 6
            result_2 = perform_weighing([6], [7])
            print(f'Second weighing result: [6]{self.first_result}[7]')

            if result_2 == '=':
                self.fake_bar = 8
            elif result_2 == '<':
                self.fake_bar = 6
            else:
                self.fake_bar = 7

        elif first_result == '>':
            offset = 3
            result_2 = perform_weighing([3], [4])
            print(f'Second weighing result: [3]{self.first_result}[4]')

            if result_2 == '=':
                self.fake_bar = 5
            elif result_2 == '<':
                self.fake_bar = 3
            else:
                self.fake_bar = 4

        else:
            offset = 0
            result_2 = perform_weighing([0], [1])
            print(f'Second weighing result: [0]{self.first_result}[1]')

            if result_2 == '=':
                self.fake_bar = 2
            elif result_2 == '<':
                self.fake_bar = 0
            else:
                self.fake_bar = 1

        print(f'The fake bar is: {self.fake_bar}')

    def click_fake_bar(self):
        fake_bar = self.fake_bar
        self.driver.find_element(By.CSS_SELECTOR, self.FAKE_BAR_BTN_TEMPLATE.format(fake_bar)).click()

    def get_alert_message(self):
        alert = self.driver.switch_to.alert
        self.alert_message = alert.text
        alert.accept()
        print(self.alert_message)

    def verify_fake_bar(self, message):
        assert message in self.alert_message, f"Expected message '{message}' but got '{self.alert_message}'"
