from selenium.webdriver.common.by import By

class LoginPage:

    my_account = (By.XPATH, '//a[@title="My Account"]')
    login = (By.XPATH, '//a[text()="Login"]')
    email = (By.NAME, 'email')
    password = (By.ID, 'input-password')
    submit = (By.XPATH, '//input[@type="submit"]')

    '''when you create an object of this in actual test case like e2e then this
    constructor will be invoked to assign the main driver to this local driver'''
    def __init__(self, driver):
        self.driver = driver

    def my_account_login(self):
        return self.driver.find_element(*LoginPage.my_account) #if we add '*' it treats login as a tuple and treats it as line 5

    def login_user(self):
        return self.driver.find_element(*LoginPage.login) #if we add '*' it treats login as a tuple and treats it as line 5

    def email_user(self):
        return self.driver.find_element(*LoginPage.email)

    def password_user(self):
        return self.driver.find_element(*LoginPage.password)

    def submit_user(self):
        return self.driver.find_element(*LoginPage.submit)

