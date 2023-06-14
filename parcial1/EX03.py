import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("algoritmos_2023"))))

from classStack import Stack

logStack = Stack()

class Mision():
    def __init__(self, name, planet, credits):
        self.name = name
        self.planet = planet
        self.credits = credits

    def __str__(self):
        return f"The mision {self.name} was in {self.planet} for {self.credits} credits"

logs = [
    {"name": "Track x down", "planet": "Alderaan", "credits": 500},
    {"name": "Track Han Solo down", "planet": "Tatooine", "credits": 5000},
    {"name": "Track y down", "planet": "Naboo", "credits": 2000}
]

def fillStack():
    for data in logs:
        mision = Mision(data["name"], data["planet"], data["credits"])
        logStack.push(mision)

# a
print("\na)")

fillStack()

while logStack.size() > 0:
    mision = logStack.pop()
    print(mision)

# b
print("\nb)")

fillStack()

total_credits = 0

while logStack.size() > 0:
    mision = logStack.pop()
    total_credits += mision.credits

print(total_credits)

# c
print("\nc)")

fillStack()

while logStack.size() > 0:
    mision = logStack.pop()

    if ("Han Solo" in mision.name):
        print(mision.planet)