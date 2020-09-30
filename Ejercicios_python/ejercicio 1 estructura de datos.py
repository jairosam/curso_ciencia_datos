# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:25:08 2019

@author: jairo
"""

semana = {"domingo":1,"lunes":2,"martes":3}

print(semana)

semana["DOMINGO"]=semana.pop("domingo")
semana["LUNES"]=semana.pop("lunes") 
semana["MARTES"]=semana.pop("martes")

print(semana)

semana["MIERCOLES"]=4

print(semana)
