import random
from statistics import mean

# 1)

print("\n".join([str(i) for i in range(0, 101)]))

# 2)

numero = input("Ingrese un numero entero: ")

print(f"El numero tiene {len(numero)} digitos")

# 3)

num1 = int(input("Ingrese el primer numero: "))

num2 = int(input("Ingrese el segundo numero: "))

total = 0

for i in range(num1 + 1, num2):
    total += i

print(total)

# 4)

sum = 0
while True:
    num = int(input("Ingrese un numero entero: "))
    if num == 0:
        print(sum)
        break
    else:
        sum += num

# 5)

correcto = random.randint(0, 9)
intentos = 0

while True:
    num = int(input("Intente adivinar el numero entre 0 y 9:"))
    intentos += 1
    if num == correcto:
        print(f"Correcto. Cantidad de intentos {intentos}")
        break
    else:
        print("Incorrecto. Intente de nuevo")

# 6)

numeros = [i for i in range(1, 101) if i % 2 == 0]

for n in numeros[::-1]:
    print(n)

# 7)

num = int(input("Ingrese un numero entero positivo"))

sum = sum(range(1, num))

print(sum)

# 8)
numeros = []

for x in range(100):
    numeros.append(int(input("Ingrese un numero entero")))

pares = [i for i in numeros if i % 2 == 0]

impares = [i for i in numeros if i % 2 != 0]

negativos = [i for i in numeros if i < 0]

positivos = [i for i in numeros if i >= 0]

print(
    f"Se ingresaron {len(pares)} numeros pares, {len(impares)} numeros impares, {len(negativos)} numeros negativos y {len(positivos)} numeros positivos"
)

# 9)

numeros = []

for x in range(5):
    numeros.append(int(input("Ingrese un numero entero")))

print(mean(numeros))

# 10)

num = input("Ingrese un numero: ")

print(num[::-1])
