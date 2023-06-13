'''Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente'''

def potencia(base, exponent):

    if exponent != 0:
        return base * potencia(base, exponent - 1)
    else:
        return 1

print(potencia(2,5))