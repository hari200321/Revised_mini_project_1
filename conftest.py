"""conftest.py"""



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver(self):
   self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   self.driver.maximize_window()
   yield driver
   self.driver.quit()
