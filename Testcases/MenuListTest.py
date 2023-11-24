import unittest

from TestPages.DashboardPage import DashboardPage
from Utility_files import Utilities_mod
from Utility_files.Utilities_mod import Utilities

# TC_PIM_03
# Main menu Validation on Admin Page


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize driver and launch URL
        # Login into Admin Page before all test cases
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.utility_obj.login_into_orangehrm()
        self.dashboardpage_obj = DashboardPage(self.driver)

    def test_menu_list(self):
        # Test whether the provided options are viewable in Dashboard Page
        #       check whether the Dashboard page is loaded properly
        #       menu_list : Get the options listed on Dashboard page
        #       test_list : Get the menu_list from the test data file
        #       Test whether the test_list matches with the menu_list
        self.dashboardpage_obj.check_is_dashboard_page()
        menu_list=self.dashboardpage_obj.get_menu_list()
        test_list = self.utility_obj.get_test_data().get("menu_list")
        self.assertEqual(True, Utilities_mod.compare_list(menu_list,test_list))  # add assertion here
        self.utility_obj.take_screenshot()


if __name__ == '__main__':
    unittest.main()
