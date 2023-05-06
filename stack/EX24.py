"""Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G"""

from stack import Stack

stack = Stack()

characters = [
    {
        "name": "Iron Man",
        "movies": ["Iron Man", "Iron Man 2", "The Avengers", "Iron Man 3"]
    },
    {
        "name": "Captain America",
        "movies": ["Captain America: The First Avenger", "The Avengers", "Captain America: The Winter Soldier", "Avengers: Age of Ultron", "Captain America: Civil War"]
    },
    {
        "name": "Thor",
        "movies": ["Thor", "The Avengers", "Thor: The Dark World", "Avengers: Age of Ultron", "Thor: Ragnarok"]
    },
    {
        "name": "Hulk",
        "movies": ["The Incredible Hulk", "The Avengers", "Avengers: Age of Ultron"]
    },
    {
        "name": "Black Widow",
        "movies": ["Iron Man 2", "The Avengers", "Captain America: The Winter Soldier", "Avengers: Age of Ultron", "Captain America: Civil War", "Black Widow"]
    },
    {
        "name": "Hawkeye",
        "movies": ["Thor", "The Avengers", "Avengers: Age of Ultron", "Captain America: Civil War"]
    },
    {
        "name": "Rocket Raccoon",
        "movies": ["Guardians of the Galaxy", "Guardians of the Galaxy Vol. 2", "Avengers: Infinity War", "Avengers: Endgame", "Guardians of the Galaxy Vol. 3"]
    },
    {
        "name": "Groot",
        "movies": ["Guardians of the Galaxy", "Guardians of the Galaxy Vol. 2", "Avengers: Infinity War", "Avengers: Endgame", "Guardians of the Galaxy Vol. 3"]
    },
    {
        "name": "Doctor Strange",
        "movies": ["Doctor Strange", "Thor: Ragnarok", "Avengers: Infinity War", "Avengers: Endgame"]
    }
]

def fillStack():
    for i in characters:
        stack.push(i)

# A

fillStack()
counter = 0

while stack.size() > 0:
    character = stack.pop()

    counter += 1

    if (character["name"] == "Rocket Raccoon"):
        print(f"Rocket Raccoon se encuentra en la posición {counter}")

fillStack()
counter = 0

while stack.size() > 0:
    character = stack.pop()

    counter += 1

    if (character["name"] == "Groot"):
        print(f"Groot se encuentra en la posición {counter}")

# B

fillStack()
while stack.size() > 0:
    character = stack.pop()
    
    name = character["name"]
    movies = len(character["movies"])

    if (len(character["movies"]) > 5):
        print(f"{name} apareció en {movies} películas")

# C

fillStack()
while stack.size() > 0:
    character = stack.pop()

    movies = len(character["movies"])

    if (character["name"] == "Black Widow"):
        print(f"Black Widow participó en {movies} películas")

# D

fillStack()
while stack.size() > 0:
    character = stack.pop()

    firstLetter = character["name"][0:1]

    if (firstLetter == "C" or firstLetter == "D" or firstLetter == "G"):
        print(character["name"])