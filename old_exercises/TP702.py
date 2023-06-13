'''Sea un lote de Números enteros positivos que finaliza con un cero que no debe ser
procesado. Generar un vector con dichos valores y calcular la productoria de sus
componentes'''

isZero = False
numbers = []

print("\nIngrese números para calcular su productoria, ¡Ingrese un 0 cuando desee terminar!\n")

while isZero == False:
    num = int(input("Ingrese un número: "))

    if (num == 0):
        isZero = True
    else:
        numbers.append(num)

total = 1

for num in numbers:
    total *= num

print(total)