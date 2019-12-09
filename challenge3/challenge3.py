import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge3(self):
        # code for our test steps
        self.driver.get("https://www.copart.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]/div[1]/ul/li[1]")))
        table = self.driver.find_elements_by_xpath("//*[@id=\"tabTrending\"]/div[1]/div[2]")
        # for item in table:
        #     print(str(item.text))
        column_number = 1
        while column_number < 5:
            row_number = 1
            while row_number < 5:
                row = self.driver.find_element_by_xpath("//*[@id=\"tabTrending\"]/div[1]/div[2]/div["+str(column_number)+"]/ul/li["+str(row_number)+"]/a")
                print(str(row.text)+" - "+str(row.get_attribute("href")))
                row_number += 1
            column_number += 1

    if __name__ == '__main__':
        unittest.main()
