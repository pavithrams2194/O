from selenium.webdriver.common.by import By

from Utility_files import Driverwait
from Utility_files import Utilities_mod

class AdminPage:
    def __init__(self,driver):
        self.page_locator = "//*[@class = 'oxd-topbar-body-nav-tab-item' and text()='User Management ']"
        self.options_locator = "//*[@class = 'oxd-topbar-body-nav-tab-item']"
        self.adminpage_driver = driver

    def check_page_loaded(self):
        """
        checks whether the Admin Page is loaded properly by locating the "User Management" tab in that page
        @return: True - if element located else throws NoSuchElementException
        """
        Driverwait.driver_wait_until_visible(self.adminpage_driver, 5, self.page_locator)
        self.adminpage_driver.find_element(By.XPATH, self.page_locator)
        return True

    def get_options(self):
        """
        Gets the options listed in admin_page
        @return: list<str> - options listed in admin_page
        """
        options = self.adminpage_driver.find_elements(By.XPATH,self.options_locator)
        return Utilities_mod.get_text_from_elements(options)



