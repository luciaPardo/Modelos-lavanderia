def menor_tiempo_prendas(archivo):
    """ """
    tiempo = {}
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
                tiempo[lin[0]] = lin[1]
    tiempo_lavanderia(params, tiempo, incom)


def tiempo_lavanderia(parametros, tiempo, incom):
    suma = 0
    a_lavar = []
    lavados = []
    soluc = {}
    lavado_nro = 1
    while len(lavados) < int(parametros[0]):
        for prenda in incom.keys():
            if len(a_lavar) == 0:
                a_lavar.append(prenda)
            elif not es_incompatible(a_lavar, incom, prenda) and prenda not in lavados:
                a_lavar.append(prenda)
        lavados += a_lavar
        suma, incom, soluc = pasar_a_solucion(
            a_lavar, tiempo, suma, incom, soluc, lavado_nro)
        lavado_nro += 1
        a_lavar = []
    print(suma)
    parsear_output(soluc)
    return


def pasar_a_solucion(a_lavar, tiempo, suma, incom, soluc, lavado_nro):
    a_sumar = 0
    for elem in a_lavar:
        if tiempo[elem] > a_sumar:
            a_sumar = tiempo[elem]
        soluc[elem] = lavado_nro
        incom.pop(elem, None)
    suma += a_sumar
    return suma, incom, soluc


def parsear_output(soluc):
    with open("entrega_2.txt", "w") as entrega:
        for key, value in soluc.items():
            entrega.write(f"{key} {value}\n")


def es_incompatible(a_lavar, incom, por_agregar):
    for prenda in a_lavar:
        if por_agregar in a_lavar or prenda in incom[por_agregar]:
            return True
    return False


menor_tiempo_prendas("segundo_problema.txt")
