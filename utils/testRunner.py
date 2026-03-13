from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.page_load_strategy = "eager"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver