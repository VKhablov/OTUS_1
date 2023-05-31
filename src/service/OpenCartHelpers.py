from selenium.common import ElementNotInteractableException

from src.service.BasePage import BasePage
from src.service.Locators import OpenCartSearchLocators, OpenCartAccountLocators


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(OpenCartSearchLocators.LOCATOR_OPENCART_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(OpenCartSearchLocators.LOCATOR_OPENCART_SEARCH_BUTTON, ).click()


class AccountHelper(BasePage):
    def open_register_page(self):
        self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_ACCOUNT_BUTTON).click()
        if self.wait_until_clickable(OpenCartAccountLocators.LOCATOR_OPENCART_REGISTER_BUTTON):
            self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_REGISTER_BUTTON).click()
        else:
            raise ElementNotInteractableException

    def open_authorize_page(self):
        self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_ACCOUNT_BUTTON, ).click()
        if self.wait_until_clickable(OpenCartAccountLocators.LOCATOR_OPENCART_AUTHORIZE_BUTTON, ):
            self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_AUTHORIZE_BUTTON, ).click()
        else:
            raise ElementNotInteractableException

    def help_register(self, name, surname, email, phone, password, confirm_pass):
        name_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_NAME_FIELD, )
        surname_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_SURNAME_FIELD, )
        email_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_EMAIL_FIELD, )
        phone_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_PHONE_FIELD, )

        pass_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_PASS_FIELD, )
        confirm_pass_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_CONFIRM_PASS_FIELD)

        policy_field = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_CONFIRM_POLICY_CHECKBOX)

        continue_button = self.find_element(OpenCartAccountLocators.LOCATOR_OPENCART_CONFIRM_REGISTER_BUTTON)

        name_field.click()
        name_field.send_keys(name)

        surname_field.click()
        surname_field.send_keys(surname)

        email_field.click()
        email_field.send_keys(email)

        phone_field.click()
        phone_field.send_keys(phone)

        pass_field.click()
        pass_field.send_keys(password)

        confirm_pass_field.click()
        confirm_pass_field.send_keys(confirm_pass)

        policy_field.click()
        continue_button.click()

        return {"name_field": name_field,
                "surname_field": surname_field,
                "email_field": email_field,
                "phone_field": phone_field,
                "pass_field": pass_field,
                "confirm_pass_field": confirm_pass_field}

    def check_successful_registration(self):
        if self.find_element(OpenCartAccountLocators.LOCATOR_SUCCESSFUL_REGISTRATION):
            return True
        else:
            return False
