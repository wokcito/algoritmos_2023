'''Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero'''

def digitCounter(number):

    number = str(number)

    if (len(number) == 0):
        return 0
    else:
        return 1 + digitCounter(number[:-1])


print(digitCounter(1181802701234870))