from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
from dotenv import load_dotenv

load_dotenv()

un=os.environ.get("un")
ps=os.environ.get("ps")

FROM_TIME="8:00 PM"
TO_TIME="8:00 PM"
REASON="Because I am testing the gatepass application script today too"
class Gatepass():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):

        self.driver.get("https://punjab.chitkara.edu.in//Interface/index.php")

        self.driver.find_element(By.ID,'username').send_keys(un)

        time.sleep(2)
        self.driver.find_element(By.ID,"password").send_keys(ps)

        select=Select(self.driver.find_element(By.ID,'instituteId'))

        time.sleep(2)
        select.select_by_visible_text('CUIET')
        time.sleep(2)
        # enter key
        self.driver.find_element(By.ID,"password").send_keys(Keys.ENTER)
        
    def apply_gatepass(self):
        self.driver.get("https://punjab.chitkara.edu.in//Interface/Student/studentGatePass.php")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/a').click()
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

    
bot=Gatepass()
bot.login()
time.sleep(2)
bot.apply_gatepass()

