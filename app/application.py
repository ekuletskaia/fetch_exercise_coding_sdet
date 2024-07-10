from pages.base_page import Page
from pages.game_page import GamePage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.game_page = GamePage(driver)