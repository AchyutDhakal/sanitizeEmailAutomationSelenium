from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class SignupPage(BasePage):
    SIGNUP_LINK = (By.XPATH,"//button[normalize-space()='Sign Up']")
    NAME_INPUT = (By.XPATH,"//input[@name='username']")
    EMAIL_INPUT = (By.XPATH,"//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH,"//button[@role='checkbox']")
    SIGNUP_BUTTON = (By.XPATH,"//button[normalize-space()='Sign Up']")
    OTP_INPUT = (By.XPATH,"//input[@autocomplete='one-time-code']")
    VERIFY_OTP_BUTTON = (By.XPATH,"//button[normalize-space()='Verify OTP']")
    PROFILE_ICON =(By.XPATH,"//button[contains(@class,'rounded-full')]")


    def __init__(self, driver):
        super().__init__(driver)

    def click_signup_link(self):
        self.click_element(self.SIGNUP_LINK)

    def enter_name(self,name):
        self.enter_text(self.NAME_INPUT,name)

    def enter_email(self,email):
        self.enter_text(self.EMAIL_INPUT,email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_pivacy_policy(self):
        self.click_element(self.PRIVACY_POLICY_CHECKBOX)

    def click_signup_button(self):
        self.click_element(self.SIGNUP_BUTTON)

