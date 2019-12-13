from common.number_reader import number_reader

def fib(number):
    if number < 1:
        return "Please enter a positive number"
    elif number == 1:
        return str(0) + " - " + number_reader(0)
    elif number == 2:
        return str(1) + " - " + number_reader(1)

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

    return str(result) + " - " + number_reader(result)
