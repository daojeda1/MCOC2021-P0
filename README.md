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



