from selenium.webdriver.common.by import By


class AddToCartPage:

    phone_pda=(By.LINK_TEXT, "Phones & PDAs")
    phoneTitle=(By.LINK_TEXT, "iPhone")
    add_to_cart=(By.ID, "button-cart")
    success_msg= (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    warning_msg=(By.XPATH, "//div[contains(@class, 'alert-danger')]//i/following-sibling::text()[contains(., 'Products marked with *** are not available in the desired quantity or not in stock!')]/parent::*")

    def __init__(self, driver):
        self.driver = driver

    def click_phone_pda(self):
        return self.driver.find_element(*AddToCartPage.phone_pda)

    def get_phone_title(self):
        return self.driver.find_element(*AddToCartPage.phoneTitle)

    def click_add_to_cart(self):
        return self.driver.find_element(*AddToCartPage.add_to_cart)

    def success_msg_validate(self):
        return self.driver.find_element(*AddToCartPage.success_msg)

    def warning_msg_validate(self):
        return self.driver.find_element(*AddToCartPage.warning_msg)



