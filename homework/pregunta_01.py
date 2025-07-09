"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_01():
    suma = 0
    with open("files/input/data.csv", "r", encoding="UTF-8") as datos:
        for linea in datos:
            dato = linea.split("\t")
            suma = suma + int(dato[1])
    
    return suma

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
#print(pregunta_01())
