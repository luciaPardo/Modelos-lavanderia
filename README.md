# Modelos-lavanderia

## Presento ideas generales:

    El problema tiene como contexto una lavandería las cuales algunas pueden ir juntas y otras no.
    A su vez cada prenda lleva un tiempo lavarla.
    Se quiere optimizar el problema de forma de generar la mayor ganancia de tiempo.

    La primera mirada al problema se centró en como resolver el problema, y se intentó de forma de fuerza bruta.

    Esto es, generar un diccionario con las incompatibilidades y otro con los tiempos respectivos de las prendas.
    Una vez parseado el archivo de entrada, se procede a recorrer las incompatibilidades recorriendo las prendas y poniéndolas a lavar fijándose si es posible juntarlas o no, o si ya habían sido lavadas.
    Una vez que se tiene el lavado se pasa a eliminar esas prendas del diccionario de incompatibilidades para no volver a recorrerlas y generar un diccionario de soluciones para generar el archivo final

    Otra visión que se tuvo en cuenta y que parecería que se ajusta bien sería tratar el problema como un grafo, de forma que cada nodo sea el numero de prenda,
    el peso de la arista sea el tiempo, y se forme un camino o no según sea compatible.
    Una vez armado el grafo se procedería a usar un algoritmo de camino mínimo, por ejemplo Dijkstra.
    El único inconveniente con esta visión sería que es necesario que el grafo sea conexo, de forma que si una prenda es incompatible con el resto, no podría encontar un camino óptimo.

    Con el primer intento de fuerza bruta, se llegó a un valor óptimo.

# Segunda Parte

    Ahora el objetivo es optimizar dicha solución. Como primera instancia usando la solución ya implementada se corre el archivo nuevo y se verifica el tiempo.
    Podemos observar que el archivo es notablemente más extenso y que el tiempo de ejecución del problema también.

    A primera vista el algoritmo no llega a ninguna solución, tal vez por que el sistema es incompatible.
    Como se mencionó en la entrega anterior, probamos la idea de plantear un grafo y generar una solución calculando el camino más corto posible, y tratando de contemplar casos en que pueda ser incompatible.

    Empezando a probar con una forma de implementar lo anterior, se conlcuye que no es la forma más eficiente de realizar, sino fijarse en las prendas con mayor tiempo y tratar de emparejarlas con la siguiente de más tiempo para tratar que se encuentren en el mismo lavado.

    Este método llega a un resultado no óptimo pero mejor que los que se venía tratando. A continuación se piensa cómo continuar mejorando el algoritmo, tal vez de forma que se ponga en un lavado las prendas con mayor cantidad de tiempo y menor incompatibilidades, para agrupar la mayor cantidad de prendas de mayor tiempo, y ver si se logra un resultado mejor
