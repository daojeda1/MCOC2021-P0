# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 21:33:21 2021

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