'''Implementar una función que calcule la suma de todos los números enteros ocmprendidos entre cero y un número entero positivo dado'''

def suma(number):
    if (number < 0): return "The must be positive"

    if number == 0:
        return 0
    else:
        return number + suma(number - 1)

print(suma(6))