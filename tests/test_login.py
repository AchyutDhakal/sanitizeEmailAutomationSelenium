from utils.testRunner import create_driver
from pages.loginPage import LoginPage
from data.test_data import VALID_LOGIN_DATA
import pytest
import time
from utils.assertions import assert_true
import allure

class TestLogin():
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://sanitizeemail.com/")

        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("valid_data",VALID_LOGIN_DATA)
    def test_valid_login(self,valid_data):
        with allure.step("Click login link"):
            self.login_page.click_login_link()

        with allure.step("Fillup login form"):
            self.login_page.enter_email(valid_data["email"])
            self.login_page.enter_password(valid_data["password"])

        with allure.step("Click login button"):    
            self.login_page.click_login_button()

        with allure.step("Assertion"):
            self.login_page.click_profile_icon()
            assert_true(self.login_page.is_element_clickable(self.login_page.LOGOUT_BUTTON),"Login failed as the logout button is not clickable","login", self.login_page)


