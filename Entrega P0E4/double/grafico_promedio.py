# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 21:44:58 2021

@author: diego
"""
import matplotlib.pylab as plt
Ns = [1,5,10,20,50,100,200,500,700,1000,2000,3000]
# dt_prom = [0.012816690000181551, 0.00015803000005689682, 8.997999993880512e-05, 0.00015082000008987962, 0.0003461200000856479, 0.000607030000173836, 0.0014463500000601926, 0.00998927000000549, 0.022518330000093557, 0.05306358999996519, 0.3727736500000901, 3.4927746300000764]
dt_prom=[]
libreria = "(I. Inversa y Matmul"
dtype = "float32)"
caso = "I"
casos = ["I","II","III","IV","V","VI","VII","Ib","IIb","IIIb","IVb","Vb"]
def graficar_promedio(Ns, dt_s, libreria, dtype, casos):
        #DANDO FORMATO A LOS GRAFICOS
    # plt.figure(1)
    # plt.subplot(2,1,1)
    plt.title("Grafico Promedio")
    plt.ylabel("Tiempo transcurrido")
    palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
    valor1 = [0.0001,0.001,0.01,0.1,1,10,60,600]
    plt.yticks(valor1,palabras1) 
    plt.xticks(Ns, [])
    
    lista_dt_prom = []
    inpu = []
    for caso in casos:
        dt_prom = open("Datos Promedio Caso "+str(caso)+".txt")
        for linea in dt_prom:
            inpu.append(float(linea))
        lista_dt_prom.append(inpu)
        inpu=[]
########################################################################
    for i in range(len(casos)): #IMPORTANTE######################################################################
        plt.loglog(Ns, lista_dt_prom[i],marker='o',label=casos[i]) #IMPORTANTE###################################################
        plt.legend(loc="upper right")
########################################################################
    n3xlabel = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    plt.xticks(n3xvalue, n3xlabel,rotation=45) #############
    plt.xlabel("Tamaño matriz N")
    plt.yticks(valor1,palabras1) 
    plt.xticks(Ns, [])
    
    n3xlabel = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    plt.xticks(n3xvalue, n3xlabel,rotation=45) #############
    plt.xlabel("Tamaño matriz N")
    # input = []
    # for i in casos:
    #     caso = i
    #     dt_prom = open("Datos Promedio Caso "+str(caso)+".txt")
    #     lista_dt_prom = []
    #     for linea in dt_prom:
    #         lista_dt_prom.append(dt_prom.readline())
    #     input.append(lista_dt_prom)
    #     lista_dt_prom = []
    # #SACAR EL PROMEDIO HACIA ABAJO DE DT_S
    # for i in range(len(casos)):#YA NO ES 10, AHORA ES EL NUMERO DE SCRIPTS
    #     plt.loglog(Ns, dt_s,marker='o')


    plt.savefig("Grafico Promedio.jpg")  
    
#Aca tengo que leer el archivo que me tiro el script, 
#meter la info en la primera linea de la una nueva matriz de tiempos
#en la que las columnas son el numero de Ns y las filas son el caso especifico de script
#luego graficar algo del estilo [CLARAMAENTE EN UN FOR]
#plt.loglog(Ns,listanueva[i],marker='o')
# dt_prom = open("Datos Promedio Caso"+str(caso)) #Solo debo importar la lista con la informacion promedios de cada archivo
graficar_promedio(Ns, dt_prom, libreria, dtype, casos)