import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge5(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge5(self):
        # Go to copart.com and search for "porsche"
        self.driver.get("https://www.copart.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "input-search")))
        self.driver.find_element(By.ID, "input-search").send_keys("porsche")
        self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)

        # Once the search page is loaded, select 100 from the dropdown menu
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "serverSideDataTable_length")))
        dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
        dropdown.find_element(By.XPATH, "//option[. = '100']").click()
        time.sleep(3)

        # Run through each entry and count based on Model
        rows = self.driver.find_elements_by_xpath("//*[@data-uname=\"lotsearchLotmodel\"]")
        model_dict = dict()
        for row in rows:
            if row.text != '':
                if row.text in model_dict:
                    model_dict[row.text] += 1
                else:
                    model_dict[row.text] = 1

        # Print the results from the dictionary
        print("MODEL:")
        for model in model_dict:
            print(model, model_dict[model])

        # Break between segments of the test
        print()
        print("* * * * * * * * * *")
        print()

        # Run through each entry and count based on Damage
        rows = self.driver.find_elements_by_xpath("//*[@data-uname=\"lotsearchLotdamagedescription\"]")
        damage_dict = {
            "REAR END": 0,
            "FRONT END": 0,
            "MINOR DENT/SCRATCHES": 0,
            "UNDERCARRIAGE": 0,
            "MISC": 0
        }
        for row in rows:
            if row.text in damage_dict:
                damage_dict[row.text] += 1
            else:
                damage_dict["MISC"] += 1

        # Print the results from the dictionary
        print("DAMAGE:")
        for damage in damage_dict:
            print(damage, damage_dict[damage])


    if __name__ == '__main__':
        unittest.main()
