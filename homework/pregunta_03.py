"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    suma_letras = {}

    with open("files/input/data.csv", "r") as data:
        for linea in data:
            dato = linea.split("\t")
            letra = dato[0]
            numero = int(dato[1])
            if letra in suma_letras:
                suma_letras[letra] += numero 
            else:
                suma_letras[letra] = numero            

    result = list(suma_letras.items())
    result.sort()
    return result

print(pregunta_03())