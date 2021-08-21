# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 21:20:48 2021

@author: diego
"""
import matplotlib.pylab as plt

def graficar(Ns, dt_s, mem_s, libreria, dtype):
        #DANDO FORMATO A LOS GRAFICOS
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title("Rendimiento Solve"+" "+ str(libreria)+" "+str(dtype))
    plt.ylabel("Tiempo transcurrido")
    palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
    valor1 = [0.0001,0.001,0.01,0.1,1,10,60,600]
    for i in range(10):
        plt.loglog(Ns, dt_s[i],marker='o') #ESTO GRAFICA TODAS LAS LINEAS


    plt.yticks(valor1,palabras1) 
    plt.xticks(Ns, [])
    plt.grid(True)
    
    plt.subplot(2,1,2)
    plt.ylabel("Uso memoria") #Sin unidades pq varian
    plt.loglog(Ns, mem_s,marker='o')
    palabras2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
    valor2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
    plt.yticks(valor2,palabras2)

    n3xlabel = [10,20,50,100,200,500,1000,2000,5000,10000]
    n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000]
    plt.xticks(n3xvalue, n3xlabel,rotation=45) #############
    plt.xlabel("Tamaño matriz N")
    plt.axhline(y=4000000000,xmin=0.0,xmax=Ns[-1],linestyle="--",color='black')
    plt.grid(True)
    plt.savefig("Rendimiento Solve" + " " + str(libreria) +" "+ str(dtype) +".jpg")  
    
    