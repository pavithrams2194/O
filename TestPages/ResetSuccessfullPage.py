from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class ResetSuccessfullPage:

    def __init__(self,driver):
        self.page_locator = "//*[text()='Reset Password link sent successfully']"
        self.ResetSuccess_driver = driver

    def check_page_loaded(self):
        """
        checks whether the ResetSuccessfull Page is loaded properly by locating the "Reset Successfull" message displayed in that page
        @return: True - if element located else throws NoSuchElementException
        """
        Driverwait.driver_wait_until_visible(self.ResetSuccess_driver, 5, self.page_locator)
        self.ResetSuccess_driver.find_element(By.XPATH,self.page_locator)
        return True