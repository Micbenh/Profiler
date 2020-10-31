from selenium import webdriver
import time
from person_creator import Person
from email_creator import Email
from utils import password_generator

class Facebooksignup:
    def __init__(self):
        pass

    def sign_up(self):
        webdriver_path = r"C:\Users\t-mibenh\Downloads\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(webdriver_path)
        driver.get("https://www.facebook.com/r.php")

        user = Person()
        user.scrape_person_information()
        
        driver.find_element_by_name('firstname').send_keys(user.Fname)
        time.sleep(1)
        driver.find_element_by_name('lastname').send_keys(user.Lname)
        time.sleep(1)
        email = Email(user.Fname + " " + user.Lname, user.Username)
        email.sign_up()
        driver.find_element_by_name('reg_email__').send_keys(email.email)
        time.sleep(1)
        driver.find_element_by_name('reg_email_confirmation__').send_keys(email.email)
        time.sleep(1)
        password = password_generator()
        driver.find_element_by_name('reg_passwd__').send_keys(password)
        time.sleep(1)
        driver.find_element_by_name('birthday_month').send_keys(user.Birthday.split(" ")[0])
        time.sleep(1)
        driver.find_element_by_name('birthday_day').send_keys(user.Birthday.split(" ")[1][:-1])
        time.sleep(1)
        driver.find_element_by_name('birthday_year').send_keys(user.Birthday.split(" ")[2])
        time.sleep(1)
        driver.find_element_by_css_selector("input[type='radio'][value='2']").click()        
        time.sleep(1)
        driver.find_element_by_name('websubmit').click()
        time.sleep(15)
        print()
        print("Email: ", email.email)
        print("Email Password: ", email.password)
        print("---------------------------")
        print("Username: ", user.Fname)
        print("Password: ", password)


class Twittersignup():
    def __init__(self):
        pass

    def sign_up(self):
        webdriver_path = r""
        driver = webdriver.Chrome(webdriver_path)
        driver.get(r"https://twitter.com/i/flow/signup")
        user = Person()
        user.scrape_person_information()
        password = password_generator()

        time.sleep(1)
        driver.find_element_by_name("name").send_keys(user.Username)
        time.sleep(0.5)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span").click()
        time.sleep(0.5)
        email = Email(user.Fname + " " + user.Lname, user.Username)
        email.temp_mail()
        driver.find_element_by_name("email").send_keys(email.email)
        time.sleep(0.5)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[1]/div[2]/select").send_keys(user.Birthday.split(" ")[0])
        time.sleep(0.5)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[2]/div[2]/select").send_keys(user.Birthday.split(" ")[1][:-1])
        time.sleep(0.5)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[3]/div[2]/select").send_keys(user.Birthday.split(" ")[2])
        time.sleep(0.5)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath(r"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div").click()
        time.sleep(10)
        print("Email: ", email.email)
        print("Email Password: ", email.password)



        #after email creator class is ready, add a driver to open email and verify code

if __name__ == "__main__":
    #test = Facebooksignup()
    #test.sign_up()
    twitsign = Twittersignup()
    twitsign.sign_up()
    time.sleep(180)


