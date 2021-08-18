# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:29:31 2021

@author: diego
"""
from time import perf_counter
from numpy.linalg import inv
from laplaciana import laplaciana
from numpy import float16, float32,float64
from Graficador import graficar
from Archivo import archivo


dts = []
dt_inv_temporal = []
mems = []
libreria = "Numpy"
dtype = "float64"


Ns = [1,5,10,20,50,100,200,500,700,1000,2000,5000]
for i in range(10):
    for N in Ns:
        t1= perf_counter()
        A= laplaciana(N, dtype = float64)
        t2=perf_counter()
        Am1 = inv(A)
        t3=perf_counter()
        
        dt_ensamblaje = t2-t1
        dt_inversion = t3-t2 #ESTE ES EL QUE ME IMPORTA PARA GRAFICAR
        bytes_total = A.nbytes + Am1.nbytes
        dts.append(dt_inversion)
        mems.append(bytes_total)
#LA MEMORIA ESTA EN LA SIGUIENTE LISTA
mem_s = []
for i in range(len(Ns)):
    mem_s.append(mems[i])




dt_s = []

    
def split_list(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

dt_s = list(split_list(dts, len(Ns))) 



#GRAFICAR Y GUARDAR ARCHIVO
graficar(Ns,dt_s,mem_s, libreria, dtype)
archivo(Ns,dt_s,mem_s,libreria,dtype)




#mis outputs son: 
# dt_s = lista de "Ns" columnas por 10 filas
# mem_s = lista de "Ns" columnas
# Ns = lista de "Ns"
# libreria = "numpy", "scipyT", "ScipyF"
