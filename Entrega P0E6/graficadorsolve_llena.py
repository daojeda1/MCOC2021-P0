# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:51:38 2021

@author: diego
"""
import matplotlib.pylab as plt

def graficar(Ns, dt_ens, dt_solv, dtype):
        #DANDO FORMATO A LOS GRAFICOS
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title("Rendimiento"+" SOLVE "+str(dtype))
    plt.ylabel("Tiempo de ensamblado")
    palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]#, "10 min"]
    valor1 = [0.0001,0.001,0.01,0.1,1,10,60]#,600]
    n0xlabel = ["10","20","50","100","200","500","1000"]
    n0xvalue = [10,20,50,100,200,500,1000]

    for i in range(10):
        plt.loglog(Ns, dt_ens[i],marker='.',color="black",linewidth=0.5) #ESTO GRAFICA TODAS LAS LINEAS
###############################################

    plt.axhline(y=max(dt_ens[-1]), xmin=0, xmax=max(Ns),linestyle = "--",label="constante") #########
    # plt.legend(loc="lower left")
############################################################################
    casos = ["O(N)","O(N)","O(N^3)","O(N^4)"]
    exp = [1,2,3,4]
    for i in range(4):    
        plt.plot([min(dt_ens[-1]),max(Ns)],[min(dt_ens[-1])**exp[i],max(dt_ens[-1])],linestyle = "--",label=casos[i]) #IMPORTANTE###################################################
############################################################################   
        # plt.legend(loc="lower left")
    # plt.axhline(y=dt_solv[-1][-1],xmin=0.0,xmax=Ns[-1],linestyle="--",color='black', label = "Constante") #CONSTANTE RAM
    # plt.legend(loc="lower left")
    plt.axis([1,max(Ns),0.00001,100])#ACA IMPORTANTE DESCOMENTARjfshdgjrhgoernñoi
###############################################
    plt.xticks(n0xvalue, [],rotation=45) #############
    plt.yticks(valor1,palabras1) 
    # plt.grid(True)
    
    plt.subplot(2,1,2)
    plt.ylabel("Tiempo de solucion") #Sin unidades pq varian
    # plt.loglog(Ns, dt_s,marker='o')
    palabras2 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min"]#, "10 min"]
    valor2 = [0.0001,0.001,0.01,0.1,1,10,60]#,600]
    for i in range(10):
        plt.loglog(Ns, dt_solv[i],marker='.',color="black",linewidth=0.5) #ESTO GRAFICA TODAS LAS LINEAS
    # plt.plot([1,Ns[-1]],[dt_solv[0][0],dt_solv[-1][-1]])
#######################################################################
    plt.axhline(y=max(dt_solv[-1]), xmin=0.1, xmax=max(Ns),linestyle = "--",label="constante") #########
    plt.legend(loc="lower left")
##############################################################################    
    exp = [1,2,3,4]
    for i in range(4):    
        plt.plot([min(dt_solv[-1]),max(Ns)],[min(dt_solv[-1])**exp[i],max(dt_solv[-1])],linestyle = "--",label=casos[i]) #IMPORTANTE###################################################
        plt.legend(loc="lower left")
##############################################################################

    plt.axis([1,max(Ns),0.00001,0.01])
    plt.yticks(valor2,palabras2)

    n3xlabel = ["10","20","50","100","200","500","1000"]#,"2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000"]
    n3xvalue = [10,20,50,100,200,500,1000]#,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000]
    plt.xticks(n3xvalue, n3xlabel,rotation=45) #############
    plt.xlabel("Tamaño matriz N")
    # plt.grid(True)
    plt.savefig("Rendimiento SOLVE" + " "+ str(dtype) +".jpg")  