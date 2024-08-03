# Find Fake Gold Bar Automation Project

This project automates the process of finding a fake gold bar on the website [http://sdetchallenge.fetch.com/](http://sdetchallenge.fetch.com/) using Selenium with Python and Behave.

## Requirements

- Python 3.7+
- Google Chrome Browser
- Chrome WebDriver (installed automatically using `webdriver_manager`)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/ekuletskaia/find_fake_gold_bar_sdet.git
    cd find-fake-gold-bar_sdet
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Install ChromeDriver:

    ```bash
    # ChromeDriver will be installed automatically using `webdriver_manager`.
    ```

## Running the Tests

You have two options to run the tests:

1. **Run the Behave tests with Allure results:**

    ```bash
    behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/game_find_fake_bar.feature
    ```

2. **Run the Behave test directly:**

    ```bash
    behave features/tests/game_find_fake_bar.feature
    ```

## Generate Allure Report

1. **Generate Allure Report:**

    ```bash
    allure serve test_results/
    ```

## Project Structure

- **features/**
  - `game_find_fake_bar.feature`: Contains the feature file with the scenario for finding the fake bar.
  - **steps/**: Contains the step definitions for the feature file.

- **pages/**
  - `base_page.py`: Base page class with common methods.
  - `game_page.py`: Page object for the game page.


## Additional Notes

- Ensure that Google Chrome is installed on your machine.
- Modify the `browser_init` function in `environment.py` if you need to run tests on a different browser.
