'''Implementar una función para calcular el producto de dos números enteros dados'''

def producto(number1, number2):
    if (number2 == 0):
        return 0
    else:
        return number1 + producto(number1, number2 - 1)

print(producto(2,2))