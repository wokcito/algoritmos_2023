'''Desarrollar un algoritmo que permita calcular la siguiente serie: 1/n'''

def serie(number):

    if (number == 1):
        return 1
    else:
        return (1 / number) + serie(number - 1)

print(serie(3))