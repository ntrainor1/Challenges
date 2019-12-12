import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge6(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge6(self):
        # Go to copart.com and search for "porsche"
        self.driver.get("https://www.copart.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "input-search")))
        self.driver.find_element(By.ID, "input-search").send_keys("porsche")
        self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)

        # Once the search page is loaded, select 100 from the dropdown menu
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "serverSideDataTable_length")))
        dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
        dropdown.find_element(By.XPATH, "//option[. = '100']").click()


    if __name__ == '__main__':
        unittest.main()
