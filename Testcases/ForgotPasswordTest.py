import time
import unittest

from selenium.common import NoSuchElementException

from TestPages.LoginPage import LoginPage
from TestPages.ResetPasswordPage import ResetPasswordPage
from TestPages.ResetSuccessfullPage import ResetSuccessfullPage
from Utility_files.Utilities_mod import Utilities

# TC_PIM_01
# Forgot Password link validation on login page


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize driver and launch URL before all test cases
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.loginpage_obj = LoginPage(self.driver)
        self.reset_pswd_obj = ResetPasswordPage(self.driver)
        self.reset_success_obj = ResetSuccessfullPage(self.driver)

    def test_ResetPassword(self):
        # Test Forgot Password link in login Page
        #     click on forgot password link
        #     Verify if driver navigated to Reset Password page
        #     Enter valid username in Reset Password page
        #     click reset button
        #     Verify if reset successfull message appears
        self.loginpage_obj.click_forgot_password()
        self.assertEqual(True,self.reset_pswd_obj.check_page_loaded())
        self.reset_pswd_obj.enter_username("Admin")
        self.reset_pswd_obj.click_reset_button()
        self.assertEqual(True,self.reset_success_obj.check_page_loaded())
        self.utility_obj.take_screenshot()

    def test_username_required_tip(self):
        # Test whether username required tool tip appears in Reset Password Page
        #     click on forgot password link
        #     click reset password button without giving username
        #     Verify whether username required tool tip appears
        #     Enter valid username
        #     Verify whether username required tool tip disappears
        #     click reset button
        #     Verify if reset successfull message appears
        self.loginpage_obj.click_forgot_password()
        self.reset_pswd_obj.click_reset_button()
        self.assertEqual(True, self.reset_pswd_obj.check_required_visiblity())
        self.reset_pswd_obj.enter_username("admin123")

        try:
            self.assertEqual(True, self.reset_pswd_obj.check_required_visiblity())
        except NoSuchElementException:
            self.assertEqual(True,True)

        self.reset_pswd_obj.click_reset_button()
        self.assertEqual(True,self.reset_success_obj.check_page_loaded())
        self.utility_obj.take_screenshot()

    def test_cancel_button(self):
        # Test Cancel button in Reset Password Page
        #     click on forgot password link
        #     Enter valid username in Reset Password page
        #     click cancel button
        #     Verify whether the driver navigates to Login Page again
        self.loginpage_obj.click_forgot_password()
        self.reset_pswd_obj.enter_username("Admin")
        self.reset_pswd_obj.click_cancel_button()
        self.assertEqual(True,self.loginpage_obj.check_page_loaded())
        self.utility_obj.take_screenshot()


if __name__ == '__main__':
    unittest.main()
