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

TL<sub>il</sub>: Tiempo de lavado de la prenda i en el lavado l [entera]

Tmax<sub>l</sub> : Tiempo máximo del lavado l [entera]

Ymax<sub>il</sub> : Si la prenda i en el lavado l es el tiempo máximo [bivalente]

L <sub>i</sub> : Lavado i [entera]

### Resolución

Si por ejemplo tomamos archivo vemos que la prenda 1 no es compatible con la prenda 10. Basados en eso sabemos que no queremos que se encuenttren en el mismo lavado por lo que:

$$\sum Y_{1l} + Y_{10l} <= 1 $$
$$\sum Y*{2l} + Y*{19l} <= 1 $$

Hacemos lo mismo y para todas las prendas y sus otras prendas incompatibles

Además me aseguro que una prenda esté en un solo lavado:

$$\sum Y_{1l} = 1 $$
Idem para cada prenda

Defino el Lavado i con la cantidad de prendas que contiene:
$$ L1= \sum*{1, cant prendas} Y*{i1} $$

Quiero que si la prenda i está en el lavado l tome valor, sino sea 0:

TL<sub>il</sub> = T<sub>i</sub> \* Y<sub>il</sub>

Ahora es necesario encontrar el tiempo máximo de ese lavado:
Para el lavado l:

TL <sub>il</sub> <= Tmax<sub>l</sub> <= TL <sub>il</sub> + M(1 - Ymax <sub>il </sub> )

$$\sum Ymax_{il} = 1 $$

$$MIN (FUNC Z) = \sum Tmax_{l} $$  
$ l = 1..cant_lavados$
