import time

from src.service.OpenCartHelpers import AccountHelper


class TestRegistration:
    def test_registration_user(self, browser, fake_data):
        acc = AccountHelper(browser)
        acc.go_to_shop()
        acc.open_register_page()
        time.sleep(10)
        password = fake_data.password()
        acc.help_register(
            name=fake_data.name(),
            surname=fake_data.last_name(),
            email=fake_data.email(),
            phone=fake_data.phone_number(),
            password=password,
            confirm_pass=password)
        time.sleep(5)

        assert acc.check_successful_registration()

