from selenium.webdriver.common.by import By

class LogOutPage:

    checkout = (By.XPATH, "//a[@title='Checkout']")
    logout = (By.XPATH, '//a[text()="Logout"]')

    def __init__(self, driver):
        self.driver = driver

    def logout_user(self):
        return self.driver.find_element(*LogOutPage.logout) #if we add '*' it treats login as a tuple and treats it as line 5

    def checkout_user(self):
        return self.driver.find_element(*LogOutPage.checkout) #if we add '*' it treats login as a tuple and treats it as line 5
