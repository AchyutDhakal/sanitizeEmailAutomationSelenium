from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import allure
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        element.locator.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
        
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        try:
            self.find_visible_element(locator)
            return True
        except TimeoutException:
            return False
        
    def take_screenshot(self, name):
        screenshot_dir = "Screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = time.time()
        file_name = f"{screenshot_dir}/{name}_{timestamp}.png"

        self.driver.save_screenshot(file_name)

        allure.attach.file(
            file_name,
            name=name,
            attachment_type = allure.attachment_type.PNG
        )
