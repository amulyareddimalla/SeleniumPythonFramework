from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.AddToCartPage import AddToCartPage
from Pages.LogOutPage import LogOutPage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig


class TestcaseOne(BaseClass):

    def test_register(self):
        readconfig = ReadConfig()  # create object without any argument
        self.baseURL = readconfig.getApplicationURL()
        self.reg_firstname=readconfig.getregister_firstname()
        self.reg_lastname=readconfig.getregister_lastname()
        self.reg_email=readconfig.getregister_email()
        self.reg_phone=readconfig.getregister_phone()
        self.reg_password=readconfig.getregister_password()
        self.reg_confirm_password=readconfig.getregister_confirm_password()
        self.driver.get(self.baseURL)

        loginPage = LoginPage(self.driver)
        registerPage=RegisterPage(self.driver)
        addtocartpage = AddToCartPage(self.driver)
        logoutPage = LogOutPage(self.driver)

        # Click on the 'My Account' link
        my_account_link = loginPage.my_account_login()
        my_account_link.click()

        # Wait for the 'Register' button to become clickable and click it
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(registerPage.register))
        register_button.click()

        # Fill in the registration form
        first_name_field = registerPage.first_name()
        first_name_field.send_keys(self.reg_firstname)

        last_name_field = registerPage.last_name()
        last_name_field.send_keys(self.reg_lastname)

        email_field = registerPage.email_user()
        email_field.send_keys(self.reg_email)

        phone_field = registerPage.phone_num()
        phone_field.send_keys(self.reg_phone)

        password_field = registerPage.password_user()
        password_field.send_keys(self.reg_password)

        confirm_password_field = registerPage.confirm_password()
        confirm_password_field.send_keys(self.reg_confirm_password)

        # click checkbox
        checkbox_click = registerPage.checkbox_click()
        checkbox_click.click()

        # Submit the form
        submit_button = registerPage.submit_user()
        submit_button.click()

        #validation of account creation message
        content_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(registerPage.content))
        success_msg_element = content_element.find_element(By.TAG_NAME, "h1")
        success_msg = success_msg_element.text
        print(success_msg)
        registerPage.click_continue_button().click()
        print(self.driver.title)

        # wait for the Phones & PDAs link to be visible and click it
        phones_pdas_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(addtocartpage.phone_pda))
        phones_pdas_link.click()

        # wait for the iPhone link to be visible and click it
        iphone_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(addtocartpage.phoneTitle))
        iphone_link.click()

        # wait for the Add to Cart button to be visible and click it
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(addtocartpage.add_to_cart))
        add_to_cart_button.click()

        # wait for the success message to be visible and validate its text
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                addtocartpage.success_msg))
        assert "Success" in success_message.text.strip()
        success_message_text = success_message.text.strip()
        print(success_message_text)

        # Click on Checkout button
        logoutPage.checkout_user().click()

        # Validate if 'Products marked with *** are not available in the desired quantity or not in stock!' message is displayed
        message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(addtocartpage.warning_msg))
        assert message.is_displayed()
        message_output = message.text.strip()
        print(message_output)

        # Click on the 'My Account' link
        my_account_link = loginPage.my_account_login()
        my_account_link.click()

        # Wait for the 'Logout' button to become clickable and click it
        Logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(logoutPage.logout_user()))
        Logout_button.click()

