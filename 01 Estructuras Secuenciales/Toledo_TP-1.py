# 1)
print("Hola Mundo!")

# 2)
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")

# 3)
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
lugar = input("Ingrese su lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4)
import math

radio = input("Ingrese el radio del circulo")
print(f"El area del circulo es {math.pi*float(radio)*float(radio)}")
print(f"El perimetro del circulo es {math.pi*2*float(radio)}")

# 5)
segundos = float(input("Ingrese una cantidad de segundos"))
print(f"Equivalen a {segundos/3600} horas")

# 6)
num = int(input("Ingrese un numero para ver su tabla de multiplicacion"))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 7)
numa = float(input("Ingrese un numero distinto de 0"))
numb = float(input("Ingrese otro numero distinto de 0:"))
print(f"{numa} + {numb} = {numa + numb}")
print(f"{numa} - {numb} = {numa - numb}")
print(f"{numb} - {numa} = {numb - numa}")
print(f"{numa} x {numb} = {numa * numb}")
print(f"{numa} % {numb} = {numa / numb}")
print(f"{numb} % {numa} = {numb * numa}")

# 8)
altura = float(input("Ingrese su altura en metros:"))
peso = float(input("Ingrese su peso en kg:"))
print(f"Su IMC es {peso/(altura*altura)}")

# 9)
celsius = float(input("Ingrese un valor en grados Celsius"))
print(f"El equivalente en grados Fahrenheit es {(9/5*celsius)+32}")

# 10)
num1 = float(input("Ingrese un numero"))
num2 = float(input("Ingrese otro numero"))
num3 = float(input("Ingrese un ultimo numero"))
print(f"El promedio es {(num1+num2+num3)/3}")
