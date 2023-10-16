'''23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.
'''

from classBinaryTree import BinaryTree, NodeTree

datos = [
  { 'name': 'Ceto', 'defeated_by': '' },
  { 'name': 'Cerda de Cromión', 'defeated_by': 'Teseo' },
  { 'name': 'Tifón', 'defeated_by': 'Zeus' },
  { 'name': 'Ortro', 'defeated_by': 'Heracles' },
  { 'name': 'Equidna', 'defeated_by': 'Argos Panoptes' },
  { 'name': 'Toro de Creta', 'defeated_by': 'Teseo' },
  { 'name': 'Dino', 'defeated_by': '' },
  { 'name': 'Jabalí de Calidón', 'defeated_by': 'Atalanta' },
  { 'name': 'Pefredo', 'defeated_by': '' },
  { 'name': 'Carcinos', 'defeated_by': '' },
  { 'name': 'Enio', 'defeated_by': '' },
  { 'name': 'Gerión', 'defeated_by': 'Heracles' },
  { 'name': 'Escila', 'defeated_by': '' },
  { 'name': 'Cloto', 'defeated_by': '' },
  { 'name': 'Caribdis', 'defeated_by': '' },
  { 'name': 'Láquesis', 'defeated_by': '' },
  { 'name': 'Euríale', 'defeated_by': '' },
  { 'name': 'Átropos', 'defeated_by': '' },
  { 'name': 'Esteno', 'defeated_by': '' },
  { 'name': 'Minotauro de Creta', 'defeated_by': 'Teseo' },
  { 'name': 'Medusa', 'defeated_by': 'Perseo' },
  { 'name': 'Harpías', 'defeated_by': '' },
  { 'name': 'Ladón', 'defeated_by': 'Heracles' },
  { 'name': 'Argos Panoptes', 'defeated_by': 'Hermes' },
  { 'name': 'Águila del Cáucaso', 'defeated_by': '' },
  { 'name': 'Aves del Estínfalo', 'defeated_by': '' },
  { 'name': 'Quimera', 'defeated_by': 'Belerofonte' },
  { 'name': 'Talos', 'defeated_by': 'Medea' },
  { 'name': 'Hidra de Lerna', 'defeated_by': 'Heracles' },
  { 'name': 'Sirenas', 'defeated_by': '' },
  { 'name': 'León de Nemea', 'defeated_by': 'Heracles' },
  { 'name': 'Pitón', 'defeated_by': 'Apolo' },
  { 'name': 'Esfinge', 'defeated_by': 'Edipo' },
  { 'name': 'Cierva de Cerinea', 'defeated_by': '' },
  { 'name': 'Dragón de la Cólquida', 'defeated_by': '' },
  { 'name': 'Basilisco', 'defeated_by': '' },
  { 'name': 'Cerbero', 'defeated_by': '' },
  { 'name': 'Jabalí de Erimanto', 'defeated_by': '' }
]


tree = BinaryTree()

for creature in datos:
    tree.insert_node(creature['name'].lower(), { 'defeated_by': creature['defeated_by'].lower() })

# A)
def printCreature(node: NodeTree):
    print(node.value, node.other_values)

# tree.inorden(printCreature)

# B)
def addDescription(name, description):
    creature = tree.search(name)

    if creature is not None:
        information = creature.other_values
        information['description'] = description

# addDescription('basilisco', 'Holaaaaaaaaaa')

# C)

def getCreatureInformation(name):
    creature: NodeTree = tree.search(name)

    if creature is not None:
        print(creature.value, creature.other_values)
    else:
        print('No existe')

# getCreatureInformation('taLoS')

# D)
ranking = {}

def winRanking(node: NodeTree):
    if node.other_values['defeated_by'] != '':
        if node.other_values['defeated_by'] not in ranking:
            ranking[node.other_values['defeated_by']] = 1
        else:
            ranking[node.other_values['defeated_by']] += 1

# tree.inorden(winRanking)

# def order_by(item):
#     return item[1]

# ordenados = list(ranking.items())
# ordenados.sort(key=order_by, reverse=True)
# print(ordenados[:3])

# E)
def creatureDefeatedByHeracles(node: NodeTree):
    if node.other_values['defeated_by'] == 'heracles':
        print(node.value)

# tree.inorden(creatureDefeatedByHeracles)

# F)
def undefeatedCreature(node: NodeTree):
    if node.other_values['defeated_by'] == '':
        print(node.value)

# tree.inorden(undefeatedCreature)

# G)
# H)
def addCaught(name: str, capturer: str):
    creature: NodeTree = tree.search(name)

    if creature is not None:
        creature.other_values['caught_by'] = capturer

addCaught('Cerbero', 'heracles')
addCaught('Toro de Creta', 'heracles')
addCaught('Cierva de Cerinea', 'heracles')
addCaught('Jabalí de Erimanto', 'heracles')

# I)
SEARCH = 'sili'

def searchByCoincidence(node: NodeTree):
    name = node.value
    if name.find(SEARCH.lower()) != -1:
        print(name)

# tree.inorden(searchByCoincidence)

# K)
# L)
def modifyName(oldName, newName):
    creature = tree.search(oldName)
    if creature is not None:
        tree.delete_node(oldName)
        tree.insert_node(newName.lower())
        tree.inorden()
    else:
        print('No está')

# modifyName('ladón', 'dragón ladón')

# M)
# tree.by_level()

def caughtByHeracles(node: NodeTree):
    other_values = node.other_values

    if 'caught_by' in other_values and other_values['caught_by'] == 'heracles':
        print(node.value)

# tree.inorden(caughtByHeracles)