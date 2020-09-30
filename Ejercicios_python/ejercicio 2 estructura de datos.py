# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:44:06 2019

@author: jairo
"""

dias_semana={"lunes":1,
             "martes": 2,
             "miercoles": 3,
             "jueves": 4,
             "viernes": 5,
             "sabado": 6,
             "domingo": 7
             }
    
#%%
lista=list(dias_semana.keys())
lista_dias=[]
for dia in lista:
    dias_semana[dia.upper()]=dias_semana.pop(dia)
    for letra in dia:
        if letra == "o" and dia not in lista_dias:
            lista_dias.append(dia)

print(dias_semana)
print(lista_dias)
#%%
