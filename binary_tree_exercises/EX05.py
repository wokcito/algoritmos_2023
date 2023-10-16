'''5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
    I. determinar cuántos nodos tiene cada árbol;
    II. realizar un barrido ordenado alfabéticamente de cada árbol.'''

from classBinaryTree import BinaryTree, NodeTree

heroes_list = [
    {'name': 'iron man', 'hero': True},
    {'name': 'thanos', 'hero': False},
    {'name': 'capitan america', 'hero': True},
    {'name': 'red skull', 'hero': False},
    {'name': 'hulk', 'hero': True},
    {'name': 'black widow', 'hero': True},
    {'name': 'rocket raccon', 'hero': True},
    {'name': 'dotor strage', 'hero': True},
    {'name': 'doctor octopus', 'hero': True},
    {'name': 'deadpool', 'hero': True},
]

tree = BinaryTree()

for hero in heroes_list:
    tree.insert_node(hero['name'], hero['hero'])

# B)
def printVillan(node: NodeTree):
    if node.other_values is False:
        print(node.value)

# tree.inorden(printVillan)

# C)
START_WITH = 'c'

def heroesThatStartsWith(node: NodeTree):
    if node.other_values is True and node.value.lower().startswith(START_WITH.lower()):
        print(node.value)

tree.inorden(heroesThatStartsWith)

# D)
def heroesCounter(node: NodeTree, value):
    if node.other_values is value:
        return 1
    else:
        return 0

total = tree.count(True, heroesCounter)
# print(total)

# E)
def modifyName():
    value = input('ingrese el nombre que desea modificar ')
    pos = tree.search(value)
    print(pos)
    if pos:
        is_hero = pos.other_values
        tree.delete_node(value)

        new_value = input('ingrese en nuevo nombre ')
        tree.insert_node(new_value, is_hero)

        tree.inorden()
    else:
        print('no esta')

# modifyName()

# F)
heroes_tree = BinaryTree()
villans_tree = BinaryTree()

def bifurcation(node: NodeTree):
    if node.other_values is True:
        heroes_tree.insert_node(node.value)
    else:
        villans_tree.insert_node(node.value)

# tree.inorden(bifurcation)

heroes_tree.inorden()
villans_tree.inorden()

def countTotalNodes(node, value):
    return 1

total_heroes = heroes_tree.count('', countTotalNodes)
total_villans = villans_tree.count('', countTotalNodes)

# print(total_heroes)
# print(total_villans)