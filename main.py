from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

un=os.environ.get("un")
ps=os.environ.get("ps")
DRIVER_PATH=os.environ.get("DRIVER_PATH")

FROM_TIME="8:00 PM"
TO_TIME="8:00 PM"
REASON="Because I am testing the gatepass application script today TOO"
class Gatepass():

    def __init__(self):
        # self.service=webdriver.EdgeService()
        # self.options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge()

    def login(self):

        self.driver.get("https://punjab.chitkara.edu.in//Interface/index.php")

        self.driver.find_element(By.ID,'username').send_keys(un)

        self.driver.find_element(By.ID,"password").send_keys(ps)

        # enter key
        self.driver.find_element(By.ID,"password").send_keys(Keys.ENTER)
        
    def apply_gatepass(self):
        self.driver.get("https://punjab.chitkara.edu.in//Interface/Student/studentGatePass.php")
        time.sleep(4)

        self.driver.find_element(By.ID,"leaveType1").click()
        time.sleep(2)
        
        self.driver.find_element(By.ID,"checkoutTime").send_keys(FROM_TIME)
        time.sleep(2)

        self.driver.find_element(By.ID,"checkinTime").send_keys(TO_TIME)
        time.sleep(2)

        self.driver.find_element(By.ID,"reason").send_keys(REASON)
        time.sleep(2)

        self.driver.find_element(By.ID,"applyGatePass").click()
        time.sleep(2)

        alert=self.driver.switch_to.alert
        alert.accept()
        alert.accept()
        time.sleep(5)
        # handle calender

    
bot=Gatepass()
bot.login()
bot.apply_gatepass()

