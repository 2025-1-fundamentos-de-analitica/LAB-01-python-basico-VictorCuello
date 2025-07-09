"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    
    """
    dict_letras = {}

    with open("files/input/data.csv", "r") as data:
        for linea in data:
            letra = linea.split("\t")[0]
            if letra in dict_letras:
                dict_letras[letra] += 1
            else:
                dict_letras[letra] = 1

    result = list(dict_letras.items())
    result.sort()
    return result

#print(pregunta_02())


