# MCOC2021-P0

# Mi computador principal

* Marca/modelo: HP 240 G4
* Tipo: Notebook
* Año adquisición: 2017
* Procesador:
  * Marca/Modelo: Intel Core i3-5005U
  * Velocidad Base: 2.00 GHz
  * Velocidad Máxima: 2.40 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 2
  * Arquitectura: x86_64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
* Tamaño de las cachés del procesador
  * L1d: 32KB
  * L1i: 32KB
  * L2: 256KB
  * L3: 8192KB
* Memoria 
  * Total: 4 GB
  * Tipo memoria: DDR3
  * Velocidad 1867 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Intel HD Graphics 5500
  * Memoria dedicada: 2133 MB
  * Resolución: 1366 x 728
* Disco 1: 
  * Marca: Samsung
  * Tipo: HDD
  * Tamaño: 1TB
  * Particiones: 2
  * Sistema de archivos: EXT4, swap
* Disco 2: 
  * Marca: Kingston
  * Tipo: SSD
  * Tamaño: 256 GB
  * Particiones: 1
  * Sistema de archivos: EXT4
* Disco 3: 
  * NO TIENE
  
* Dirección MAC de la tarjeta wifi: 62-6D-C7-DC-19-17
* Dirección IP (Interna, del router): 192.168.100.1
* Dirección IP (Externa, del ISP): 181.43.37.115
* Proveedor internet: Entel fibra optica


######################################################################################################################################################################

# "Desempeño MATMUL"


![image](https://user-images.githubusercontent.com/53507891/128485611-0d393343-f0d3-4804-9506-67a739a40481.png)

* El archivo txt con los resultados se encuentra en el repositorio

a) ¿Cómo difiere del gráfico del profesor/ayudante?

A grandes rasgos es un gráfico muy similar, sin embargo, nos podemos percatar de que el tamaño de la memoria RAM del profesor es notablemente mayor a la de mi computador, la cual posee 4 GB. Por otro lado, tambien nos podemos percatar que el valor de N para el cual mi computador llega a su limite es bastante menor a la del profesor, lo cual, claramente se deriva de las diferencias de RAM recien mencionadas entre otros motivos.

b) ¿A qué se pueden deber las diferencias en cada corrida?

El computador está constantemente realizando procesos, por lo tanto, es posible que en algunos instantes utilice distintas memorias para realizar el proceso debido a que el procesador se ocupo/desocupo con algun otro proceso y este usando ya sea el disco duro (mas lento), la ram (lo más común) o incluso la memoria cache (más rápido).

c) El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

Porque el tamaño de información a procesar es constante, por lo tanto el uso de información es constante y como vamos variando el valor de N en forma creciente, el grafico inferior por lo tanto será lineal. El tiempo transcurrido no es constante porque la velocidad de procesamiento del computador es variable (el motivo fue explicado en la pregunta anterior) por lo tanto, no será lineal el grafico del tiempo transcurrido.

d) ¿Qué versión de python está usando?

Python 3.8

e) ¿Qué versión de numpy está usando?

Numpy 1.19.2

f) Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 


