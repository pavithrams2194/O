from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driver_wait_until_visible(driver,seconds,locator):
    """
     driver waits for mentioned seconds until the element is located
    @param driver: webdriver
    @param seconds: int - Number of seconds to wait
    @param locator: str - XPATH to locate the element
    """
    WebDriverWait(driver, seconds).until(
            EC.presence_of_element_located((By.XPATH, locator)))


def driver_wait_until_clickable(driver,seconds,locator):
    """
    driver waits for mentioned seconds until the element is clickable
    @param driver: webdriver
    @param seconds: int - Number of seconds to wait
    @param locator: str - XPATH to locate the element

    """
    WebDriverWait(driver, seconds).until(
            EC.element_to_be_clickable((By.XPATH, locator)))
