
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    """
    Waits for an element to be present and visible on the page.
    :param driver: WebDriver instance
    :param locator: tuple with the type of locator and the locator string
    :param timeout: maximum time to wait for the element
    :return: the WebElement object
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))

def wait_for_text_to_be_present_in_element(driver, locator, text, timeout=10):
    """
    Waits for the specified text to be present in the specified element.
    :param driver: WebDriver instance
    :param locator: tuple with the type of locator and the locator string
    :param text: the text to wait for
    :param timeout: maximum time to wait for the text to be present
    :return: True if the text is present, False otherwise
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.text_to_be_present_in_element(locator, text))

def wait_for_element_to_be_clickable(driver, locator, timeout=10):
    """
    Waits for an element to be clickable (i.e., can be clicked).
    :param driver: WebDriver instance
    :param locator: tuple with the type of locator and the locator string
    :param timeout: maximum time to wait for the element to be clickable
    :return: the WebElement object
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))

def wait_for_element_to_be_selected(driver, locator, timeout=10):
    """
    Waits for an element to be selected (i.e., checked or selected in a dropdown).
    :param driver: WebDriver instance
    :param locator: tuple with the type of locator and the locator string
    :param timeout: maximum time to wait for the element to be selected
    :return: the WebElement object
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_selected(locator))

def wait_for_visibility_of_element_located(driver, locator, timeout=10):
    """
    Waits for an element to be present and visible on the page.
    :param driver: WebDriver instance
    :param locator: tuple with the type of locator and the locator string
    :param timeout: maximum time to wait for the element to be visible
    :return: the WebElement object
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))
