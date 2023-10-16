'''Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos

tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros están en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.'''

from classBinaryTree import BinaryTree, NodeTree, get_value_from_file

file_jedi = 'jedis.txt'
read_lines = open(file_jedi).readlines()

name_tree = BinaryTree()
species_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')

    name = jedi[0]
    rank = jedi[1]
    species = jedi[2]

    name_tree.insert_node(name, index + 2)
    ranking_tree.insert_node(rank, index + 2)
    species_tree.insert_node(species, index + 2)

# B)
# name_tree.inorden()
# ranking_tree.inorden()

# C)
# ranking_tree.by_level()
# species_tree.by_level()

# D)
def printCharacterInformation(name):
    node: NodeTree = name_tree.search(name)
    if node:
        print(get_value_from_file(file_jedi, node.other_values))
    else:
        print('no esta en la lista')

# printCharacterInformation('yoda')
# printCharacterInformation('luke skywalker')

# E)
def printJediMasters(node: NodeTree):
    if node.value.lower() == 'jedi master':
        print(get_value_from_file(file_jedi, node.other_values))

# ranking_tree.inorden(printJediMasters)

# F)
def printCharacterLightsaber(node: NodeTree):
    index = node.other_values
    value = get_value_from_file(file_jedi, index)
    colors_list = value[4].split('/')

    if 'green' in colors_list:
        print(value)

# name_tree.inorden(printCharacterLightsaber)

# G)
def printCharacterWithMaster(node: NodeTree):
    index = node.other_values
    value = get_value_from_file(file_jedi, index)
    masters_list = value[3].split('/')

    have_master = False

    for master in masters_list:
        master_node = name_tree.search(master)

        if master_node is not None:
            have_master = True

    if have_master:
        print(node.value)

# name_tree.inorden(printCharacterWithMaster)

# H)
def printCereanAndTogrutaCharacters(node: NodeTree):
    species = node.value.lower()
    index = node.other_values

    if species == 'togruta' or species == 'cerean':
        jedi = get_value_from_file(file_jedi, index)
        print(jedi)

# species_tree.inorden(printCereanAndTogrutaCharacters)

# I)
STARS_WITH = 'a'
CONTAINS = '-'

def startsWith(node: NodeTree):
    name = node.value

    if name.lower().startswith(STARS_WITH.lower()):
        print(name)

def contains(node: NodeTree):
    name = node.value

    if name.lower().find(CONTAINS.lower()) != -1:
        print(name)

# name_tree.inorden(startsWith)
# name_tree.inorden(contains)