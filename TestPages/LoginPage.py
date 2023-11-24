from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class LoginPage:

    def __init__(self,driver):
        self.forgot_password_locator = "//p[contains(.,'Forgot')]"
        self.username_locator = "//*[@name='username']"
        self.password_locator = "//*[@name='password']"
        self.login_button_locator = "//button[text()=' Login ']"
        self.loginpage_driver = driver

    def click_forgot_password(self):
        """
         clicks on the forgot password link displayed in login Page
        """
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.forgot_password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.forgot_password_locator).click()

    def check_page_loaded(self):
        """
        checks whether the Login Page is loaded properly by locating the "Forgot Password" link in that page
        @return: True - if element located else throws NoSuchElementException

        """
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.forgot_password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.forgot_password_locator)
        return True

    def enter_username(self, username_text):
        """
        Enters text in username textbox
        @param username_text: <str> - to be entered in username textbox
        """
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.username_locator)
        self.loginpage_driver.find_element(By.XPATH, self.username_locator).send_keys(username_text)

    def enter_password(self, password_text):
        """
        Enters text in password textbox
        @param password_text: <str> - to be entered in password textbox
        """
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.password_locator).send_keys(password_text)

    def click_login_button(self):
        """
        clicks login button displayed in login page
        """
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.login_button_locator)
        self.loginpage_driver.find_element(By.XPATH, self.login_button_locator).click()



