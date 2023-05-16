"""Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classStack import Stack
from random import randint

stack = Stack()
stack_aux = Stack()

for i in range(100):
    value = randint(0, 10)
    stack.push(value)

result = []

while stack.size() > 0:
    value = stack.pop()
    if (value % 2 == 0):
        stack_aux.push(value)
        result.append(value)

while stack_aux.size() > 0:
    stack.push(stack_aux.pop())

print(result)