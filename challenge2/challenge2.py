import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge2(self):
        # code for our test steps
        self.driver.get("https://www.copart.com/")
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "input-search")))
        self.driver.find_element(By.ID, "input-search").send_keys("exotic")
        self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(5) > span")))
        assert self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(2) > td:nth-child(5) > span").text == "PORSCHE"

    if __name__ == '__main__':
        unittest.main()
