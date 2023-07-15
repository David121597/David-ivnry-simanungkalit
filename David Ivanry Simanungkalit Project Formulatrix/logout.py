import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_logout(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/index.html") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[1]/input").send_keys("davidsimanungkalit") # isi username
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form/div[2]/input").send_keys("davidsimanungkalit") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/nav/div[1]/ul/li[6]/a").click()
        time.sleep(3)

        # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, "https://www.demoblaze.com/index.html")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()