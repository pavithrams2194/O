from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class ResetPasswordPage:
    def __init__(self,driver):
        self.reset_pswd_driver = driver
        self.username_locator = "//input[@name = 'username']"
        self.reset_pswd_locator = "//button[text()=' Reset Password ']"
        self.cancel_button_locator = "//button[text()=' Cancel ']"
        self.page_locator = "//*[text()='Reset Password']"
        self.required_locator="//*[text()='Required']"

    def enter_username(self,username_text):
        """
        Enters text in username textbox
        @param username_text: <str> - to be entered in username textbox
        """
        Driverwait.driver_wait_until_visible(self.reset_pswd_driver, 5, self.username_locator)
        self.reset_pswd_driver.find_element(By.XPATH, self.username_locator).send_keys(username_text)

    def click_reset_button(self):
        """
         clicks Reset password button displayed in Reset Password page
        """
        Driverwait.driver_wait_until_clickable(self.reset_pswd_driver, 5, self.reset_pswd_locator)
        self.reset_pswd_driver.find_element(By.XPATH,self.reset_pswd_locator).click()

    def click_cancel_button(self):
        """
         clicks cancel button displayed in Reset Password page
        """
        self.reset_pswd_driver.find_element(By.XPATH,self.cancel_button_locator).click()

    def check_page_loaded(self):
        """
        checks whether the ResetPassword Page is loaded properly by locating the "Reset Password" text displayed as title in that page
        @return: True - if element located else throws NoSuchElementException
        """
        Driverwait.driver_wait_until_visible(self.reset_pswd_driver, 5, self.page_locator)
        return True

    def check_required_visiblity(self):
        """
        checks whether the required tool tip is visible below username textbox
        @return: True - if element located else throws NoSuchElementException
        """
        self.reset_pswd_driver.find_element(By.XPATH,self.required_locator)
        return True




