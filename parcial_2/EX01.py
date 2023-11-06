"""1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de tipo eléctrico y acero."""

from classBinaryTree import BinaryTree, NodeTree

nameTree = BinaryTree()
pokedexNumberTree = BinaryTree()
typesTree = BinaryTree()

pokemonList = [
    { 'name': 'bulbasaur', 'pokedexNumber': 1, 'types': ['grass', 'poison'] },
    { 'name': 'charmander', 'pokedexNumber': 4, 'types': ['fire']},
    { 'name': 'pidgey', 'pokedexNumber': 16, 'types': ['normal', 'flying']},
    { 'name': 'pikachu', 'pokedexNumber': 25, 'types': ['electric'] },
    { 'name': 'jolteon', 'pokedexNumber': 135, 'types': ['electric'] },
    { 'name': 'lycanroc', 'pokedexNumber': 745, 'types': ['rock'] },
    { 'name': 'tyrantrum', 'pokedexNumber': 697, 'types': ['rock', 'dragon'] }
]

# A)
for pokemon in pokemonList:
    name = pokemon['name']
    pokedexNumber = pokemon['pokedexNumber']
    types = pokemon['types']

    nameTree.insert_node(name, pokemon)
    pokedexNumberTree.insert_node(pokedexNumber, pokemon)
    typesTree.insert_node(types, pokemon)

# B)
def searchByCoincidence(node: NodeTree):
    if node.value.find('bul'.lower()) != -1:
        print(node.value)

# nameTree.inorden(searchByCoincidence)

# C)
types = ['water', 'fire', 'grass', 'electric']

def searchByTypes(node: NodeTree):
    for specificType in types:
        if specificType in node.value:
            print(node.other_values['name'])

# typesTree.inorden(searchByTypes)

# D)
# pokedexNumberTree.inorden()
# nameTree.inorden()
# nameTree.by_level()

# E)
# print(nameTree.search('lycanroc').value)
# print(nameTree.search('tyrantrum').value)
# print(nameTree.search('jolteon').value)

# F)
types = ['electric', 'steel']

def countByType(node: NodeTree, value):
    for specificType in types:
        if specificType in node.value:
            return 1
        else:
            return 0

# print(typesTree.count('', countByType))