import random
from statistics import mode, median, mean

# 1)

edad = input("Ingrese su edad: ")

if int(edad) > 18:
    print("Es mayor de edad")

# 2)

nota = input("Ingrese su nota: ")

if int(nota) >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3)

while int(input("Ingrese un numero: ")) % 2 != 0:
    print("Por favor, ingrese un numero par")
else:
    print("Ha ingresado un numero par")

# 4)

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# 5)

while True:

    password = input("Ingrese una constrasenia entre 8 y 14 caracteres: ")

    if 8 <= len(password) <= 14:
        print("Ha ingresado una contrasenia correcta")
        break
    else:
        print("Por favor ingrese una contrasenia entre 8 y 14 caracteres")

# 6)

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")

# 7)
vocales = "aeiou"

frase = input("Ingrese una frase: ")

if frase[-1] in vocales:
    print(f"{frase}!")
else:
    print(frase)

# 8)

nombre = input("Ingrese su nombre: ")
opcion = input(
    "Ingrese la opcion deseada:\n 1. Nombre en mayusculas \n 2. Nombre en minusculas \n 3. Nombre con primera letra mayuscula \n"
)

if int(opcion) == 1:
    print(nombre.upper())
elif int(opcion) == 2:
    print(nombre.lower())
elif int(opcion) == 3:
    print(nombre.title())

# 9)

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

# 10)

hemisferio = input("Ingrese el hemisferio donde se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes del año: "))
dia = int(input("Ingrese el día del mes: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"


print(f"{estacion_norte if hemisferio == "N" else estacion_sur}")
