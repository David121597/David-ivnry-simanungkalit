import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import login1

class TestAdd(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())



    def test_a_fail_addlist(self):
        driver=self.browser

        #login
        login1.login_(self)
        response_data = driver.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[7]/a").text
        self.assertIn('Welcome davidsimanungkalit', response_data)

        #Steps
        driver.find_element(By.XPATH,"/html/body/nav/div[1]/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[1]/input").send_keys("davidsimanungkalit121597@gmail.com") #email
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[2]/input").send_keys("David Simanungkalit") #countact name
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[3]/textarea").send_keys("Congratulation") #message
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/nav/div[1]/ul/li[2]/a").click()
        time.sleep(3)

        #validasi
        response_data = driver.current_url
        self.assertEqual(response_data, "https://www.demoblaze.com/index.html")




        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()