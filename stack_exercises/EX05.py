"""Determinar si una cadena de caracteres es un palíndromo"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classStack import Stack

stack = Stack()
stack1 = Stack()
stack2 = Stack()

word = input("Ingrese una palabra: ")

for i in word:
    stack.push(i.lower())
    
while stack.size() > 0:
    value = stack.pop()
    stack1.push(value)
    stack2.push(value)

while stack2.size() > 0:
    stack.push(stack2.pop())
    
if (stack == stack1):
    print("Es palíndromo")
else:
    print("No es palíndromo")