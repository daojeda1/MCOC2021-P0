# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:54:54 2021

@author: diego
"""
def archivo(Ns, dt_s, mem_s, libreria, dtype):
    archivo = open("Salida "+str(libreria)+" "+str(dtype)+".txt","w")
    for i in range(10):
        archivo.write("Corrida "+str(i+1)+"\n")
        for j in range(len(Ns)):
            linea = ("N =",Ns[j],"   tiempo transcurrido =",dt_s[i][j],"[seg] ", "   uso memoria total=", mem_s[j], "[bytes] ")
            lin = str(linea)+str("\n")
            archivo.write(lin)
#        archivo.write("Corrida"+str(i))
    archivo.close()


# Ns =[1,10,100,200,300]
# dts = [[0.001, 0.01, 0.1, 1, 10],[0.00001,0.0001,0.001,0.01,0.000000001],[10,0.0001,0.001,0.1,1],[10,0.0001,0.001,0.1,1],[0.00001,0.0001,0.001,0.01,1],[0.00001,0.0001,0.001,0.01,1],[0.00001,0.0001,0.001,0.01,1],[0.00001,0.0001,0.001,0.01,1],[0.00001,0.0001,0.001,0.01,1],[0.00001,0.0001,0.001,0.01,1]]
# mems = [20,40,60,80,100]
# libreria = "numpy"
# dtype = "float16"
# archivo(Ns,dts,mems,libreria,dtype)