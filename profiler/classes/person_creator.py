from bs4 import BeautifulSoup as BeautifulSoup
import requests

class Person():
    def __init__(self):
        self.Fname = None
        self.Lname = None
        self.Sex = None
        self.Address = None
        self.Birthday = None
        self.Age = None
        self.Username = None
        self.Password = "asfsafasfasfasf152151251AAAFAFSA@"
        self.Favorite_Color = None


    def scrape_person_information(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
        URL = "https://www.fakenamegenerator.com/advanced.php?t=country&n%5B%5D=ir&c%5B%5D=us&gen=&age-min=&age-max="
        req = requests.get(URL, headers = headers).text
        soup = BeautifulSoup(req, 'html.parser')
        Name = soup.find("div", {"class":"address"}).find("h3").text
        self.Fname = Name.split(" ")[:-2][0]
        self.Lname =  " ".join(Name.split(" ")[-2:])
        self.Address = soup.find("div", {"class":"adr"}).text.lstrip()
        self.Birthday = soup.find("div", {"class":"extra"}).findAll("dd")[5].text
        self.Age = soup.find("div", {"class":"extra"}).findAll("dd")[6].text.split(" ")[0]
        self.Username= soup.find("div", {"class":"extra"}).findAll("dd")[9].text
        self.Favorite_Color = soup.find("div", {"class":"extra"}).findAll("dd")[24].text


if __name__ == "__main__":
    person = Person()
    person.scrape_person_information()
    print(person.Fname)
    print(person.Lname)
    print(person.Address)
    print(person.Birthday)
    print(person.Birthday.split(" ")[1])
    print(person.Age)
    print(person.Username)
    print(person.Password)
    print(person.Favorite_Color)




    