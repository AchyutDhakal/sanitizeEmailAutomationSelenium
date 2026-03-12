from utils.testRunner import create_driver
from pages.loginPage import LoginPage
from data.test_data import VALID_LOGIN, INVALID_LOGIN
import pytest
import time
from utils.assertions import assert_true, assert_false
import allure

class TestLogin():
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://sanitizeemail.com/")

        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("valid_data",VALID_LOGIN)
    def test_valid_login(self,valid_data):
        with allure.step("Click login link"):
            self.login_page.click_login_link()

        with allure.step("Fillup login form"):
            self.login_page.enter_email(valid_data["email"])
            self.login_page.enter_password(valid_data["password"])

        with allure.step("Click login button"):    
            self.login_page.click_login_button()

        with allure.step("Assertion"):
            assert_true(self.login_page.is_element_visible(self.login_page.PROFILE_ICON),"Login failed as the profile icon is not visible","login", self.login_page)

    @pytest.mark.parametrize("invalid_data",INVALID_LOGIN)
    def test_invalid_login(self,invalid_data):
        with allure.step("Click login link"):
            self.login_page.click_login_link()

        with allure.step("Fillup login form"):
            self.login_page.enter_email(invalid_data["email"])
            self.login_page.enter_password(invalid_data["password"])

        with allure.step("Click login button"):    
            self.login_page.click_login_button()

        with allure.step("Assertion"):
            assert_false(self.login_page.is_element_visible(self.login_page.PROFILE_ICON),"Login failed as the logout button is not clickable","login", self.login_page)


