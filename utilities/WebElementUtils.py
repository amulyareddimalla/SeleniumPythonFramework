import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ElementsUtil:

    def __init(self,obj1, obj2):
        global driver,loc
        driver=obj1
        loc=obj2

    def highlight(self,element):
        driver=element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style',arguments[1])",element,s)
        original_style=element.get_attribute('style')
        apply_style("border: 4px solid red")
        if (element.get_attribute("style")!=None):
            time.sleep(1)
        apply_style(original_style)

    def waitForElementDisplayed(self,locator,secs):
        wait=WebDriverWait(driver,secs)
        element=wait.until(ec.visibility_of_element_located(loc,locator))
        self.highlight(element)
        if (element==None):
            return False
        else:
            return True

    def waitForPresenceElement(self, locator, secs):
        wait = WebDriverWait(driver, secs)
        element = wait.until(ec.presence_of_element_located(loc, locator))
        self.highlight(element)
        if (element == None):
            return False
        else:
            return True


    def waitForElementClickable(self, locator, secs):
        wait = WebDriverWait(driver, secs)
        element = wait.until(ec.element_to_be_clickable(loc, locator))
        self.highlight(element)
        if (element == None):
            return False
        else:
            return True


    def waitForPageLoaded(self, title, secs):
        try:
            wait = WebDriverWait(driver, secs)
            return wait.until(ec.title_contains(title))
        except TimeoutException:
            return

    def get_element(self,locator_type,locator):
        try:
            element=getattr(driver,"find_element_by_"+locator_type)(locator)
            self.highlight(element)
            return element
        except Exception:
            print(locator, Exception)

    def get_text(self,locator_type,locator):
        try:
            element=driver.find_element(locator_type,locator)
            self.highlight(element)
            return element.text
        except Exception:
            driver.quit()

    def type(self,locator_type,locator,data):
        wait=WebDriverWait(driver,10)
        get_element=driver.find_element(locator_type,locator)
        get_element.send_keys(data)

    def click(self,locator_type,locator):
        get_element=driver.find_element(locator_type,locator)
        get_element.click()

    def select_by_visible_text(self,locator_type,locator,text):
        get_element=driver.find_element(locator_type,locator)
        get_element.click()
        get_element.select_by_visible_text(text)

    def js_click(self,locator_type,locator):
        get_element=driver.find_element(locator_type,locator)
        driver.execute_script("arguments[0].click();",get_element)

    def explicit_wait(self,wait_time,locator_type,locator):
        element=WebDriverWait(driver,wait_time).until(ec.presence_of_element_located(locator_type,locator))


    def explicit_wait2(self, wait_time, locator_type, locator):
        element = WebDriverWait(driver, wait_time).until(ec.element_to_be_clickable(locator_type, locator))

    def scroll_into_view(self,locator_type,locator):
        element=driver.find_element(locator_type,locator)
        element.location_once_scrolled_into_view



