"""Eliminar de una cola de caracteres todas las vocales que aparecen."""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classQueue import Queue

queue = Queue()

vocals = ["a", "e", "i", "o", "u"]

text = input("Ingrese un texto: ")

for letter in text:
    if (letter != " "):
        queue.arrive(letter.lower())

counter = 0

while counter < queue.size():
    letter = queue.on_front()

    if (letter in vocals):
        queue.atention()
    else:
        print(queue.move_to_end())
        counter += 1