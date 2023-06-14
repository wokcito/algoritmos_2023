import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classList import List
from classQueue import Queue

class Hero():
    def __init__(self, supername, name, group, year):
        self.supername = supername
        self.name = name
        self.group = group
        self.year = year

    def __str__(self) -> str:
        return f"{self.supername} | {self.name} | {self.group} | {self.year}"

heroesList = List("supername")

characters = [
    {"supername": "Captain Marvel", "name": "Carol Danvers", "group": "Avengers", "year": 2012},
    {"supername": "Star-Lord", "name": "Peter Quill", "group": "Guardians of the Galaxy", "year": 2014},
    {"supername": "Gamora", "name": "Gamora", "group": "Guardians of the Galaxy", "year": 2014},
    {"supername": "Drax the Destroyer", "name": "Drax", "group": "Guardians of the Galaxy", "year": 2014},
    {"supername": "Rocket Raccoon", "name": "Rocket", "group": "Guardians of the Galaxy", "year": 2014},
    {"supername": "Groot", "name": "Groot", "group": "Guardians of the Galaxy", "year": 2014},
    {"supername": "Mr. Fantastic", "name": "Reed Richards", "group": "Fantastic Four", "year": 1961},
    {"supername": "Invisible Woman", "name": "Sue Storm", "group": "Fantastic Four", "year": 1961},
    {"supername": "Human Torch", "name": "Johnny Storm", "group": "Fantastic Four", "year": 1961},
    {"supername": "The Thing", "name": "Ben Grimm", "group": "Fantastic Four", "year": 1961},
    {"supername": "Vlanck Widow", "name": "Natasha Romanoff", "group": "Avengers", "year": 2010},
    {"supername": "Iron Man", "name": "Tony Stark", "group": "Avengers", "year": 1963},
    {"supername": "Thor", "name": "Thor Odinson", "group": "Avengers", "year": 1962},
    {"supername": "Hawkeye", "name": "Clint Barton", "group": "Avengers", "year": 1964},
    {"supername": "Black Panther", "name": "TChalla", "group": "Avengers", "year": 1966},
    {"supername": "Scarlet Witch", "name": "Wanda Maximoff", "group": "Avengers", "year": 1964},
    {"supername": "Doctor Strange", "name": "Stephen Strange", "group": None, "year": 1963},
    {"supername": "Ant-Man", "name": "Scott Lang", "group": "Avengers", "year": 1962}
]

additionalCharacters = [
    {"supername": "Black Cat", "name": "Felicia Hardy", "group": None, "year": 1979},
    {"supername": "Hulk", "name": "Bruce Banner", "group": "Avengers", "year": 1962},
    {"supername": "Loki", "name": "Loki Laufeyson", "group": "Avengers", "year": 1962}
]

for data in characters:
    hero = Hero(data["supername"], data["name"], data["group"], data["year"])
    heroesList.insert(hero)

# a
print("\na)")

def searchHero(name):
    heroIndex = heroesList.search(name)
    if (heroIndex != None):
        return heroesList.getByIndex(heroIndex)

print(searchHero("Captain Marvel"))

# b
print("\nb)")

queueGOTG = Queue()
counter = 0

while (counter < heroesList.size()):
    heroFound = heroesList.getByIndex(counter)

    if (heroFound == None):
        break

    if (heroFound.group == "Guardians of the Galaxy"):
        queueGOTG.arrive(heroFound)

    counter += 1

print(queueGOTG.size())

# c
print("\nc)")

listGOTG = List("supername")
listFF = List("supername")

counter = 0

while (counter < heroesList.size()):
    heroFound = heroesList.getByIndex(counter)

    if (heroFound == None):
        break

    if (heroFound.group == "Guardians of the Galaxy"):
        listGOTG.insert(heroFound)
    elif (heroFound.group == "Fantastic Four"):
        listFF.insert(heroFound)

    counter += 1

listGOTG.iteration()
listFF.iteration()

# d
print("\nd)")

counter = 0

while (counter < heroesList.size()):
    heroFound = heroesList.getByIndex(counter)

    if (heroFound == None):
        break

    if (heroFound.year > 1960):
        print(heroFound)

    counter += 1

# e
print("\ne)")

heroesList.set("Vlanck Widow", Hero("Black Widow", "Natasha Romanoff", "Avengers", 2010))

# f
print("\nf)")

for data in additionalCharacters:
    hero = Hero(data["supername"], data["name"], data["group"], data["year"])
    heroesList.insert(hero)

# g
print("\ng)")

counter = 0

while (counter < heroesList.size()):
    heroFound = heroesList.getByIndex(counter)

    if (heroFound == None):
        break

    firstLetter = heroFound.supername[0].lower()

    if (firstLetter == "c"):
        print(heroFound)
    elif (firstLetter == "p"):
        print(heroFound)
    elif (firstLetter == "s"):
        print(heroFound)

    counter += 1