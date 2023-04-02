'''Leer un vector de N elementos, de a uno por vez. Generar y emitir la sumatoria
de sus componentes de posición par'''

numbers = [0, 1, 2, 3, 4]
total = 0

for num in numbers:
    if ((numbers.index(num) + 1) % 2 == 0): total += num

print(total)