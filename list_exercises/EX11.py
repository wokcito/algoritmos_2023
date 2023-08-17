"""
Dada una lista que contiene información de los personajes de la saga de Star Wars con la siguiente información nombre, altura, edad, género, especie, planeta natal y episodios en los que apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:

a. listar todos los personajes de género femenino;
b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga;
c. mostrar toda la información de Darth Vader y Han Solo;
d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
"""

from classList import List

charactersList = List("name", "name")

class Character():
    def __init__(self, name, height, age, gender, species, homeworld, episodes):
        self.name = name
        self.height = height
        self.age = age
        self.gender = gender
        self.species = species
        self.homeworld = homeworld
        self.episodes = episodes

    def __str__(self):
        return f"{self.name}:\n  Height: {self.height}\n  Age: {self.age}\n  Gender: {self.gender}\n  Species: {self.species}\n  Homeworld: {self.homeworld}\n"

characters = [
    {
        "name": "Leia Organa",
        "height": "150",
        "age": "53",
        "gender": "Female",
        "species": "Human",
        "homeworld": "Alderaan",
        "episodes": [4, 5, 6, 7, 8, 9]
    },
    {
        "name": "R2-D2",
        "height": "96",
        "age": None,
        "gender": None,
        "species": "Astromech Droid",
        "homeworld": None,
        "episodes": [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    {
        "name": "Darth Vader",
        "height": None,
        "age": None,
        "gender": "Male",
        "species": "Human",
        "homeworld": "Tatooine",
        "episodes": [4, 5, 6]
    },
    {
        "name": "Chewbacca",
        "height": "228",
        "age": None,
        "gender": "Male",
        "species": "Wookiee",
        "homeworld": "Kashyyyk",
        "episodes": [3, 4, 5, 6, 7, 8, 9]
    },
    {
        "name": "Han Solo",
        "height": "180",
        "age": None,
        "gender": "Male",
        "species": "Human",
        "homeworld": "Corellia",
        "episodes": [4, 5, 6, 7]
    },
    {
        "name": "Yoda",
        "height": "66",
        "age": "900",
        "gender": "Male",
        "species": "Yoda's species",
        "homeworld": None,
        "episodes": [2, 3, 5, 6, 8]
    },
    {
        "name": "Maz Kanata",
        "height": "152",
        "age": "1000",
        "gender": "Female",
        "species": None,
        "homeworld": "Takodana",
        "episodes": [7, 8, 9]
    }
]

for data in characters:
    character = Character(data["name"], data["height"], data["age"], data["gender"], data["species"], data["homeworld"], data["episodes"])
    charactersList.insert(character)

charactersList.iteration()