## Análisis del problema:

Se trata de un problema de Armado en donde una lavandería tiene prendas que destiñen y son incompatibles con otras, teniendo un tiempo de lavado de determinado cada una.

## Objetivo:

Se quiere minimizar el tiempo de lavado de todas las prendas respetando las incompatibilidades entre prendas.

## Modelo:

### Hipótesis:

Los tiempos de cada prenda son constantes

### Variables:

Y<sub>il</sub> : Prenda i usada en el lavado l (Bivalente, 1 para usada, 0 para no usada en el lavado i)

T<sub>i</sub> : Tiempo de la prenda i (constante)

### Resolución

Si por ejemplo tomamos archivo vemos que la prenda 1 no es compatible con la prenda 10. Basados en eso sabemos que no queremos que se encuenttren en el mismo lavado por lo que:

$$\sum Y_{1l} + Y_{10l} = 0 $$
$$\sum Y*{2l} + Y*{19l} = 0 $$

Hacemos lo mismo y para todas las prendas y sus otras prendas incompatibles

$$ L1= \sum*{1, cant prendas} Y*{i1} $$

Quiero que si la prenda i está en el lavado l tome valor, sino sea 0:

Ahora es necesario encontrar el tiempo máximo de ese lavado:
Para el lavado 1:

    T2 <= T1 <= T2 + M (1- Y2)
    T3 <= T1 <= T3 + M (1 - Y3)
    T3 <= T1 <= T3 + M (1 - Y3)
    Y2 + Y3 + Y4 = 1

MIN (FUNC Z) = $\sum $
