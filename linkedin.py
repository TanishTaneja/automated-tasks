from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
from dotenv import load_dotenv
import os
load_dotenv()

email=os.environ.get("EMAIL")
password=os.environ.get("PASSWORD")

class Apply():

    def __init__(self) -> None:
        self.driver=webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://www.linkedin.com/login')

        self.email_field=self.driver.find_element(by=By.ID,value="username")
        self.email_field.send_keys(email)

        self.password_field=self.driver.find_element(by=By.ID,value="password")
        self.password_field.send_keys(password)
        self.password_field.send_keys(Keys.ENTER)
        time.sleep(2)
    
    def apply(self):
        self.driver.get(
        "https://www.linkedin.com/jobs/search/?currentJobId=3960096036&f_AL=true&geoId=105214831&keywords=python%20developer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
        )
        time.sleep(5)
        
bot=Apply()
bot.login()
bot.apply()


