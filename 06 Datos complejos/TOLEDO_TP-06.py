from math import pi

# 1)

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300


# 2)

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800


# 3)

frutas = precios_frutas.keys()


# 4)
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(
            f"Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} anios."
        )


yo = Persona("martin", "argentina", 30)

yo.saludar()

# 5)


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        print(f"El area del circulo es {pi*float(self.radio) ** 2}")

    def calcular_perimetro(self):
        print(f"El perimetro del circulo es {pi*2*float(self.radio)}")


mi_circ = Circulo(5)

mi_circ.calcular_area()

mi_circ.calcular_perimetro()

# 6)


class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else None


def balanceado(caracteres):
    pila = Pila()
    pares = {")": "(", "}": "{", "]": "["}

    for caracter in caracteres:
        if caracter in "({[":
            pila.apilar(caracter)
        elif caracter in ")}]":
            if pila.esta_vacia() or pila.desapilar() != pares[caracter]:
                return False

    return pila.esta_vacia()


print(balanceado("({[]})"))

print(balanceado("({[})"))

# 7)


class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, cliente):
        self.elementos.append(cliente)

    def desencolar(self):
        return (
            self.elementos.pop(0)
            if not self.esta_vacia()
            else "No hay clientes en la fila"
        )

    def esta_vacia(self):
        return len(self.elementos) == 0

    def siguiente_cliente(self):
        return (
            self.elementos[0] if not self.esta_vacia() else "No hay clientes en la fila"
        )

    def mostrar_fila(self):
        return self.elementos


cola_banco = Cola()

cola_banco.encolar("cliente 1")
cola_banco.encolar("cliente 2")

print("Siguiente cliente:", cola_banco.siguiente_cliente())
print("Atendiendo a:", cola_banco.desencolar())

print("Siguiente cliente:", cola_banco.siguiente_cliente())
print("Clientes en la fila:", cola_banco.mostrar_fila())


# 8 y 9)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
