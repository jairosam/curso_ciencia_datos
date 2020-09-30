#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:23:14 2019

@author: jairo
"""

#%%
class Vehiculo:

    def __init__(self, modelo, velocidad_maxima, color="negro"):
        self.color = color
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el coche empieza parado
        
    def describir(self):
        descripcion = "Vehiculo Modelo:{}. Color {}. Velocidad máxima: {}".format(
                self.modelo, self.color, self.velocidad_maxima)
        return descripcion
    
    # El metodo __repr__ es un metodo mágico que se usa cuando queremos representar algo (con el metodo print)
    def __repr__(self):
        return self.describir()

    def describir_estado(self):
        if self.velocidad == 0:
            print("El vehiculo está parado")
        elif self.velocidad > 0:
            print("El vehiculo va a {} kilómetros por hora".format(self.velocidad))
        else:
            print("El vehiculo va marcha atrás {} a kilómetros por hora".format(self.velocidad))
            
    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self, diferencia_velocidad):
        print("Acelerando {} km/h".format(diferencia_velocidad))
        # abs devuelve un numero positivo si es negativo
        self.velocidad += abs(diferencia_velocidad)
        # min devuelve el valor minimo de una lista de números
        self.velocidad = min(self.velocidad, self.velocidad_maxima)

    def frenar(self, diferencia_velocidad):
        print("Frenando {} km/h".format(diferencia_velocidad))
        self.velocidad -= abs(diferencia_velocidad)
        # max nos devuelve el máximo valor de una lista de números
        self.velocidad = max(self.velocidad, -5)

#%%
class Taxi(Vehiculo):
    
    def __init__(self,modelo,velocidad_maxima):
        self.color = "amarillo"
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el coche empieza parado
        self.distancia_recorrido=0
        self.tarifa=3
    
    def cobrar(self):
        return self.tarifa*self.distancia_recorrido
    
    def agregar_distancia(self, distancia):
        self.distancia_recorrido += distancia
        
    def agregar_tiempo(self, tiempo):
        self.agregar_distancia(tiempo*self.velocidad)

taxi=Taxi(modelo="mazda",velocidad_maxima=200)
taxi.acelerar(100) 
taxi.agregar_tiempo(2)
print(taxi.cobrar())
#%%

class Parking:
    
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.vehiculos=[]
    
    def aparcar_coche(self,vehiculo):
        if self.capacidad>len(self.vehiculos) and not type(vehiculo)==Vehiculo:
            print("Estacionando Coche")
            self.vehiculos.append(vehiculo)
        else:
            print("No hay espacio o esta intentando estacionar un carro distinto a un vehiculo")
        
    def verificar(self, vehiculo):
        if vehiculo in self.vehiculos:
            return True
        else:
            return False
    
    def sacar_coche(self, vehiculo):
        if self.verificar(vehiculo)==True:
            print("sacando coche")
            self.vehiculos.pop(self.vehiculos.index(vehiculo))
        else:
            print("el coche no se encuentra aparcado")
    
carro=Vehiculo(modelo="chevrolet",velocidad_maxima=200)
parqueadero=Parking(50)
parqueadero.aparcar_coche(carro)
print(parqueadero.vehiculos)
parqueadero.sacar_coche(carro)        
#%%

