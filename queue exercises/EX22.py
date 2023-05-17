"""Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes."""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classQueue import Queue

queue = Queue()

marvel_characters = [
    {"name": "Tony Stark", "superhero_name": "Iron Man", "gender": "M"},
    {"name": "Steve Rogers", "superhero_name": "Captain America", "gender": "M"},
    {"name": "Scott Lang", "superhero_name": "Ant-Man", "gender": "M"},
    {"name": "Carol Danvers", "superhero_name": "Captain Marvel", "gender": "F"},
    {"name": "Natasha Romanoff", "superhero_name": "Black Widow", "gender": "F"},
    {"name": "Wanda Maximoff", "superhero_name": "Scarlet Witch", "gender": "F"},
    {"name": "Peter Parker", "superhero_name": "Spider-Man", "gender": "M"}
]

def fillQueue(): 
    for superhero in marvel_characters:
        queue.arrive(superhero)

# A

fillQueue()

while queue.size() > 0:
    superhero = queue.atention()

    if superhero["superhero_name"] == "Captain Marvel":
        print(superhero["name"])

# B y C

fillQueue()

female = []
male = []

while queue.size() > 0:
    superhero = queue.atention()

    if superhero["gender"] == "F":
        female.append(superhero["name"])
    else:
        male.append(superhero["name"])

print(female)
print(male)

# D

fillQueue()

while queue.size() > 0:
    superhero = queue.atention()

    if superhero["name"] == "Scott Lang":
        print(superhero["superhero_name"])

# E

fillQueue()

while queue.size() > 0:
    superhero = queue.atention()

    if superhero["name"][0].lower() == "s" or superhero["superhero_name"][0].lower() == "s":
        print(superhero)

# F

fillQueue()

while queue.size() > 0:
    superhero = queue.atention()

    if superhero["name"] == "Carol Danvers":
        print(f"Carol Danvers es {superhero['superhero_name']}")