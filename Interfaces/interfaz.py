#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:28:05 2020

@author: buitrago
"""

from datetime import date, timedelta
from tkinter import *
from Administrador import Calendario
from Administrador import Administrador

def registrar():
    nombre = nombre_text.get()
    year = year_text.get()
    mes = mes_text.get()
    dia = dia_text.get()
    if int(mes) < 12 or int(mes) > 0:
        if int(dia) < 31 or int(dia) > 0:
            if int(year) < 2080 or int(year) > date.today().year:
                fecha = "{}-{}-{}".format(year, mes, dia)
                A.crear_tarea(nombre, fecha)
            else:
                messagebox.showerror("Alerta!!!", "Este año es invalido")
        else:
            messagebox.showerror("Alerta!!!", "Este día es invalido")
    else:
        messagebox.showerror("Alerta!!!", "Este mes es invalido")

def eliminar():
    nombre = nombre_text.get()
    if A.eliminar_tarea(nombre) != None:
        messagebox.showinfo("Alerta!!!", A.eliminar_tarea(nombre))

def alertar():
    c = Calendario()
    tareas = A.lanzar_alerta(c)
    if len(tareas) == 0:
        messagebox.showinfo("No te preocupes!!", "No hay tareas proximas a vencer")
    else:
        for tarea in tareas:
            messagebox.showwarning("tarea proxima a vencer!!!",tarea)

def mostrar_tareas():
    list_tareas.delete(0,END)
    tareas = A.lectura_tareas()
    for tarea in tareas:
        list_tareas.insert(END, "{} <-> {}".format(tarea[0], tarea[1]))

A = Administrador()
C = Calendario()
 
raiz = Tk()
raiz.resizable(0,0)
raiz.title("Gestor de Tareas")


mi_frame = Frame(raiz, width=300, height=600)
mi_frame.pack()

titulo = Label(mi_frame, text="Administrador")   
titulo.grid(row=0, column=1, pady=10)
titulo.config(fg="black", font=("Verdana",16))

nombre = Label(mi_frame, text="Nombre de la tarea:")
nombre.grid(row=1,column=1)

nombre_text = Entry(mi_frame)
nombre_text.grid(row=2,column=1) 

vacio1 = Label(mi_frame)
vacio1.grid(row=3,column=1)

year = Label(mi_frame, text="Año")
mes = Label(mi_frame, text="Mes")
dia = Label(mi_frame, text="Día")

year.grid(row=4, column=0)
mes.grid(row=4, column=1)
dia.grid(row=4,column=2)

year_text = Entry(mi_frame, width=8)
mes_text = Entry(mi_frame, width=8)
dia_text = Entry(mi_frame, width=8)

year_text.grid(row=5, column=0)
mes_text.grid(row=5, column=1)
dia_text.grid(row=5, column=2)

register_button = Button(mi_frame, text="Registrar Tarea", command=registrar)
register_button.grid(row=6,column=1, pady=7.5)

eliminar_button = Button(mi_frame, text="Eliminar Tarea", command=eliminar)
eliminar_button.grid(row=7, column=1, pady=7.5)

alertar_button = Button(mi_frame, text="Alertar!!!", command=alertar)
alertar_button.grid(row=8, column=1, pady=7.5)

subtitulo = Label(mi_frame, text="Lista de tareas")
subtitulo.grid(row=10, column=1, pady=7.5)
subtitulo.config(fg="black", font=("Verdana",12))

actualizar = Button(mi_frame, text="Actualizar lista", command=mostrar_tareas)
actualizar.grid(row=11,column=1)

label_task = Label(mi_frame, text="Nombre-Fecha")

label_task.grid(row=12, column=1)

scroll_vert = Scrollbar(mi_frame,orient=VERTICAL)
scroll_hort = Scrollbar(mi_frame,orient=HORIZONTAL)

list_tareas = Listbox(mi_frame, yscrollcommand=scroll_vert.set,
                      xscrollcommand=scroll_hort.set)

scroll_vert.config(command=list_tareas.yview)
scroll_hort.config(command=list_tareas.xview)

list_tareas.grid(row=13, column=1,sticky="news")
scroll_vert.grid(row=13,column=2,sticky="nsw")
scroll_hort.grid(row=14,column=1,sticky="nswe")

raiz.mainloop()


    

