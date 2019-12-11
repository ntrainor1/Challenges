import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        # code for our test steps
        fib = Fibonacci()
        print(fib.fib(-1))
        print(fib.fib(0))
        print(fib.fib(1))
        print(fib.fib(2))
        print(fib.fib(3))
        print(fib.fib(4))
        print(fib.fib(5))
        print(fib.fib(6))
        print(fib.fib(7))
        print(fib.fib(8))
        print(fib.fib(9))
        print(fib.fib(10))
        print(fib.fib(11))
        print(fib.fib(12))
        print(fib.fib(13))
        print(fib.fib(14))
        print(fib.fib(15))
        print(fib.fib(16))
        print(fib.fib(17))
        print(fib.fib(18))
        print(fib.fib(19))
        print(fib.fib(20))

    if __name__ == '__main__':
        unittest.main()


class Fibonacci:

    def fib(self, number):
        number_reader = NumberReader()
        if number < 1:
            return "Please enter a positive number"
        elif number == 1:
            return str(0) + " - " + number_reader.number_reader(0)
        elif number == 2:
            return str(1) + " - " + number_reader.number_reader(1)

        counter = 2
        x = 0
        y = 1
        result = 1

        while counter < number:
            result = x + y
            z = y
            y = result
            x = z
            counter += 1

        return str(result) + " - " + number_reader.number_reader(result)


class NumberReader:

    def number_reader(self, number):
        length = str(number).__len__()
        if str(number) == "0":
            return "zero"
        elif length == 1:
            answer = self.number_translator(str(number)[0], "digits")
            return answer
        elif length == 2 and str(number)[0] == "1":
            answer = self.number_translator(str(number), "teens")
            return answer
        elif length == 2:
            answer = self.number_translator(str(number)[0], "tens") + " "\
                     + self.number_translator(str(number)[1], "digits")
            return answer
        elif length == 3 and str(number)[1] == "1":
            answer = self.number_translator(str(number)[0], "hundreds") + " "\
                     + self.number_translator((str(number)[1]+str(number)[2]), "teens")
            return answer
        elif length == 3:
            answer = self.number_translator(str(number)[0], "hundreds") + " "\
                     + self.number_translator(str(number)[1], "tens") + " "\
                     + self.number_translator(str(number)[2], "digits")
            return answer
        elif length == 4 and str(number)[2] == "1":
            answer = self.number_translator(str(number)[0], "thousands") + " "\
                     + self.number_translator(str(number)[1], "hundreds") + " "\
                     + self.number_translator((str(number)[2]+str(number)[3]), "teens")
            return answer
        elif length == 4:
            answer = self.number_translator(str(number)[0], "thousands") + " "\
                     + self.number_translator(str(number)[1], "hundreds") + " "\
                     + self.number_translator(str(number)[2], "tens") + " "\
                     + self.number_translator(str(number)[3], "digits")
            return answer

    def number_translator(self, number, place):
        if place == "digits":
            if number == "1":
                return "one"
            elif number == "2":
                return "two"
            elif number == "3":
                return "three"
            elif number == "4":
                return "four"
            elif number == "5":
                return "five"
            elif number == "6":
                return "six"
            elif number == "7":
                return "seven"
            elif number == "8":
                return "eight"
            elif number == "9":
                return "nine"
            elif number == "0":
                return ""
        elif place == "teens":
            if number == "11":
                return "eleven"
            elif number == "12":
                return "twelve"
            elif number == "13":
                return "thirteen"
            elif number == "14":
                return "fourteen"
            elif number == "15":
                return "fifteen"
            elif number == "16":
                return "sixteen"
            elif number == "17":
                return "seventeen"
            elif number == "18":
                return "eighteen"
            elif number == "19":
                return "nineteen"
            elif number == "10":
                return "ten"
        elif place == "tens":
            if number == "2":
                return "twenty"
            elif number == "3":
                return "thirty"
            elif number == "4":
                return "forty"
            elif number == "5":
                return "fifty"
            elif number == "6":
                return "sixty"
            elif number == "7":
                return "seventy"
            elif number == "8":
                return "eighty"
            elif number == "9":
                return "ninety"
            elif number == "0":
                return ""
        elif place == "hundreds":
            if number == "0":
                return ""
            else:
                return self.number_translator(number, "digits") + " hundred"
        elif place == "thousands":
            if number == "0":
                return ""
            else:
                return self.number_translator(number, "digits") + " thousand"
