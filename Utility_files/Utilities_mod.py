import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TestPages.LoginPage import LoginPage
from selenium import webdriver
from pathlib import Path
from datetime import datetime


def get_text_from_elements(ele_list):
    """
    converts list of webelements to list of strings by extracting the inner text present in corresponding webelemnt
    @param ele_list: list<WebElement>
    @return: list<str>
    """
    text_list = []
    for ele in ele_list:
        text_list.append(ele.text)
    return text_list


def compare_list(list1, list2):
    """
    checks whether two lists are equal
    @param list1: list<str>
    @param list2: list<str>
    @return: True - if both the list are equal else returns False
    """
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


class Utilities:
    file_open = None

    def __init__(self):
        self.utilities_driver = None
        self.loginpage_obj =None

    @classmethod
    def get_root_directory(cls):
        """
        @return: str - path of project directory
        """
        return str(Path(os.getcwd()).parent)

    @classmethod
    def get_test_data(cls):
        """
        creates object for testdata file "AdminPageData.json"
        @return: object of json file
        """
        cls.file_open = open(cls.get_root_directory() + "/TestData/AdminPageData.json")
        test_data = json.load(cls.file_open)
        cls.file_open.close()
        return test_data

    def initialize_driver(self):
        """
        initialize webdriver and launch OrangeHRM URL
        @return: webdriver
        """
        self.utilities_driver = webdriver.Chrome()
        self.utilities_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.utilities_driver.maximize_window()
        return self.utilities_driver

    def login_into_orangehrm(self):
        """
        login into OrangeHRM portal using Admin credentials
        """
        self.loginpage_obj = LoginPage(self.utilities_driver)
        self.utilities_driver.implicitly_wait(5)
        self.loginpage_obj.enter_username("Admin")
        self.loginpage_obj.enter_password("admin123")
        self.loginpage_obj.click_login_button()

    def take_screenshot(self):
        """
        Takes screenshot of current webpage and stores in "/TestResult/Screenshots/" inside current project folder.
        Saves the screenshot as png file and has the name of current system date and time.
        """
        filename = (datetime.now()).strftime("%d%m%Y %H%M%S")+".png"
        screenshot_folder = "/TestResult/Screenshots/"
        self.utilities_driver.get_screenshot_as_file(self.get_root_directory()+screenshot_folder+filename)

    def take_failed_screenshot(self):
        """
        Takes screenshot of current webpage and stores in "/TestResult/FailedScreenshots/" inside current project folder.
        Saves the screenshot as png file and has the name of current system date and time
        """
        filename = (datetime.now()).strftime("%d%m%Y %H%M%S") + ".png"
        screenshot_folder = "/TestResult/FailedScreenshots/"
        self.utilities_driver.get_screenshot_as_file(self.get_root_directory() + screenshot_folder + filename)

