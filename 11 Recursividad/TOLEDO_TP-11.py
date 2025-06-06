def ejercicio_1():
    def fact(n):
        if n == 0 or n == 1:
            return 1
        return n * fact(n - 1)

    n = int(input("Ingrese un número entero positivo: "))
    for i in range(1, n + 1):
        print(f"{i}! =", fact(i))


def ejercicio_2():
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    n = int(input("Ingrese la posición n para Fibonacci: "))
    for i in range(1, n + 1):
        print(f"Fibonacci({i}) =", fib(i))


def ejercicio_3():
    def potencia(base, exp):
        if exp == 0:
            return 1
        return base * potencia(base, exp - 1)

    base = int(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))
    print("Resultado potencia =", potencia(base, exp))


def ejercicio_4():
    def a_binario(n):
        if n < 2:
            return str(n)
        return a_binario(n // 2) + str(n % 2)

    n = int(input("Ingrese un número entero positivo para convertir a binario: "))
    print("Binario =", a_binario(n))


def ejercicio_5():
    def es_pal(palabra):
        if len(palabra) <= 1:
            return True
        if palabra[0] == palabra[-1]:
            return es_pal(palabra[1:-1])
        return False

    palabra = input("Ingrese una palabra sin espacios ni tildes: ")
    print("Es palIndromo?:", es_pal(palabra))


def ejercicio_6():
    def suma_dig(n):
        if n < 10:
            return n
        return n % 10 + suma_dig(n // 10)

    n = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
    print("Suma de dígitos =", suma_dig(n))


def ejercicio_7():
    def contar(n):
        if n == 1:
            return 1
        return n + contar(n - 1)

    n = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
    print("Total de bloques =", contar(n))


def ejercicio_8():
    def contar_digito(numero, digito):
        if numero == 0:
            return 0
        cuenta = 1 if numero % 10 == digito else 0
        return cuenta + contar_digito(numero // 10, digito)

    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))
    print("Apariciones del dígito =", contar_digito(numero, digito))


if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()
