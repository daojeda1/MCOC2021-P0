# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 22:55:18 2021

@author: diego
"""
from time import perf_counter
from numpy import zeros, float32
import matplotlib.pylab as plt
archivo = open("Salida.txt","w")
dts = []
mems = []

Ns = [1,4,10,16,20,35,49,50,75,100,125,150,250,500,700,750,1000,2000,5000]#10000]
for N in Ns:
    
    uso_memoria = 0

    A = zeros((N,N), dtype=float32)+1
    uso_memoria_teorico = 4*N*N #bytes
    uso_memoria_numpy = A.nbytes
    
    B = zeros((N,N), dtype=float32)+2    
    
    t1= perf_counter()
    C = A@B
     
    t2= perf_counter()
    
    uso_memoria_total = A.nbytes + B.nbytes + C.nbytes
    dt = t2-t1
    
    dts.append(dt)
    mems.append(uso_memoria_total)
    linea = ("N =",N,"   tiempo transcurrido =",dt,"[seg] ", "   uso memoria total=", uso_memoria_total, "[bytes] ", "   flops =", (N**3/dt), "[flops/seg]")
    lin = str(linea)+str("\n")
    archivo.write("Corrida 1")
    archivo.write(lin)
archivo.write("\n")


#Grafico el tiempo versus el valor de N
plt.figure(1)
plt.subplot(2,1,1)
plt.loglog(Ns, dts,marker='o')

plt.title("Rendimiento A@B")
plt.ylabel("Tiempo transcurrido") #No está unicamente en segundos pq varian

######################################################

aux=0
while aux <9:
    d_ts = []
    m_ems = []
    Ns = [1,4,10,16,20,35,49,50,75,100,125,150,250,500,700,750,1000,2000,5000]#,10000]
    for n in Ns:
        
        usomemoria = 0

        a = zeros((n,n), dtype=float32)+1
        usomemoriateorico = 4*n*n #bytes
        usomemorianumpy = a.nbytes

        b = zeros((n,n), dtype=float32)+2    
        
        t_1= perf_counter()
        c = a@b
         
        t_2= perf_counter()
        
        usomemoriatotal = a.nbytes + b.nbytes + c.nbytes

        d_t = t_2-t_1
        
        d_ts.append(d_t)
        m_ems.append(usomemoriatotal)
#        archivo.write("\n")
        escr = ("N =",n,"   tiempo transcurrido =",d_t,"[seg] ", "   uso memoria total=", usomemoriatotal, "[bytes] ", "   flops =", (n**3/d_t), "[flops/seg]")
        escribe = str("Corrida")+str(aux+2)+str(escr)+str("\n")
        archivo.write(escribe)
    archivo.write("\n")
    plt.loglog(Ns, d_ts,marker='o')
    aux+=1


###Fin ciclo para graficar 10 veces

#A continuación damos formato a los ejes del primer graficopalabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
palabras1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
valor1 = [0.0001,0.001,0.01,0.1,1,10,60,600]
plt.yticks(valor1,palabras1) 
plt.xticks(Ns, [])
#######################################################


plt.grid(True)
    
plt.subplot(2,1,2)
plt.ylabel("Uso memoria") #Sin unidades pq varian
plt.loglog(Ns, mems,marker='o')
palabras2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
valor2 = [1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
plt.yticks(valor2,palabras2)
n3xlabel = [10,20,50,100,200,500,1000,2000,5000,10000]
n3xvalue = [10,20,50,100,200,500,1000,2000,5000,10000]
plt.xticks(n3xvalue, n3xlabel,rotation=45) #############
plt.xlabel("Tamaño matriz N")
plt.axhline(y=4000000000,xmin=0.0,xmax=Ns[-1],linestyle="--",color='black')
plt.grid(True)
plt.savefig("Rendimiento A@B.jpg")
plt.show()

archivo.close()
