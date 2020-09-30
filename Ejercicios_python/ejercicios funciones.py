# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:05:30 2019

@author: jairo
"""

#%%
#ejercicio 1
resta=lambda a,b:a-b
print(resta(1,2))
#%%
#ejercicio 2
funcion=lambda cadena:cadena.lower()
print(funcion("HOLA"))
#%%
#ejercicio 3
def operacion(cadena,a,b):
    if cadena=="suma":
        return a+b
    elif cadena=="resta":
        return a-b
    else:
        return "entrada no valida"

print(operacion("suma",2,3))
print(operacion("resta",2,3))
print(operacion("no valido",2,3))
#%%
#ejercicio 4

def contraria(frase):
    lista=frase.split(" ")
    lista.reverse()
    frase_nueva=""
    for palabra in range(len(lista)):
        frase_nueva=frase_nueva+lista[palabra]+" "
    return frase_nueva

print(contraria("hola mundo"))

#%%
#ejercicio 5

def palindroma(frase):
    sin_espacios=frase.replace(" ","")
    largo=len(sin_espacios)
    if largo % 2==0:
        for letra in range(largo/2):
            if sin_espacios[letra]==sin_espacios[largo-1-letra]:
                pass
            else:
                return "no es palindroma"
        return "es palindroma"
    else:
        for letra in range((largo-1)/2):
            if sin_espacios[letra]==sin_espacios[largo-1-letra]:
                pass
            else:
                return "no es palindroma"
        return "es palindroma"    

print(palindroma("dabale arroz a la zorra el abad"))        

#%%
lista=[
       [1,2,3,321,321],
       [4,5,6,123],
       [7,8,9,10]
       ]
def funcion(lista_inicial):
    lista_simple=[]
    for lista in lista_inicial:
        for elemento in lista:
            lista_simple.append(elemento)
    return lista_simple

print(funcion(lista))
    
#%%