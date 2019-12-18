import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge7(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge7(self):
        # Go to copart.com and retrieve the popular makes and models
        self.driver.get("https://www.copart.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@ng-if=\"popularSearches\"]")))
        table = self.driver.find_elements_by_xpath("//*[@id=\"tabTrending\"]/div[1]/div[2]//a")

        # Put makes and models into a dictionary with model name as the key and href as the value
        model_dict = dict()
        for row in table:
            model_dict[row.text] = row.get_attribute("href")

        for model in model_dict:
            self.driver.get(model_dict[model])
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-uname=\"lotsearchLotmodel\"]")))
            keyword = model[0:4]
            print(keyword)
            print(self.driver.find_element_by_xpath("//*[@data-uname=\"lotsearchLotmodel\"]").text)
            print(self.driver.title)
            try:
                self.assertTrue(keyword.upper() in self.driver.find_element_by_xpath("//*[@data-uname=\"lotsearchLotmodel\"]").text)
            except:
                self.assertTrue(keyword.lower() in self.driver.title)

    if __name__ == '__main__':
        unittest.main()
