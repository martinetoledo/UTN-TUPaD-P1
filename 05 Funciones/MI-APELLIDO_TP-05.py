from math import pi


def programa_principal():
    imprimir_hola_mundo()
    saludar_usuario(input("Ingrese su nombre: "))
    informacion_personal(
        input("Ingrese su nombre"),
        input("Ingrese su apellido"),
        input("Ingrese su edad"),
        input("Ingrese su lugar de residencia"),
    )
    radio = float(input("Ingrese el radio del circulo"))
    print(f"El area del circulo es {calcular_area_circulo(radio)}")
    # print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)}")
    segs = int(input("Ingrese una cantidad de segundos: "))
    print(f"{segs} segundos equivalen a {segundos_a_horas(segs)} horas")
    tabla_multiplicar(
        int(input("Ingrese un numero para ver su tabla de multiplicacion"))
    )

    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))

    suma, resta1, resta2, mult, div1, div2 = operaciones_basicas(a, b)

    print(f"\nResultados de operaciones entre {a} y {b}:\n")
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta1}")
    print(f"{b} - {a} = {resta2}")
    print(f"{a} x {b} = {mult}")
    print(f"{a} / {b} = {div1}")
    print(f"{b} / {a} = {div2}")

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    print(f"Su IMC es de {calcular_imc(peso,altura):.2f}")

    celsius = float(input("Ingrese una temperatura en grados celsius: "))

    print(f"El equivalente en fahrenheit es {celsius_a_fahrenheit(celsius)}")

    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    c = int(input("Ingrese un tercer numero: "))

    print(f"El promedio de los 3 numeros es {calcular_promedio(a,b,c)}")


def calcular_promedio(a, b, c):
    total = sum([a, b, c])
    return total / 3


def celsius_a_fahrenheit(celsius):
    return (9 / 5 * celsius) + 32


def calcular_imc(peso, altura):
    return peso / (altura**2)


def operaciones_basicas(a, b):
    suma = a + b
    resta1 = a - b
    resta2 = b - a
    multiplicacion = a * b
    division1 = a / b
    division2 = b / a

    return (suma, resta1, resta2, multiplicacion, division1, division2)


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {i*numero}")


def segundos_a_horas(segundos):
    return segundos / 60


def imprimir_hola_mundo():
    print("Hola Mundo!")


def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):
    return pi * radio * radio


def calcular_perimetro_circulo(radio):
    return 2 * pi * radio


if __name__ == "__main__":
    programa_principal()