![image](https://user-images.githubusercontent.com/53507891/128484506-719dc3eb-7160-42fb-ba26-a5e90d2fc068.png)


En cuanto a procesadores, claramente se utiliza solo intel i3 5005U, sin embargo, si hablaramos de procesos, es claro que se ejecuta más de uno en simultaneo (imagen adjunta)

######################################################################################################################################################################

# "Timing inv Numpy y Scipy"

En la presente entrega se evaluo el desempeño de la función inv, utilizando numpy y scipy, para este ultimo, teniamos la posibilidad de aplicar overwrite o no. Nos pudimos
percatar de que la libreria numpy era bastante más lenta, esto es debido al algrotimo de inversión que utiliza, el cual abordaremos más adelante.

Para la libreria Scipy podemos percatarnos de que al aplicar overwrite=True el codigo corria mas rapido aprovechando de mejor manera la memoria del computador.

Por otro lado se utilizó distintos formatos de numeros (float 16, 32, 64 y 128), sin embargo, no todos estaban disponibles debido a que nos vemos limitados tanto por la libreria
como por las capacidades del computador.

¿Que algoritmos de inversión cree que utiliza cada metodo (ver wiki)? Justifique

Numpy lo que hace es usar factorización LU para resolver una ecuacion del tipo Ax = b, por lo tanto, asi logra encontrar la inversa del problema utilizando herramientas de algebra lineal. Por otro lado Scipy utiliza scipy.linalg.inv y por lo que se pude investigar tiene una herramienta que la ayuda a optimizar (Atlas). Dentro de la misma libreria se encuentra overwrite, la cual puede decidir si se sobreescribir o no la matriz en la memoria, y como se mencionó anterirormente el metodo ow= True es el más eficiente, debido a que usa de forma mas eficiente la memoria RAM del computador.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

El paralelismo corresponde al uso eficiente de los nucleos del computador en forma simultanea, en la siguiente imagen podemos ver como los en este caso 4 nucleos del computado trabajan en forma simultanea para llevar a cabo la tarea solicitada por el programa ejecutandose.

![image](https://user-images.githubusercontent.com/53507891/129987141-3e2ce489-ebe4-4564-804f-4407d506b0af.png)


######################################################################################################################################################################

# "Desempeño de Solve y Eigh"

En terminos de desempeño, podemos ver claramente que el modulo eigh es bastante inferior en velocidad de calculos y por tanto mayor en uso de memoria al modulo solve de scipy, esto se debe a que trabaja de forma más engorrosa y asume menos supuestos, por lo tanto, gasta mas memoria. Por otro lado el modulo solve de scipy es mucho más rapido y más aun a medida que asumimos supuestos tales como que A es positiva o simetrica. Sin embargo nos podemos percatar que el algoritmo más eficiente es el de invertir la matriz A y multiplicarla por el vector b dando asi el resultado de x. Por otro lado al usar un formato de numero más preciso, llegaremos a resultados mas exactos pero a costa de mayor uso en memoria, por esto mismo, es que se crearon 2 graficos de tiempo promedio para todos los algoritmos pedidos y sus variantes, los cuales difieren unicamente en que uno es para float y el otro para double, como dije antes, para no mezclar peras con manzanas.

A continuación, podemos ver el gráfico con tiempos promedio de 10 corridas para todos los algoritmos utilizados

 ![Grafico Promedio](https://user-images.githubusercontent.com/53507891/130304962-f4d234c0-b74b-4ede-a39c-4d4d9ab85584.jpg)
 
 La leyenda corresponde a:
 I = Invertir matriz mediante scipy y hacer matmul con el vector b para encontrar x
 II,III,IV,V,VI,VII = Utilizar modulo scipy.linalg.solve con cada una de las posibles variantes del enunciado (overwrite = T or F and assume = sim or pos, etc...)
 Ib,IIb,IIIb,IVb,Vb = Utilizar modulo scipy.linalg.eigh con cada una de las posibles variantes del enunciado (driver = ev, evd, evr, evx and overwrite = T or F))

 ¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? 
 
 Se puede ver perfectamente en el gráfico adjunto anteriormente, en el, podemos ver que el caso Vb es el mas lento, el cual corresponde al modulo eigh, con driver = 'evx' y overwrite_a = False, al parecer el driver exv seria el mas lento de todos, ademas, al no aplicar overwrite, utilizamos mas memoria del computador debido a que no estamos sobrescribiendo la matriz, por lo tanto, es razonable pensar que a mayor uso de memoria, mayor es el tiempo invertido en la solución del sistema.

 ¿Qué algoritmo gana (en promedio) en cada caso? 
 
 Fuera de lo que personalmente creia, el algoritmo que más rapidamente soluciona el sistema es el del caso I, es decir, el que simplemente invierte la matriz A y la multiplica por el vector b usando matmul (@). Cabe destacar, que para no comparar peras con manzanas, se creó un gráfico de N vs Tiempo promedio para los valores en formato double y otro distinto para los valores en formato float, sin embargo, en ambos graficos (adjuntos en la entrega de github) obtuvieron resultados similares todos los algoritmos y aún más importante, el ganador y perdedor fueron los mismos.
 
 ¿Depende del tamaño de la matriz?
 
 Claramente influye el tamaño de la matriz, debido a que requiere mucho mayor uso de memoria RAM una matriz más grande ralentiza el proceso. Se puede ver claramente en el gráfico como es creciente, a mayor valor de N, mayor valor de tiempo [segundos]
 
 ¿A que se puede deber la superioridad de cada opción?
 
 A la simplicidad por una parte, por esto creo que el más veloz es el que solo invierte y aplica matmul entre (A^-1 @ b) para encontrar x. Por otro lado, se debe tambien a las suposiciones que se hagan sobre una matriz A en especifico, si decimos que la matriz es de cierto tipo, le podemos evitar al algoritmo el realizar comprobaciones y solo se pone a trabajar directamente
 
 ¿Su computador usa más de un proceso por cada corrida? ¿Que hay del uso de memoria (como crece)? 
 
 ![image](https://user-images.githubusercontent.com/53507891/130305403-44bb69bb-d195-4e5f-9a22-4113451959fa.png)

Definitiva usa más de un proceso, en la captura de pantalla anterior lo podemos notar, además, podemos ver que está al 100% de su capacidad, mi computador es de 2.00 GHz y en ese momento está trabajando a 1.99 GHz.
El uso de memoria crece junto con el tamaño de la matriz N de forma lineal, sin embargo, es importante destacar que estamos trabajando en un gráfico bilogaritmico, por lo tanto crece de manera lineal pero manteniendo constantes las proporciones, esa es la gracia de este tipo de gráfico

######################################################################################################################################################################

# "Matrices dispersas y complejidad computacional"

```2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)```

Esta linea de codigo utiliza el formato sparse de scipy, lo interesante, es que la matriz es la misma laplaciana de la entrega anterior con "2" en la diagonal principal y con "-1" en las diagonales adyacentes a la principal, solo que el formato es distinto, ya que no considera ninguno de los ceros de la matriz, los cuales representan la mayoria de los datos de nuestro problema y por lo tanto, la mayoria de la memoria que utilizará el computador multiplicando ceros con valores que de antemano sabremos el resultado, por lo tanto, al usar sparse, siguiendo el mismo formato de la matriz laplaciana mencionada, logramos no almacenar los ceros recien mencionados que tanto ralentizan la solucion de nuestro problema. 
Por otro lado, para esta entrega se crean las matrices A y B, las que luego se multiplican usando matmul (@), y podemos notar que si son dispersas, la capacidad del computador aumenta considerablemente, llegando a valores cercanos a los 50 millones para el N mas grande.

######################################################################################################################################################################

# "Matrices dispersas y complejidad computacional (parte 2)"

Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.

Claramente para las matrices llenas, las operaciones son ampliamente más complejas que las dispersas, esto es valido para solve, inv y matmul. Sin embargo, la velocidad a la cual el programa es capaz de crear las matrices necesarias para las operaciones es similar en ambas, siendo algo mas rapido en matrices del tipo sparse pero con diferencias realmente increibles a la hora de trabajarlas en las operaciones matematicas

¿Cual parece la complejidad asintótica (para N→∞)  para el ensamblado y solución en ambos casos y porqué?
1. Matmul:
a) Dispersa: Ensamblado N^3 y Solucion N^3
b) Llena: Ensamblado N^4 y Solucion N^4

2. Solve
4. a) Dispersa: Ensamblado N^3 y Solucion N^3
b) Llena: Ensamblado N^4 y Solucion N^3

