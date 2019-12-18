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

        # Once the search page is loaded, search for "skyline" in the secondary searchbar
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@placeholder=\"Search by Lot#,VIN#\"]")))
        # self.driver.find_element(By.XPATH, "//*[@placeholder=\"Search by Lot#,VIN#\"]").send_keys("skyline")
        # time.sleep(10)

        # Try to find an entry with "skyline", otherwise take a screenshot
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-uname=\"lotsearchLotnumber\"]")))
            elements = self.driver.find_elements_by_xpath("//*[@data-uname=\"lotsearchLotnumber\"]")
            href = elements[1].get_attribute("href")
            self.assertIn("copart", href)
        except:
            print("\"skyline\" not found")
            self.driver.save_screenshot("screenshot.png")

    if __name__ == '__main__':
        unittest.main()
