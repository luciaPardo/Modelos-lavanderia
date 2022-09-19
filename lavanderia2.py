import numpy as np
import random
# list(itertools.permutations([1, 2, 3]))


def parsear_input(archivo):
    """ """
    tiempo = []
    params = []
    incom = {}
    with open(archivo, "r") as lav:
        for linea in lav:
            if linea[0] == "p":  # parametros
                params = list(map(int, linea.split()[2::]))
            elif linea[0] == "e":  # incompatibilidad
                lin = linea.split()[1::]
                incom[int(lin[0])] = incom.get(int(lin[0]), []) + [int(lin[1])]
            elif linea[0] == "n":  # tiempo
                lin = list(map(int, linea.split()[1::]))
                tiempo.append((lin[1], lin[0]))
        return incom, sorted(tiempo, reverse=True)


def tiempo_lavanderia(incom, tiempos_max):
    suma = 0
    a_lavar = []
    soluc = {}
    lavado_nro = 1
    print(tiempos_max)
    mezclado = random.shuffle(tiempos_max)
    while len(tiempos_max):
        for mayor_tiempo in tiempos_max:
            prenda = mayor_tiempo[1]
            if len(a_lavar) == 0:
                a_lavar.append(mayor_tiempo)
                suma += mayor_tiempo[0]
            elif not es_incompatible(a_lavar, incom, prenda):
                a_lavar.append(mayor_tiempo)
        pasar_a_solucion(a_lavar, soluc, lavado_nro, tiempos_max)
        lavado_nro += 1
        a_lavar = []
    # print(suma)
    parsear_output(soluc)
    return suma


def pasar_a_solucion(a_lavar, soluc, lavado_nro, tiempos_max):
    for tiempo, elem in a_lavar:
        soluc[elem] = lavado_nro
        tiempos_max.remove((tiempo, elem))


def parsear_output(soluc):
    with open("entrega_5.txt", "w") as entrega:
        for key, value in soluc.items():
            entrega.write(f"{key} {value}\n")


def es_incompatible(a_lavar, incom, por_agregar):
    for _, prenda in a_lavar:
        # Esto lo hago porque no estan hechas las reciprocas en el archivo con las incompatibilidades
        if por_agregar in incom:
            if prenda in incom[por_agregar]:
                return True
        if prenda in incom:
            if por_agregar in incom[prenda]:
                return True
    return False


def main():
    suma = 4000
    soluc = {}

    while (suma > 300):
        incom, tiempos_max = parsear_input("segundo_problema.txt")
        suma = tiempo_lavanderia(incom, tiempos_max)

    print(suma)


main()
