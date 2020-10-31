from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import time
from person_creator import Person
from utils import password_generator

class Email():
    def __init__(self, name = None, username=None):
        self.email = None
        self.password = None
        self.name = name
        self.username = username
        

    def fast_mail_sign_up(self):
        webdriver_path = r""
        driver = webdriver.Chrome(webdriver_path)
        password = password_generator()
        driver.get("https://www.fastmail.com/signup/")
        time.sleep(3)
        try:
            driver.find_element_by_name("name").send_keys(self.name)
            time.sleep(1)
            driver.find_element_by_name("email-localpart").send_keys(self.username)
            self.email = self.username + "@fastmail.com"
            time.sleep(0.5)
            driver.find_element_by_name("password").send_keys(password)
            self.password = password
            time.sleep(0.5)
            driver.find_element_by_name("tos").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='main-submit']").click()
            time.sleep(6)
        except NoSuchElementException:
            pass

if __name__ == "__main__":
    tets = Email()
    tets.temp_mail()

