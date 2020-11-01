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

    def gmail_creator(self):
        webdriver_path = r""
        driver = webdriver.Chrome(webdriver_path)
        user = Person()
        user.scrape_person_information()
        password = password_generator()
        driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=en&dsh=S-721270947%3A1604150653782696&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
        time.sleep(2)
        driver.find_element_by_name("firstName").send_keys(user.Fname)
        time.sleep(1)
        driver.find_element_by_name("lastName").send_keys(user.Lname)
        time.sleep(1)
        driver.find_element_by_name("Username").send_keys(user.Username + "999")
        time.sleep(1)
        driver.find_element_by_name("Passwd").send_keys(password)
        time.sleep(1)
        driver.find_element_by_name("ConfirmPasswd").send_keys(password)
        time.sleep(1.5)
        driver.find_element_by_xpath("//*[@id='accountDetailsNext']").click()
        time.sleep(5)
        #stuck with phone verification

    def protonmail_generator(self):
        webdriver_path = r""
        driver = webdriver.Chrome(webdriver_path)
        driver.get("https://mail.protonmail.com/create/new?language=en")
        user = Person()
        user.scrape_person_information()
        time.sleep(10)
        driver.find_element_by_class_name("input").send_keys(user.Username)
        time.sleep(5)
        #stuck with username input


    def temp_mail(self):
        webdriver_path = r""
        driver = webdriver.Chrome(webdriver_path)
        driver.get("https://temp-mail.org/en/")
        user = Person()
        user.scrape_person_information()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='click-to-change']").click()
        time.sleep(1)
        driver.find_element_by_name("new_mail").send_keys(user.Username)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='postbut']").click()
        time.sleep(0.5)
        self.email = user.Username + "@adeata.com"       

    def temp_mail_verificaiton(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
        URL = "https://temp-mail.org/en/"
        req = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(req, "html.parser")
        mail = soup.find("div", {"class":"user-data-subject"})

        print(mail)

if __name__ == "__main__":
    tets = Email()
    tets.temp_mail_verificaiton()

