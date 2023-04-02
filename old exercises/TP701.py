'''Leer un vector de 100 Números reales, un componente por vez. Emitir la sumatoria
de sus componentes'''

import random

numeros = [random.randint(0, 100) for _ in range(100)]

suma = sum(numeros)

print("La suma nos da:", suma)