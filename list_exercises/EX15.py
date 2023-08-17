"""
15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre,
cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;
"""

from classListList import List
from random import randint

trainerList = List("name", "name")

class Pokemon:
    def __init__(self, name, types, level = 1):
        self.name = name
        self.types = types
        self.level = level

    def __str__(self):
        return f'{self.name}-{self.level}-{self.types}'

class Trainer():
    def __init__(self, name, tournaments_won = 0, battles_won = 0, battles_lose = 0):
        self.name = name
        self.tournaments_won = tournaments_won
        self.battles_won = battles_won
        self.battles_lose = battles_lose

    def __str__(self):
        return f'\n{self.name} --> ctg:{self.tournaments_won}-cbg:{self.battles_won}-cbp:{self.battles_lose}'

def trainerIteration(callback, data = [], counter = 0):
    toReturn = []
    while counter < trainerList.size():
        trainer, pokemons = trainerList.getByIndex(counter)
        toReturn.append(callback(trainer, pokemons, data))
        counter += 1
    return toReturn

def pokemonIteration(callback, pokemons, data = [], counter = 0):
    toReturn = []
    while counter < pokemons.size():
        pokemon = pokemons.getByIndex(counter)
        toReturn.append(callback(pokemon, data))
        counter += 1
    return toReturn

t1 = Trainer('Maxi', randint(1, 10), randint(1, 10), randint(1, 10))
t2 = Trainer('Juan', randint(1, 10), randint(1, 10), randint(1, 10))
t3 = Trainer('Luigi', randint(1, 10), randint(1, 10), randint(1, 10))

trainers = [t1, t2, t3]

p1 = Pokemon('pikachu', ['electric'], randint(3, 20))
p2 = Pokemon('jolteon', ['electric'], randint(3, 20))
p3 = Pokemon('vaporeon', ['water'], randint(3, 20))
p4 = Pokemon('flareon', ['fire'], randint(3, 20))
p5 = Pokemon('leafeon', ['grass'], randint(3, 20))
p7 = Pokemon('leafeon', ['grass'], randint(3, 20))
p8 = Pokemon('leafeon', ['grass'], randint(3, 20))
p9 = Pokemon('leafeon', ['grass'], randint(3, 20))
p6 = Pokemon('pelipper', ['water', 'flying'], randint(3, 20))
p7 = Pokemon('terrakion', ['rock', 'fighting'], randint(3, 20))

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

for trainer in trainers:
    trainerList.insert(trainer)

for pokemon in pokemons:
    trainerIndex = randint(0, trainerList.size() - 1)
    trainer = trainerList.getByIndex(trainerIndex)
    trainer[1].insert(pokemon)

# A)
def ATrainer(trainer, pokemons, name):
    if (trainer.name == name):
        pokemon_quantity = pokemons.size()
        print(f"El entrenador {name} posee {pokemon_quantity} pokémon")

# trainerIteration(ATrainer, "Maxi")

# B)
def BTrainer(trainer, pokemons, data):
    if (trainer.tournaments_won > data):
        print(trainer)

# trainerIteration(B, 3)

# C)
def CTrainer(trainer, pokemons, data):
    return trainer.tournaments_won

def CPokemon(pokemon, data):
    return pokemon.level

def C():
    tournaments_data = trainerIteration(CTrainer)
    trainer_position = tournaments_data.index(max(tournaments_data))

    trainer, pokemons = trainerList.getByIndex(trainer_position)

    level_data = pokemonIteration(CPokemon, pokemons)
    pokemon_position = level_data.index(max(level_data))

    pokemon = pokemons.getByIndex(pokemon_position)

    print(f"El entrenador {trainer.name} tiene {trainer.tournaments_won} torneos ganados con su pokémon {pokemon.name} de nivel {pokemon.level}")

# C()

# D)
def D(name):
    trainer, pokemons = trainerList.getByValue(name)

    print(trainer)

    counter = 0

    while counter < pokemons.size():
        print(pokemons.getByIndex(counter))
        counter += 1

def DPokemon(pokemon, data):
    print(pokemon)

def DTrainer(trainer, pokemons, name):
    if (trainer.name == name):
        pokemonIteration(DPokemon, pokemons)

# trainerIteration(DTrainer, "Maxi")

# E)
def E(trainer, pokemons, data):
    percentage = (trainer.battles_won / (trainer.battles_won + trainer.battles_lose)) * 100
    if (percentage > 79):
        print(f"El entrenador {trainer.name} tiene un porcentaje de {percentage:2.2f}%")

# trainerIteration(E)

# F)
def FPokemon(pokemon, data):
    trainer, types = data

    match len(types):
            case 1:
                if (types[0] in pokemon.types):
                    print(trainer)
            case 2:
                type, subtype = types
                if (type in pokemon.types and subtype in pokemon.types):
                    print(trainer)

def FTrainer(trainer, pokemons, types):
    pokemonIteration(FPokemon, pokemons, [trainer, types])

# trainerIteration(FTrainer, ["water", "flying"])

# g
def GPokemon(pokemon, data):
    return pokemon.level

def GTrainer(trainer, pokemons, name):
    if (trainer.name == name):
        level_data = pokemonIteration(GPokemon, pokemons)
        print(f"El promedio de los pokémon de {name} es de {sum(level_data) / len(level_data)}")

# trainerIteration(GTrainer, "Maxi")

# H)
def HPokemon(pokemon, name):
    if (pokemon.name == name):
        return True
    else:
        return False

def HTrainer(trainer, pokemons, data):
    name_data = pokemonIteration(HPokemon, pokemons, data)
    if (True in name_data):
        return True
    else:
        return False

def H(name):
    own_data = trainerIteration(HTrainer, name)
    trainers_quantity = own_data.count(True)
    print(f"Se encontraron a {trainers_quantity} entrenador/es con ese pokémon")

# H('jolteon')

# I)
def IPokemon(pokemon, data):
    return pokemon.name

def ITrainer(trainer, pokemons, data):
    pokemons_data = pokemonIteration(IPokemon, pokemons)
    pokemon_counter = {}

    for name in pokemons_data:
        if (name in pokemon_counter):
            pokemon_counter[name] += 1
        else:
            pokemon_counter[name] = 1

    for name, quantity in pokemon_counter.items():
        if (quantity > 1):
            return print(f"El entrenador {trainer.name} tiene {quantity} {name}")

# trainerIteration(ITrainer)

# J)
def JPokemon(pokemon, names):
    if (pokemon.name in names):
        return True
    else:
        return False

def JTrainer(trainer, pokemons, data):
    name_data = pokemonIteration(JPokemon, pokemons, data)
    if (True in name_data):
        return [trainer, True]
    else:
        return [trainer, False]

def J(names):
    own_data = trainerIteration(JTrainer, names)

    for trainer, state in own_data:
        if (state == True):
            print(f"El entrenador {trainer.name} posee uno de los pokémon ingresados")

# J(['terrakion'])

# K)
def KPokemon(pokemon, data):
    return pokemon.name

def KTrainer(trainer, pokemons, data):
    t_name, p_name = data

    if (t_name == trainer.name):
        names_data = pokemonIteration(KPokemon, pokemons, data)
        if (p_name in names_data):
            print(f"Se encontró al entrenador {t_name} que tiene al pokemon {p_name}")
        else:
            print("No se encontró a un entrenador que posea ese pokémon")

def K(t_name, p_name):
    trainerIteration(KTrainer, [t_name, p_name])

# K("Maxi", "jolteon")