def number_reader(number):
    length = str(number).__len__()
    if str(number) == "0":
        return "zero"
    elif length == 1:
        answer = number_translator(str(number)[0], "digits")
        return answer
    elif length == 2 and str(number)[0] == "1":
        answer = number_translator(str(number), "teens")
        return answer
    elif length == 2:
        answer = number_translator(str(number)[0], "tens") + " " \
                 + number_translator(str(number)[1], "digits")
        return answer
    elif length == 3 and str(number)[1] == "1":
        answer = number_translator(str(number)[0], "hundreds") + " " \
                 + number_translator((str(number)[1] + str(number)[2]), "teens")
        return answer
    elif length == 3:
        answer = number_translator(str(number)[0], "hundreds") + " " \
                 + number_translator(str(number)[1], "tens") + " " \
                 + number_translator(str(number)[2], "digits")
        return answer
    elif length == 4 and str(number)[2] == "1":
        answer = number_translator(str(number)[0], "thousands") + " " \
                 + number_translator(str(number)[1], "hundreds") + " " \
                 + number_translator((str(number)[2] + str(number)[3]), "teens")
        return answer
    elif length == 4:
        answer = number_translator(str(number)[0], "thousands") + " " \
                 + number_translator(str(number)[1], "hundreds") + " " \
                 + number_translator(str(number)[2], "tens") + " " \
                 + number_translator(str(number)[3], "digits")
        return answer


def number_translator(number, place):
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
            return number_translator(number, "digits") + " hundred"
    elif place == "thousands":
        if number == "0":
            return ""
        else:
            return number_translator(number, "digits") + " thousand"