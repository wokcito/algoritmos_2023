'''Desarrollar una función que permita convertir un número romano en un número decimal'''

def romano(number):

    number = number.upper()

    numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    operator = False if (len(number) >= 2 and numbers.get(number[-2]) < numbers.get(number[-1])) else True

    if (len(number) == 0):
        return 0
    elif (operator):
        return numbers.get(number[-1]) + romano(number[:-1])
    else:
        return numbers.get(number[-1]) - numbers.get(number[-2]) + romano(number[:-2])

print(romano("MCMXCIX"))