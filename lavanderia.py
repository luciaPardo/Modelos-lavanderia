def menor_tiempo_prendas(archivo):
    """ """
    tiempo = []
    params = []
    incom = []
    with open(archivo, "r") as lav:
        for linea in lav:
            if linea[0] == "p":  # parametros
                params.append(linea.split()[1::])
            else if linea[0] == "e":  # incompatibilidad
                incom.append(linea.split()[1::])
            else if linea[0] == "n":  # tiempo
                tiempo.append(linea.split()[1::])

    tiempo_lavanderia(params, incom, tiempo)


def tiempo_lavanderia(parametros, tiempo, incom):

    for _ in range(parametros[1]):
        # busqueda binaria????
