'''Generar y emitir el vector A = (1,0,1,0,1,0, ...) de N elementos'''

lon = int(input("\nIngrese la longitud que desee para su lista: "))
list = []
counter = 0

while counter < lon:
    if (counter % 2 == 0):
        list.append(1)
    else:
        list.append(0)

    counter += 1

print(list)



