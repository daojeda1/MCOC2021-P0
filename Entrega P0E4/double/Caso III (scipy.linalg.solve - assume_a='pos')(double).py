# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:51:50 2021

@author: diego
"""
from vector_b import b
from time import perf_counter
from laplaciana import laplaciana
from scipy.linalg import eigh, inv
from scipy import linalg
from numpy import float16, float32,float64
from graficador import graficar
from archivo import archivo
from numpy import matrix, transpose, mean
# from Graficador import graficar
# from Archivo import archivo

dts = []
dt_inv_temporal = []
mems = []
libreria = "(Caso III - scipy.linalg.solve "
dtype = "float32)"
caso = "III"


Ns = [1,5,10,20,50,100,200,500,700,1000,2000,3000]
for i in range(10):
    for N in Ns:
        t1= perf_counter()
        A= laplaciana(N, dtype = float32)
        t2=perf_counter()
        Am1 = inv(A)
        t3=perf_counter()
        B = b(N,dtype = float32)
        t4=perf_counter()
        x = linalg.solve(A,B,assume_a='pos')
        t5=perf_counter()
        
        dt_ensamblaje_A = t2-t1
        dt_inversion_A = t3-t2
        dt_solve = t5-t2
        bytes_total = A.nbytes + Am1.nbytes + B.nbytes + x.nbytes
        dts.append(dt_solve)
        mems.append(bytes_total)

mem_s = []
for i in range(len(Ns)):
    mem_s.append(mems[i])


dt_s = []

    
def split_list(lst, n):  
    for i in range(0, len(lst), n): 
        yield lst[i:i + n] 

dt_s = list(split_list(dts, len(Ns))) 
###################################################################################
#ESTE PEDAZO DE CODIGO SACA EL PROMEDIO DE CADA COLUMNA Y LOS APPEND EN UNA NUEVA LISTA
dt_prom = []

jex = matrix(dt_s)
transpuesta = transpose(jex)
for i in range(len(transpuesta)):
    cex = mean(transpuesta[i])    
    dt_prom.append(cex)
# print(dt_prom)
# print(list(dt_prom))

archivo_dts = open("Datos Promedio Caso "+str(caso)+".txt","w")
for i in range(len(dt_prom)):
    lin= (str(dt_prom[i])+"\n")
    archivo_dts.write(lin)
archivo_dts.close()
############################################################################
graficar(Ns, dt_s, mem_s, libreria, dtype)
# archivo(Ns,dt_s,mem_s,libreria,dtype)