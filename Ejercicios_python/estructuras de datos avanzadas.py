#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:50:15 2019

@author: jairo
"""


#%%
from collections import defaultdict

pokemon_entrenadores_lista = [
        ['Ash', 'Nidorian'],
         ['Ash', 'Charmander'],
         ['Ash', 'Jigglypuff'],
         ['Ash', 'Rattata'],
         ['Ash', 'Pikachu'],
         ['Ash', 'Pidgey'],
         ['Misty', 'Pikachu'],
         ['Misty', 'Squirtle'],
         ['Misty', 'Jigglypuff'],
         ['Misty', 'Rattata'],
         ['Brock', 'Nidorian'],
         ['Brock', 'Charmander'],
         ['Brock', 'Jigglypuff']
]

lista=[]    

for entrenador,pokemon in pokemon_entrenadores_lista:
    lista.append({"entrenador": entrenador, "pokemon":pokemon})
    
#%%
   
from collections import Counter

def contar(frase):
    contador=Counter([letra for letra in frase if letra not in " ,.\n"])
    return contador.most_common(5)
    
print(contar("esterno cleido mastoideo"))
#%%

def jaccard(lista1, lista2):
    union=len(set(lista1).union(set(lista2)))
    interseccion=len(set(lista1).intersection(set(lista2)))
    return interseccion/union

grupo_amigos1 = {"Manuel", "Rodrigo", "Miguel", "Jesus", "Iñigo"}
# tambien se pueden crear con llaves {}
grupo_amigos2 = {"Manuel", "Alejandro", "Fernando", "Antonio", "Lazaro"}

coeficiente=jaccard(grupo_amigos1,grupo_amigos2)
print(coeficiente)

#%%