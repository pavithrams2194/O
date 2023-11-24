import unittest

from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.common import TimeoutException
from TestPages.AdminPage import AdminPage
from TestPages.DashboardPage import DashboardPage
from Utility_files import Utilities_mod
from Utility_files.Utilities_mod import Utilities

#TC_PIM_02
# Header validation on Admin Page

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize driver and launch URL
        # Login into Admin Page before all test cases
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.utility_obj.login_into_orangehrm()
        self.dashboardpage_obj = DashboardPage(self.driver)
        self.admin_page_obj = AdminPage(self.driver)

    def test_admin_page(self):
        # Test whether the provided options(test data) are viewable in Admin Page
        #       check whether the title of the page is "OrangeHRM"
        #       click on Admin link on side pane
        #       admin_page_options : Get the options listed on Admin page
        #       test_data_options : Get the options_list from the test data file
        #       Test whether the test_data_options matches with admin_page_options
        try:
            self.assertEqual("OrangeHRM", self.driver.title)
            self.dashboardpage_obj.check_is_dashboard_page()
            self.dashboardpage_obj.click_admin_link()
            self.admin_page_obj.check_page_loaded()
            admin_page_options=self.admin_page_obj.get_options()
            test_data_options = self.utility_obj.get_test_data().get("options_list")
            self.assertEqual(True, Utilities_mod.compare_list(test_data_options,admin_page_options))
            self.utility_obj.take_screenshot()
        except (NoSuchElementException,TimeoutException,InvalidSelectorException) as e:
            self.utility_obj.take_failed_screenshot()
            print(e)

if __name__ == '__main__':
    unittest.main()
