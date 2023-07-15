import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
        
def login_(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.demoblaze.com/index.html") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/nav/div[1]/ul/li[5]/a").click() # klik login
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[1]/input").send_keys("davidsimanungkalit") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[1]/input").send_keys("davidsimanungkalit") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click() # klik tombol login
        time.sleep(3)
        