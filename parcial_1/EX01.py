words = ["Perro", "Gato", "Avion", "Perro", "Perro", "perro"]

def countWords(list, word, i = 0):
    if (len(list) == i):
        return 0
    elif (list[i].lower() == word.lower()):
        return 1 + countWords(list, word, i + 1)
    else:
        return 0 + countWords(list, word, i + 1)    

print(countWords(words, "Perro"))
