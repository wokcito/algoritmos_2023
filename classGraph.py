from classProfeList import List as ListaArista
from classQueue import Queue
from classStack import Stack
from classHeapMin import Heap

class Arista():
    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso
    
    def __str__(self):
        return f"{self.vertice} {self.peso}"

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('No se puede ordenar por este criterio')

class Graph():
    def __init__(self, dirigido = True):
        self.__elements = []
        self.dirigido = dirigido

    def insert_vertice(self, value, criterio = None):
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaArista(), False])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaArista(), False])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaArista(), False])

    def insert_arist(self, vertice_ori, vertice_des, peso, criterio_vertice = None, criterio_arista = 'vertice'):
        origen = self.search_vertice(vertice_ori, criterio_vertice)
        destino = self.search_vertice(vertice_des, criterio_vertice)
        if origen is not None and destino is not None:
            self.get_element_by_index(origen)[1].insert(Arista(vertice_des, peso), criterio_arista)
            if not self.dirigido:
                self.get_element_by_index(destino)[1].insert(Arista(vertice_ori, peso), criterio_arista)

    def search_vertice(self, search_value, criterio = None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def delete_vertice(self, value, criterio=None):
        return_value = None
        pos = self.search_vertice(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
            for vertice in self.__elements:
                vertice[1].delete(value, 'vertice')

        return return_value

    def delete_arista(self, origen, destino):
        pos_origen = self.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = self.get_element_by_index(pos_origen)
            delete = ver_origen[1].delete(destino, 'vertice')
            if not self.dirigido:
                pos_destino = self.search_vertice(destino)
                if pos_destino is not None:
                    ver_destino = self.get_element_by_index(pos_destino)
                    ver_destino[1].delete(origen, 'vertice')
            return delete

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value[0])
            print('------------- Aristas -------------')
            value[1].barrido()
            print()

    # def order_by(self, criterio=None, reverse=False):
    #     dic_atributos = self.__elements[0][0].__dict__
    #     if criterio in dic_atributos:
    #         def func_criterio(valor):
    #             return valor.__dict__[criterio]

    #         self.__elements.sort(key=func_criterio, reverse=reverse)
    #     else:
    #         print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def is_adyacent(self, origen, destino):
        result = False
        pos_origen = self.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = self.get_element_by_index(pos_origen)
            arista = ver_origen[1].search(destino, 'vertice')
            result = True if arista is not None else False
        return result

    def adyacents(self, origen):
        pos_origen = self.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = self.get_element_by_index(pos_origen)
            ver_origen[1].barrido()

    def mark_as_not_visited(self):
        for vertice in self.__elements:
            vertice[2] = False

    def deep_list(self, posicion = 0):
        origen = self.get_element_by_index(posicion)
        if origen is not None:
            if not origen[2]:
                origen[2] = True
                print(origen[0])
                adjacentes = origen[1]
                for index in range(adjacentes.size()):
                    arista = adjacentes.get_element_by_index(index).vertice
                    vertice_adjacente = self.search_vertice(arista)
                    if vertice_adjacente is not None:
                        adjacente = self.get_element_by_index(vertice_adjacente)
                        if not adjacente[2]:
                            self.deep_list(posicion = vertice_adjacente)
                
    def amplitude_list(self, posicion = 0):
        origen = self.get_element_by_index(posicion)
        if origen is not None:
            cola_pendientes = Queue()
            cola_pendientes.arrive(origen)
            while not cola_pendientes.size() == 0:
                vertice = cola_pendientes.atention()
                if not vertice[2]:
                    vertice[2] = True
                    print(vertice[0])
                    adjacentes = vertice[1]
                    for index in range(adjacentes.size()):
                        arista = adjacentes.get_element_by_index(index).vertice
                        vertice_adjacente = self.search_vertice(arista)
                        if vertice_adjacente is not None:
                            adjacente = self.get_element_by_index(vertice_adjacente)
                            if not adjacente[2]:
                                cola_pendientes.arrive(adjacente)
            
    def has_path(self, origen, destino):
        result = False
        origen = self.search_vertice(origen)
        if origen is not None:
            vertice_origen = self.get_element_by_index(origen)
            if not vertice_origen[2]:
                vertice_origen[2] = True
                # print(vertice_origen[0])
                adjacentes = vertice_origen[1]
                pos_destino = adjacentes.search(destino, 'vertice')
                if pos_destino is not None:
                    result = True
                    return result
                for index in range(adjacentes.size()):
                    arista = adjacentes.get_element_by_index(index).vertice
                    vertice_adjacente = self.search_vertice(arista)
                    if vertice_adjacente is not None:
                        adjacente = self.get_element_by_index(vertice_adjacente)
                        if not adjacente[2]:
                            result = self.has_path(adjacente[0], destino)
        return result

    def dijkstra(self, origen, destino):
        from math import inf
        """Algoritmo de Dijkstra para hallar el camino mas corto."""
        no_visitados = Heap()
        camino = Stack()
        for i in range(self.size()):
            vertice = self.get_element_by_index(i)    
            if(vertice[0] == origen):
                no_visitados.arrive(vertice, 0)
            else:
                no_visitados.arrive(vertice, inf)

        while no_visitados.size() > 0:
            vertice = no_visitados.atention()
            camino.push([vertice[1][0], vertice[0], vertice[2]])
            adjacentes = vertice[1][1]
            for index in range(adjacentes.size()):
                arista = adjacentes.get_element_by_index(index)
                pos = no_visitados.search(arista.vertice)
                if pos is not None:
                    if(no_visitados.vector[pos][0] > vertice[0] + arista.peso):
                        no_visitados.vector[pos][2] = vertice[1][0]
                        no_visitados.change_priority(pos, vertice[0] + arista.peso)
        return camino


    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index

        bosque = []
        aristas = Heap()
        for index in range(self.size()):
            vertice = self.get_element_by_index(index)
            bosque.append(vertice[0])
            aristas_adjacentes = vertice[1]
            for i in range(aristas_adjacentes.size()):
                arista = aristas_adjacentes.get_element_by_index(i)
                aristas.arrive([vertice[0], arista.vertice], arista.peso)

        while len(bosque) > 1 and aristas.size() > 0:
            arista = aristas.atention()
            origen = buscar_en_bosque(bosque, arista[1][0])
            destino = buscar_en_bosque(bosque, arista[1][1])
            if origen is not None and destino is not None:
                if origen != destino:
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)
                        vertice_des = bosque.pop(destino)
                    else:
                        vertice_des = bosque.pop(destino)
                        vertice_ori = bosque.pop(origen)

                    if '-' not in vertice_ori and '-' not in vertice_des:
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')

        return bosque