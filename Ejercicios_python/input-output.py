#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:29:27 2019

@author: jairo
"""
#%%
def archivo(name_file):
    linea_larga=""
    lista=[]
    with open(name_file) as fname:
        lista=fname.readlines()
        linea_larga=lista[0]
        for palabra in lista:
            if len(palabra)>=len(linea_larga):
                linea_larga=palabra
        return linea_larga
print(archivo("archivo.txt"))

#%%

def devolver(name_file, numero):
    lista=[]
    lista2=[]
    with open(name_file) as fname:
        lista=fname.readlines()
        for palabra in lista:
            lista2.append(palabra.strip("\n"))
        lista_final=lista2[numero:]
    return lista_final

print(devolver("archivo.txt", 1))

#%%

def dict_a_csv(archivo, diccionario):
    claves=list(diccionario.keys())
    items=len(diccionario[claves[0]])
    with open(archivo,"w") as fname:
        fname.write(','.join(claves))
        fname.write("\n")
        for i in range(items):
            fila=",".join([str(diccionario[clave][i]) for clave in claves])
            fname.write(fila)
            fname.write("\n")
            
diccionario={
"nombre": ["Antonio", "Miguel", "Julian", "Andres"],
"edad": [45, 40, 22, 34],
"ciudad": ["Murcia", "Almería", "Barcelona", "Madrid"]
}  
    
dict_a_csv("nombres.csv",diccionario)

#%%
            