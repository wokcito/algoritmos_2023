'''Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.'''

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classList import List

heroesList = List("name")

class Hero():
    def __init__(self, name, year, comicHouse, biography):
        self.name = name
        self.year = year
        self.comicHouse = comicHouse
        self.biography = biography

    def __str__(self) -> str:
        return f"{self.year} | {self.name} | {self.comicHouse} \n {self.biography} \n"

superheroes = [
  {
    "name": "Green Lantern",
    "year": 1940,
    "comicHouse": "DC",
    "biography": "Linterna Verde, también conocido como Hal Jordan..."
  },
  {
    "name": "Wolverine",
    "year": 1974,
    "comicHouse": "Marvel",
    "biography": "Wolverine, también conocido como Logan, es un mutante con garras retráctiles, sentidos agudizados y un factor de curación. Su pasado está envuelto en misterio, pero es conocido por su actitud hosca y su disposición para hacer lo que sea necesario para proteger a los mutantes y a sus aliados."
  },
  {
    "name": "Doctor Strange",
    "year": 1963,
    "comicHouse": "Marvel",
    "biography": "Doctor Strange, también conocido como Stephen Strange, es un antiguo cirujano convertido en el Hechicero Supremo. Posee habilidades místicas y es capaz de manipular la realidad, viajar en el tiempo y lanzar hechizos poderosos. Utiliza su conocimiento de las artes místicas para proteger al mundo de amenazas sobrenaturales."
  },
  {
    "name": "Captain Marvel",
    "year": 1967,
    "comicHouse": "Marvel",
    "biography": "Capitana Marvel, también conocida como Carol Danvers, es una ex piloto de la Fuerza Aérea de los Estados Unidos. Obtuvo sus poderes cuando fue expuesta a la tecnología alienígena y se convirtió en una híbrida humana-Kree. Posee fuerza sobrehumana, vuelo y la capacidad de generar energía cósmica. Capitana Marvel defiende la Tierra de amenazas extraterrestres y lucha por la justicia."
  },
  {
    "name": "Wonder Woman",
    "year": 1941,
    "comicHouse": "DC",
    "biography": "Mujer Maravilla, también conocida como Diana Prince, es una princesa guerrera amazona. Posee fuerza sobrehumana, agilidad y la capacidad de volar. Mujer Maravilla lucha por la justicia, el amor y la paz en un mundo lleno de conflictos."
  },
  {
    "name": "Flash",
    "year": 1940,
    "comicHouse": "DC",
    "biography": "Flash, también conocido como Barry Allen, es un velocista sobrehumano. Puede correr a velocidades increíbles y atravesar el tiempo. Utiliza sus habilidades para proteger Central City y mantener la paz. El traje de Flash está diseñado para soportar sus velocidades extremas y protegerlo mientras corre a través del espacio-tiempo."
  },
  {
    "name": "Star-Lord",
    "year": 1976,
    "comicHouse": "Marvel",
    "biography": "Star-Lord, también conocido como Peter Quill, es un aventurero espacial y líder de los Guardianes de la Galaxia. Posee habilidades de combate, manejo de armas y utiliza un traje especial con una armadura avanzada. Star-Lord viaja por el cosmos protegiendo a la galaxia de amenazas intergalácticas."
  }
]

for data in superheroes:
    hero = Hero(data["name"], data["year"], data["comicHouse"], data["biography"])
    heroesList.insert(hero)

# A
heroesList.delete("Green Lantern")

# B
print(heroesList.getByValue("Wolverine").year)

# C
heroesList.getByValue("Doctor Strange").comicHouse = "DC"

# D
counter = 0

while counter != heroesList.size():
    biography = heroesList.getByIndex(counter).biography
    
    if ("traje" in biography or "armadura" in biography):
        print(biography)
        break

    counter += 1

# E
heroesList.orderBy("year")
print(heroesList.getByIndex(heroesList.search(1963, "year")).name)

# F
heroesList.orderBy()
print(heroesList.getByIndex(heroesList.search("Captain Marvel")).comicHouse)
print(heroesList.getByIndex(heroesList.search("Wonder Woman")).comicHouse)

# G
print(heroesList.getByValue("Star-Lord"))
print(heroesList.getByValue("Flash"))

# H
counter = 0

while counter != heroesList.size():
    heroName = heroesList.getByIndex(counter).name

    firstLetter = heroName[0].lower()

    if (firstLetter == "b" or firstLetter == "m" or firstLetter == "s"):
        print(heroName)

    counter += 1

# I

counter = 0

marvel = 0
dc = 0

while counter != heroesList.size():
    comicHouse = heroesList.getByIndex(counter).comicHouse.lower()

    if (comicHouse == "dc"):
        dc += 1
    else:
        marvel += 1

    counter += 1

print(f"Superheroes de DC: {dc}")
print(f"Superheroes de Marvel: {marvel}")