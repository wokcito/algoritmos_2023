"""Determinar el número de ocurrencias de un determinado elemento en una pila"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classStack import Stack
from random import randint

stack = Stack()

value = input("Ingrese un número: ")

for i in range(100):
    value = randint(0, 10)
    stack.push(value)

total = 0

while stack.size() > 0:
    if (stack.pop() == value):
        total += 1

print(f"El valor se encontró {total} veces")