3. Inv
a) Dispersa: Ensamblado N^4 y Solucion N^1
b) Llena: Ensamblado N^4 y Solucion N^2

¿Como afecta el tamaño de las matrices al comportamiento aparente?
Al principio, para valores notablemente inferiores a los que el computador es capaz de procesar, nos damos cuenta que el tamaño no afecta de manera muy considerable para el crecimiento de la matriz Ns, sin embargo, a medida que el problema se complejiza en tamaño, podemos ver que puede el tiempo crecer de manera exponencial para solucionar el problema, es decir, si N se duplica, dt (tiempo antes de duplicar N) puede seguir un comportamiento de creciemiento exponencial, para detallarlo en cada tipo, suponiendo una duplicacion en la diagonal de N, tenemos que el nuevo dt puede ser:
Para N duplicado:
O(N) dt(antiguo) = 2dt
O(N^2) dt(antiguo) = 2^2 * dt
O(N^3) dt(antiguo) = 2^3 * dt
O(N^4) dt(antiguo) = 2^4 * dt

Llegando incluso a 16 veces el tiempo para una matriz de tan solo el doble de tamaño

¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
Las corridas son relativamente estables en todos los casos, de esto nos podemos percatar debido a que para todas se grafican 10 corridas distintas en un mismo ploteo y si bien no todas las lineasson iguales, a medida que aumenta el tamaño de N podemos ver como todas se huntan y siguen una misma tendencia (cte, N, N^2, N^3, N^4,). De todas formas, hay una excepcion la cual no se comporto demasiado estable y por lo mismo corri el programa varias veces para ver si habia algun error, estoy hablando del caso INV para matrices dispersas, el cual, luego de analizarlo, me di cuenta de que esto se debe a que para matrices dispersas es notablemente mas rapido la operacion, por lo tanto, no alcanza a verse tan exigida como para que los tiempos de las 10 corridas se alinien en alguna tendencia demarcada con las lineas punteadas. (Adjunto gráfico mencionado)

![Rendimiento Inv Dispersa](https://user-images.githubusercontent.com/53507891/132078150-5d48131a-3ff5-40ce-9284-e02a5c9fc83f.jpg)

Ademas adjunto el caso SOLVE para matrices Llenas, el cual sirve como ejemplo de la estabilidad de las corridas, que si bien no son tan estable en valores pequeños de N, podemos ver como a medida que crece, existe una alineacion de los tiempos y sigue una tendencia de manera mas clara:

![Rendimiento SOLVE Llena](https://user-images.githubusercontent.com/53507891/132078188-6865f7b5-1d97-46da-ab67-1a1b47dad24c.jpg)


Incluya en su README.md el código de ensamblaje de la matriz laplaciana usada por Ud. 

```2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)```

Esta funcion de ensamblaje de la matriz dispersa me di cuenta que probablemente no es la mejor, porque para muchos casos su complejidad es de N^4, la cual, claramente no es la mejor, quizas sea bueno indagar en otras formas de ensamblar la matriz dispersa, que si bien tiene indudables cualidades a la hora de realizar operaciones con ella, en caso de estar mal ensamblada (de una forma poco eficiente), arruina de cierta forma sus caracterisitcas tan beneficiosas



