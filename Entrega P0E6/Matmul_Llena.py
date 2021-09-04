# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:11:01 2021

@author: diego
"""
from laplaciana_llena import laplaciana_llena
from numpy import float16
from time import perf_counter
from graficador_llena import graficar

dtsolve= []
dtens = []
xo = perf_counter()
Ns = [1,5,10,20,50,100,200,500,700]#,1000]#,2000]#,3000]#,5000,9000]
for i in range(10):
    for N in Ns:
        t1= perf_counter()
        A= laplaciana_llena(N, dtype = float16)
        B= laplaciana_llena(N, dtype = float16)
        t2=perf_counter()
        x = A@B
        t3=perf_counter()
        
        dt_ensamblaje = t2-t1
        dt_solve = t3-t2
        dtens.append(dt_ensamblaje)
        dtsolve.append(dt_solve)

dt_s = []

    
def split_list(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

dt_ens = list(split_list(dtsolve, len(Ns)))
dt_solv = list(split_list(dtens, len(Ns)))


dtype = "Llena"
graficar(Ns, dt_ens, dt_solv, dtype)
xf = perf_counter()
delta = xf-xo
print("Tiempo Total: ", delta)
