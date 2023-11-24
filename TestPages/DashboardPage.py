from selenium.webdriver.common.by import By

from Utility_files import Driverwait, Utilities_mod


class DashboardPage:
    def __init__(self,driver):
        self.dashboard_locator = "//h6[text()='Dashboard']"
        self.admin_locator = "//*[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Admin']"
        self.menu_locator = "//*[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name']"
        self.dashboard_driver = driver

    def check_is_dashboard_page(self):
        """
        checks whether the Dashboard Page is loaded properly by locating the "Dashboard" text displayed as title in that page
        @return: True - if element located else throws NoSuchElementException
        """
        Driverwait.driver_wait_until_visible(self.dashboard_driver,5,self.dashboard_locator)
        self.dashboard_driver.find_element(By.XPATH,self.dashboard_locator)
        return True

    def click_admin_link(self):
        """
        clicks admin link displayed in side pane
        """
        self.dashboard_driver.find_element(By.XPATH,self.admin_locator).click()

    def get_menu_list(self):
        """
        Gets the menu list displayed in side pane of Dashboard Page
        @return: list<str> - menu list displayed in side pane of Dashboard Page
        """
        menu_list = self.dashboard_driver.find_elements(By.XPATH,self.menu_locator)
        return Utilities_mod.get_text_from_elements(menu_list)