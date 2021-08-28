# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:22:31 2021

@author: diego
"""
import matplotlib.pylab as plt

def graficar(Ns, dt_ens, dt_solv, dtype):
        #DANDO FORMATO A LOS GRAFICOS
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title("Rendimiento"+" "+str(dtype))
    plt.ylabel("Tiempo de ensamblado")
    palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
    valor1 = [0.0001,0.001,0.01,0.1,1,10,60,600]
    n0xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000"]
    n0xvalue = [10,20,50,100,200,500,1000,2000,5000,10000]

    for i in range(10):
        plt.loglog(Ns, dt_ens[i],marker='o') #ESTO GRAFICA TODAS LAS LINEAS
###############################################
    cortes = [3,10,100,400]
    casos = ["O(N)","O(N^2)","O(N^3)","O(N^4)"]
    exp = [1,2,3,4]
    for i in range(len(cortes)):    
        plt.plot([cortes[i],max(Ns)],[dt_ens[0][0]**exp[i],max(dt_ens[-1])],linestyle = "--",label=casos[i]) #IMPORTANTE###################################################
        plt.legend(loc="lower left")
    plt.axhline(y=dt_solv[-1][-1],xmin=0.0,xmax=1000,linestyle="--",color='black', label = "Constante") #CONSTANTE RAM
    plt.legend(loc="lower left")
    plt.axis([0,max(Ns),0.000001,70])
###############################################
    plt.xticks(n0xvalue, [],rotation=45) #############
    plt.yticks(valor1,palabras1) 
    plt.grid(True)
    
    plt.subplot(2,1,2)
    plt.ylabel("Tiempo de solucion") #Sin unidades pq varian
    # plt.loglog(Ns, dt_s,marker='o')
    palabras2 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min","10 min"]
    valor2 = [0.0001,0.001,0.01,0.1,1,10,60,600]
    for i in range(10):
        plt.loglog(Ns, dt_solv[i],marker='o') #ESTO GRAFICA TODAS LAS LINEAS
    # plt.plot([1,Ns[-1]],[dt_solv[0][0],dt_solv[-1][-1]])
    cortes = [3,10,100,400]
    exp = [1,2,3,4]
    for i in range(len(cortes)):    
        plt.plot([cortes[i],max(Ns)],[dt_ens[0][0]**exp[i],max(dt_ens[-1])],linestyle = "--",label=casos[i]) #IMPORTANTE###################################################
        plt.legend(loc="lower left")
    plt.axis([0,max(Ns),0.000001,70])

    # plt.axhline(y=dt_solv[-1][-1],xmin=0.0,xmax=1000,linestyle="--",color='black', label = "Constante") #CONSTANTE RAM
    # plt.legend(loc="lower left")
    plt.yticks(valor2,palabras2)

    n3xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000"]
    n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000]
    plt.xticks(n3xvalue, n3xlabel,rotation=45) #############
    plt.xlabel("Tamaño matriz N")
    # plt.axhline(y=4000000000,xmin=0.0,xmax=Ns[-1],linestyle="--",color='black') #CONSTANTE RAM
    plt.grid(True)
    plt.savefig("Rendimiento" + " "+ str(dtype) +".jpg")  