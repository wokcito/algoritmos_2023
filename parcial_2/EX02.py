"""2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8"""

from classGraph import Graph
from random import randint

charactersGraph = Graph(False)

characters = ['luke skywalker', 'darth vader', 'yoda', 'boba fett', 'c-3po', 'leia', 'rey', 'kylo ren', 'chewbacca', 'han solo', 'r2-d2', 'bb-8']

for character in characters:
    charactersGraph.insert_vertice(character)

# A) y D)
charactersGraph.insert_arist('luke skywalker', 'darth vader', randint(1, 10))
charactersGraph.insert_arist('darth vader', 'yoda', randint(1, 10))
charactersGraph.insert_arist('yoda', 'boba fett', randint(1, 10))
charactersGraph.insert_arist('boba fett', 'c-3po', randint(1, 10))
charactersGraph.insert_arist('c-3po', 'leia', randint(1, 10))
charactersGraph.insert_arist('leia', 'rey', randint(1, 10))
charactersGraph.insert_arist('rey', 'kylo ren', randint(1, 10))
charactersGraph.insert_arist('kylo ren', 'chewbacca', randint(1, 10))
charactersGraph.insert_arist('chewbacca', 'han solo', randint(1, 10))
charactersGraph.insert_arist('han solo', 'r2-d2', randint(1, 10))
charactersGraph.insert_arist('r2-d2', 'bb-8', randint(1, 10))
charactersGraph.insert_arist('bb-8', 'luke skywalker', randint(1, 10))

# B)

[ kruskal ] = charactersGraph.kruskal()

print(kruskal)

if kruskal.find('yoda') != -1:
    print('Yoda sí es parte del árbol de expansión mínimo')
else:
    print('Yoda no es parte del árbol de expansión mínimo')

# C)
