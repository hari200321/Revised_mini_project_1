"""main.py"""

#Importing necessary modules
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Common import Data


#importing exception handling modules to handle error gracefully
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

#importing Explicit wait modules
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators: # which contains all locators to automate the Guvi website
    Login_button_locator = "login-btn"
    Signup_button_locator = "//a[@class='⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']"
    Username_locator = "email"
    Password_locator = "password"
    Submit_locator = "login-btn"

class Automation(Data, Locators):  # this is as Automation class which inherits the Data and Locators Class here ive used OOPs concepts!

    def __init__(self): # its a constructor.
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20) #here im using Explicit wait to automate the webpage
        self.actions = ActionChains(self.driver) # im using Action chains to insert the data into webpage and do some actions in it

    def start(self): #start method contains get the URL

        try:
            self.driver.maximize_window()
            self.driver.get(self.URL)
            return f"{self.URL} is valid"

        except TimeoutException as error:
            return False

    def webpage_title(self): # webpage_title method contains title of the url

        try:
            if self.start():
                return self.driver.title

        except TimeoutException as error:
            return False

    def is_login_button_visible(self): # here im trying to check whether the login button is visible or not in webpage

        try:
            login_locator = self.wait.until(EC.visibility_of_element_located((By.ID, self.Login_button_locator)))
            return 'Login locator is Visible'

        except (NoSuchElementException, ElementNotVisibleException) as error:
            return  error

    def is_login_button_clickable(self):  # here im trying to check whether the login button ios clickable or not!

        try:
            login_locator = self.wait.until(EC.element_to_be_clickable((By.ID, self.Login_button_locator)))
            return 'Login button is clickable'

        except (TimeoutException, NoSuchElementException) as error:
            return error

    def is_signup_button_visible(self): # in this method im trying to check whether signup button is visible or not !

        try:
            signup_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Signup_button_locator)))
            return 'signup button is visible'

        except (NoSuchElementException, TimeoutException) as error:
            return error

    def is_signup_button_clickable(self):  # in this method im trying to check whether the signup button is clickable or not.

        try:
            signup_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Signup_button_locator)))
            signup_locator.click()


        except (NoSuchElementException, TimeoutException) as error:
            return error

    def go_backward(self): # in this method i need to go backward to proceed further !

        self.driver.back()


    def guvi_login(self): #in this method im trying to login with my user credentials by using BY and action chains builtin method!

        try:

            self.driver.find_element(by=By.ID, value = self.Login_button_locator).click()
            self.driver.find_element(by=By.ID, value=self.Username_locator).send_keys(self.USERNAME)
            self.driver.find_element(by=By.ID, value=self.Password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.ID, value=self.Submit_locator).click()


        except NoSuchElementException as error:
            return error


    def quit(self): # this method will quit the session once automation is done.
        self.driver.quit()

#main execution program
if __name__ == "__main__":

    hari = Automation()
    print(hari.start())
    print(hari.webpage_title())
    print(hari.is_login_button_visible())
    print(hari.is_login_button_clickable())
    print(hari.is_signup_button_visible())
    hari.is_signup_button_clickable()
    hari.go_backward()
    hari.guvi_login()