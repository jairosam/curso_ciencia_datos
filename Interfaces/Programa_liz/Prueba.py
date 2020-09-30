#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:01:50 2020

@author: buitrago
"""


import pandas as pd
import numpy as np
from datetime import date, timedelta

class Gestor:
    
    def __init__(self):
        self.df = pd.DataFrame()
    
    def cargar_archivo(self, archivo):
        self.df = pd.read_excel("{}.xlsx".format(archivo))
        self.df.ODS = self.df.fillna(method='ffill')
        self.df.INICIO.loc[(self.df.INICIO == "-") 
                           | (np.isnan(self.df.INICIO))] = ""
        self.df.FIN.loc[self.df.FIN == "-"] = ""

    def filtrar(self, columna, parametro):
        filtro = self.df.loc[self.df[columna] == parametro,]    
        return  len(filtro), filtro
    
    def registrar(self, ODS, Acto, inicio, fin, dias):
        datos = [ODS, Acto, inicio, fin, dias]
        
    
gestor = Gestor()

gestor.cargar_archivo("Fechas ODS")