from numpy import zeros
from time import perf_counter
import numpy as np



#Tamaño
N = 1000
A = zeros((N, N))+1
B = zeros((N, N))+2


t1 = perf_counter()
C = A@B
t2 = perf_counter()


dt = t2 - t1

print(f"dt = {dt} s")

#Agregamos la función matmul y la imprimimos en la consola
print("AB =", np.matmul(A,B))
