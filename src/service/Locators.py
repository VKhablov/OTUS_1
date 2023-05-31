from selenium.webdriver.common.by import By


class OpenCartSearchLocators:
    LOCATOR_OPENCART_SEARCH_FIELD = (By.XPATH, '//input[@type="text" and @name="search"]')
    LOCATOR_OPENCART_SEARCH_BUTTON = (By.XPATH, '//div[@id="search"]/span/button[@type="button"]')


class OpenCartAccountLocators:
    # main page locators
    LOCATOR_OPENCART_ACCOUNT_BUTTON = (By.XPATH, '//span[contains(text(), "Личный кабинет")]')
    LOCATOR_OPENCART_REGISTER_BUTTON = (By.XPATH, '//a[contains(text(), "Регистрация")]')
    LOCATOR_OPENCART_AUTHORIZE_BUTTON = (By.XPATH, '//a[contains(text(), "Авторизация")]')

    # register page locators
    LOCATOR_OPENCART_NAME_FIELD = (By.XPATH, '//input[@name="firstname"]')
    LOCATOR_OPENCART_SURNAME_FIELD = (By.XPATH, '//input[@name="lastname"]')
    LOCATOR_OPENCART_EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    LOCATOR_OPENCART_PHONE_FIELD = (By.XPATH, '//input[@name="telephone"]')

    LOCATOR_OPENCART_PASS_FIELD = (By.XPATH, '//input[@name="password"]')
    LOCATOR_OPENCART_CONFIRM_PASS_FIELD = (By.XPATH, '//input[@name="confirm" and @placeholder="Подтверждение пароля"]')

    LOCATOR_OPENCART_CONFIRM_REGISTER_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Продолжить"]')

    LOCATOR_OPENCART_CONFIRM_POLICY_CHECKBOX = (By.XPATH, '//input[@type="checkbox" and @name="agree"]')

    LOCATOR_SUCCESSFUL_REGISTRATION = (By.XPATH, '//h1[contains(text(), "Ваша учетная запись создана!")]')


class OpenCartProductLocators:
    LOCATOR_OPENCART_BUY_BUTTONS = (By.XPATH, '//span[contains(text(), "Купить")]/ancestor::button')
