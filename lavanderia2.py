import numpy as np


def menor_tiempo_prendas(archivo):
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
        tiempos_max = sorted(tiempo, reverse=True)
        tiempo_lavanderia(params, incom, tiempos_max)


def tiempo_lavanderia(parametros, incom, tiempos_max):
    suma = 0
    a_lavar = []
    lavados = []
    soluc = {}
    lavado_nro = 1
    while len(lavados) < int(parametros[0]):
        for mayor_tiempo in tiempos_max:
            prenda = mayor_tiempo[1]
            if len(a_lavar) == 0:
                a_lavar.append(mayor_tiempo)
            elif not es_incompatible(a_lavar, incom, prenda):
                a_lavar.append(mayor_tiempo)
                # print(prenda)
        lavados += a_lavar
        suma, incom, soluc = pasar_a_solucion(
            a_lavar, suma, incom, soluc, lavado_nro)
        lavado_nro += 1
        a_lavar = []
    print(suma)
    parsear_output(soluc)
    return


def pasar_a_solucion(a_lavar, suma, incom, soluc, lavado_nro):
    a_sumar = 0
    for tiempo, elem in a_lavar:
        if tiempo > a_sumar:
            a_sumar = tiempo
        soluc[elem] = lavado_nro
        incom.pop(elem, None)
        tiempos_max.remove((tiempo, elem))
    suma += a_sumar
    return suma, incom, soluc


def parsear_output(soluc):
    with open("entrega_2.txt", "w") as entrega:
        for key, value in soluc.items():
            entrega.write(f"{key} {value}\n")


def es_incompatible(a_lavar, incom, por_agregar):
    for _, prenda in a_lavar:
        # Esto lo hago porque no estan hechas las reciprocas en el archivo con las incompatibilidades
        if por_agregar in incom:
            if por_agregar in a_lavar or prenda in incom[por_agregar]:
                return True
        if prenda in incom:
            if por_agregar in a_lavar or por_agregar in incom[prenda]:
                return True
    return False


menor_tiempo_prendas("segundo_problema.txt")
