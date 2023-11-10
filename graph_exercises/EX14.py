"""Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv."""

from classGraph import Graph

houseGraph = Graph(False)

habitaciones = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitacion 1', 'habitacion 2', 'sala de estar', 'terraza', 'patio']

class Habitacion():
    def __init__(self, name):
        self.name = name

for habitacion in habitaciones:
    houseGraph.insert_vertice(habitacion)

houseGraph.insert_arist('cocina', 'comedor', 20)
houseGraph.insert_arist('comedor', 'cochera', 14)
houseGraph.insert_arist('cochera', 'quincho', 30)
houseGraph.insert_arist('quincho', 'baño 1', 3)
houseGraph.insert_arist('baño 1', 'baño 2', 50)
houseGraph.insert_arist('baño 2', 'habitacion 1', 10)
houseGraph.insert_arist('habitacion 1', 'habitacion 2', 17)
houseGraph.insert_arist('habitacion 2', 'sala de estar', 24)
houseGraph.insert_arist('sala de estar', 'terraza', 14)
houseGraph.insert_arist('terraza', 'patio', 32)
houseGraph.insert_arist('cocina', 'patio', 15)
houseGraph.insert_arist('comedor', 'terraza', 29)
houseGraph.insert_arist('cochera', 'sala de estar', 4)
houseGraph.insert_arist('quincho', 'habitacion 2', 40)
houseGraph.insert_arist('baño 1', 'habitacion 1', 7)
houseGraph.insert_arist('patio', 'comedor', 26)
houseGraph.insert_arist('patio', 'sala de estar', 22)
houseGraph.insert_arist('patio', 'baño 1', 14)
houseGraph.insert_arist('cocina', 'baño 2', 9)
houseGraph.insert_arist('comedor', 'sala de estar', 5)

print(houseGraph.kruskal())

stack = houseGraph.dijkstra('habitacion 1', 'sala de estar')

while stack.size() > 0:
    print(stack.on_top())
    stack.pop()
