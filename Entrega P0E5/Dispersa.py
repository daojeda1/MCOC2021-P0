# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:11:01 2021

@author: diego
"""
from laplaciana_dispersa import laplaciana_dispersa
from numpy import float16
from time import perf_counter
from graficador_dispersa import graficar
#from numpy import matrix, transpose, mean

# N = 4

# A = laplaciana_llena(N, float32)
# print(A)

# Acsr = sparse.csr_matrix(A)
# Acsc = sparse.csc_matrix(A)
# Acoo = sparse.coo_matrix(A)
# print(Acoo)
dtsolve= []
dtens = []
xo=perf_counter()
Ns = [1,5,10,20,50,100,200,500,700,1000,2000,3000,5000,9000,15000,20000,30000,40000,50000,70000,100000,150000,200000,300000,500000,1000000,2000000,5000000]
for i in range(10):
    for N in Ns:
        t1= perf_counter()
        A= laplaciana_dispersa(N, dtype = float16)
        B= laplaciana_dispersa(N, dtype = float16)
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


# print(dtsolve)
dtype = "Dispersa"
graficar(Ns, dt_ens, dt_solv, dtype)
xf = perf_counter()
delta = xf-xo
print("Tiempo Total: ", delta)
from matplotlib import pyplot as plt
Nss = [1**2,5**2,10**2,20**2,50**2,100**2,200**2,500**2,700**2,1000**2,2000**2,3000**2,5000**2,9000**2,15000**2,20000**2,30000**2,40000**2,50000**2,70000**2,100000**2]
# plt.loglog(Nss,dt_solv[-1])