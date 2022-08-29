def menor_tiempo_prendas(archivo):
    """ """
    tiempo = {}
    params = []
    incom = {}
    with open(archivo, "r") as lav:
        for linea in lav:
            if linea[0] == "p":  # parametros
                params = linea.split()[1::]
            elif linea[0] == "e":  # incompatibilidad
                lin = linea.split()[1::]
                incom[lin[0]] = incom.get(lin[0], []) + [lin[1]]
            elif linea[0] == "n":  # tiempo
                lin = linea.split()[1::]
                tiempo[lin[0]] = lin[1]
    tiempo_lavanderia(params, tiempo, incom)


def tiempo_lavanderia(parametros, tiempo, incom):
    suma = 0
    incompat_tot = []
    a_lavar = []
    lavados = []
    while len(lavados) <= int(parametros[1]):
        for prenda in incom:
            if len(a_lavar) == 0:
                a_lavar.append(prenda)
            elif prenda not in a_lavar and not es_incompatible(a_lavar, incom, prenda):
                a_lavar.append(prenda)
        # print(a_lavar)
        a_sumar = 0
        for elem in a_lavar:
            if int(tiempo[elem]) > a_sumar:
                a_sumar = int(tiempo[elem])
        suma += a_sumar
        lavados += a_lavar
        a_lavar = []
    print(suma)
    return


def es_incompatible(a_lavar, incom, por_agregar):
    print(a_lavar)
    for prenda in a_lavar:
        print(incom[por_agregar])
        if por_agregar in a_lavar or prenda in incom[por_agregar]:
            return True
    return False


menor_tiempo_prendas("primer_problema.txt")
