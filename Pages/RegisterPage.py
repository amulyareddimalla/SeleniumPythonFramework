from selenium.webdriver.common.by import By

class RegisterPage:

    register = (By.XPATH, '//a[text()="Register"]')
    firstname = (By.ID, 'input-firstname')
    lastname = (By.ID, 'input-lastname')
    email = (By.ID, 'input-email')
    phone = (By.ID, 'input-telephone')
    password = (By.ID, 'input-password')
    confirm = (By.ID, 'input-confirm')
    checkbox = (By.NAME, 'agree')
    submit = (By.XPATH, '//input[@type="submit"]')
    account_created_message = (By.TAG_NAME, "h1")
    continue_button = (By.LINK_TEXT, "Continue")
    content = (By.ID, "content")

    def __init__(self, driver):
        self.driver = driver

    def register_user(self):
        return self.driver.find_element(*RegisterPage.register) #if we add '*' it treats login as a tuple and treats it as line 5

    def first_name(self):
        return self.driver.find_element(*RegisterPage.firstname)

    def last_name(self):
        return self.driver.find_element(*RegisterPage.lastname)

    def email_user(self):
        return self.driver.find_element(*RegisterPage.email)

    def phone_num(self):
        return self.driver.find_element(*RegisterPage.phone)

    def password_user(self):
        return self.driver.find_element(*RegisterPage.password)

    def confirm_password(self):
        return self.driver.find_element(*RegisterPage.confirm)

    def checkbox_click(self):
        return self.driver.find_element(*RegisterPage.checkbox)

    def submit_user(self):
        return self.driver.find_element(*RegisterPage.submit)

    def content_user(self):
        return self.driver.find_element(*RegisterPage.content)

    def account_created_user(self):
        return self.driver.find_element(*RegisterPage.account_created_message)

    def click_continue_button(self):
        return self.driver.find_element(*RegisterPage.continue_button)

