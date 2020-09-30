#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:08:22 2020

@author: buitrago
"""

from datetime import date, timedelta
from tkinter import messagebox

class Calendario:
    
    def __init__(self):
        self.fecha = date.today()

    def diferencia_de_fechas(self, fecha1, fecha2):
        return fecha1 - fecha2

    def retornar_hoy(self):
        return date.today()

class Administrador:
    
    def verificar_tarea(self, nombre):
        tareas = self.lectura_tareas()
        for registro in tareas:
            if registro[0] == nombre:
                return registro
    
    def crear_tarea(self, nombre, fecha_vencimiento):
        f = open('tareas.txt', 'a')
        if self.verificar_tarea(nombre) != None:
            return "La tarea con nombre {} ya se encuentra registrada".format(nombre)
        f.write('{}&{}\n'.format(nombre, fecha_vencimiento))      
        f.close()            
        
    def eliminar_tarea(self, nombre):
        tareas = self.lectura_tareas()
        registro = self.verificar_tarea(nombre)
        if registro != None:
            tareas.pop(tareas.index(registro))
        else:
            return "La tarea con nombre {} no ha sido creada".format(nombre)
        
        f = open('tareas.txt','w')
        f.write("")
        f.close()
        f = open('tareas.txt','a')
        for registro in tareas:
            f.write('{}&{}\n'.format(registro[0], registro[1]))
        f.close()
    
    def lectura_tareas(self):
        f = open('tareas.txt','r')
        tareas = f.readlines()
        tareas = [registro.replace("\n","").split("&") for registro in tareas]
        f.close()
        return tareas
        
    def lanzar_alerta(self, calendario):
        tareas = self.lectura_tareas()
        fec = []
        for registro in tareas:
            fechas = [int(valor) for valor in registro[1].split('-')]    
            fec.append(date(fechas[0], fechas[1], fechas[2]))
        
        contador = 0
        vencer = []
        for fecha in fec:
            if calendario.diferencia_de_fechas(fecha,date.today()) <= timedelta(days=10):
                vencer.append("la tarea {} esta proxima a vencer {}"
                              .format(tareas[contador][0], tareas[contador][1]))
            contador += 1
        return vencer

#A = Administrador()
#C = Calendario()
#A.crear_tarea("tareas1", "2020-3-3")
#A.crear_tarea("tareas2", "2020-3-3")
#A.crear_tarea("tareas3", "2020-3-3")
#A.crear_tarea("tareas4", "2020-3-3")
#A.crear_tarea("tareas5", "2020-12-9")
#A.eliminar_tarea("tareas1")
#A.lanzar_alerta(C)
#print(A.lectura_tareas())











