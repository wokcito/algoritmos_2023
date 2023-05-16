"""Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classStack import Stack
from random import randint

stack = Stack()
stack_aux = Stack()

for i in range(10):
    value = randint(0, 10)
    stack.push(value)

result = []

while stack.size() > 0:
    stack_aux.push(stack.pop())

while stack_aux.size() > 0:
    result.append(stack_aux.pop())

print(result)