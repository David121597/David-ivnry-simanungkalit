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
        driver.find_element(By.XPATH,"/html/body/nav/div/div/ul/li[4]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[4]/a").click()
        time.sleep(3)

        #validasi
        response_data = driver.current_url
        self.assertEqual(response_data, "https://www.demoblaze.com/cart.html#")




        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()