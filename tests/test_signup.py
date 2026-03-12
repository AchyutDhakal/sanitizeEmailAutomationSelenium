from utils.testRunner import create_driver
from pages.signup_page import SignupPage
import pytest
from data.test_data import VALID_SIGNUP
import allure
from utils.otp_reader import get_otp_from_email
import time
from utils.assertions import assert_true

class TestSignup():
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://sanitizeemail.com/")

        self.signup_page = SignupPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("valid_data", VALID_SIGNUP)
    @allure.title("Test of signup using valid data:")
    def test_signup(self, valid_data):
        with allure.step("Click signup link"):
            self.signup_page.click_signup_link()
        
        with allure.step("Fillup signup form"):
            self.signup_page.enter_name(valid_data["name"])
            self.signup_page.enter_email(valid_data["email"])
            self.signup_page.enter_password(valid_data["password"])
            self.signup_page.click_pivacy_policy()
        
        with allure.step("click signup button"):
            self.signup_page.click_signup_button()

        with allure.step("Read otp from gmail and enter otp"):
            time.sleep(20)
            self.signup_page.enter_text(self.signup_page.OTP_INPUT,get_otp_from_email())
            self.signup_page.click_element(self.signup_page.VERIFY_OTP_BUTTON)

        with allure.step("Assertion"):
            assert_true(self.signup_page.is_element_visible(self.signup_page.PROFILE_ICON),"Signup failed as the profile icon is not visible","signup", self.signup_page)

