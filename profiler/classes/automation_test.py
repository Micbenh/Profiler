from selenium import webdriver
import time

class Facebooksignup:
    def __init__(self, first_name , last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def sign_up(self):
        """ A function that auto-fills the facebook sign up form
        using information from the 'PersonCreator' class """
        webdriver_path = r""
        driver = webdriver.Chrome(webdriver_path)
        driver.get("https://www.facebook.com/r.php")
        driver.find_element_by_name('firstname').send_keys(self.first_name)
        time.sleep(2)
        driver.find_element_by_name('lastname').send_keys(self.last_name)
        time.sleep(2)
        driver.find_element_by_name('reg_email__').send_keys(self.email)
        time.sleep(2)
        driver.find_element_by_name('reg_email_confirmation__').send_keys(self.email)
        time.sleep(2)
        driver.find_element_by_name('reg_passwd__').send_keys(self.password)
        time.sleep(2)
        driver.find_element_by_name('birthday_month').send_keys('Jul')
        time.sleep(2)
        driver.find_element_by_name('birthday_day').send_keys('25')
        time.sleep(2)
        driver.find_element_by_name('birthday_year').send_keys('1990')
        time.sleep(2)
        driver.find_element_by_css_selector("input[type='radio'][value='2']").click()        
        time.sleep(2)
        driver.find_element_by_name('websubmit').click()
        time.sleep(60)








if __name__ == "__main__":
    test = Facebooksignup("Daniel","Ben-Shalom", "micbenh@outlook.com", str(1125125)+"asfaf2325!@")
    test.sign_up()

