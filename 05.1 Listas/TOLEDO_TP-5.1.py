def punto1():
    print([i for i in range(1, 101) if i % 4 == 0])


def punto2():
    lista = [1, 2, 3, 4, 5]
    print(lista[-2])


def punto3():
    lista_vacia = []
    lista_vacia.append("hola")
    lista_vacia.append("como")
    lista_vacia.append("va")

    print(lista_vacia)


def punto4():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"


def punto5():
    print(
        "El programa remueve el numero mas grande (22) de la lista e imprime la lista"
    )


def punto6():
    lista = [i for i in range(10, 31, 5)]
    print(lista[:2])


def punto7():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "astra"
    autos[2] = "ranger"
    print(autos)


def punto8():
    dobles = []
    for i in range(5, 16, 5):
        dobles.append(i * 2)
    print(dobles)


def punto9():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)


def punto10():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print(lista_anidada)


if __name__ == "__main__":
    punto1()
    punto2()
    punto3()
    punto4()
    punto5()
    punto6()
    punto7()
    punto8()
    punto9()
    punto10()
