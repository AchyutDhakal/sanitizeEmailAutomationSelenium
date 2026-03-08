from pages.basePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    LOGIN_LINK =(By.XPATH,"//button[normalize-space()='Log In']")
    EMAIL_INPUT =(By.XPATH,"//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    FORGOT_PASSWORD = (By.XPATH,"//a[normalize-space()='Forgot Password?']")
    LOGIN_BUTTON =  (By.XPATH,"//button[normalize-space()='Log In']")
    PROFILE_ICON =(By.XPATH,"//span[@class='flex size-full items-center justify-center rounded-full bg-global-primary text-white']")
    LOGOUT_BUTTON = (By.XPATH,"//span[normalize-space()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)

    def enter_email(self, email):
        self.enter_text( self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_profile_icon(self):
        self.click_element(self.PROFILE_ICON)

