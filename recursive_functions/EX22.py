'''
El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:

a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila.
'''

BAG = ["soga", "sable de luz", "linterna", "botella de agua"]

def useTheForce(bag, objects = 0):

    if (len(bag) == 0):
        return f'No se encontró el Sable de Luz, se sacaron {objects} objetos.'
    elif (bag[-1] == "sable de luz"):
        return f'¡Sable de luz encontrado! Se sacaron {objects} objetos antes de encontrarlo.'
    else:
        return useTheForce(bag[:-1], objects + 1)

print(useTheForce(BAG))