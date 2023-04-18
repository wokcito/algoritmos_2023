'''Dada una secuencia de caracteres, obtener dicha secuencia invertida'''

def invertir(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1])

print(invertir(""))