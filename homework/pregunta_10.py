"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    # 1. Creamos una lista vacía para almacenar los resultados.
    # No necesitamos un diccionario porque no estamos agrupando, solo transformando.
    resultado_final = []

    # 2. Abrimos y leemos el archivo línea por línea.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos la línea en sus columnas.
            columnas = linea.strip().split('\t')
            
            # 3. Extraemos la información necesaria de cada línea.
            
            # a) La letra de la columna 1 (índice 0).
            letra = columnas[0]
            
            # b) La cadena de la columna 4 (índice 3), ej: "C,A,D"
            cadena_col4 = columnas[3]
            # Contamos sus elementos separándolos por la coma y obteniendo la longitud de la lista.
            # "C,A,D" -> .split(',') -> ['C', 'A', 'D'] -> len() -> 3
            cantidad_elementos_col4 = len(cadena_col4.split(','))
            
            # c) La cadena de la columna 5 (índice 4), ej: "aaa:1,bbb:2"
            cadena_col5 = columnas[4]
            # La lógica es la misma: los elementos están separados por comas.
            # "aaa:1,bbb:2" -> .split(',') -> ['aaa:1', 'bbb:2'] -> len() -> 2
            cantidad_elementos_col5 = len(cadena_col5.split(','))
            
            # 4. Creamos la tupla con los datos procesados de esta línea.
            tupla_linea = (letra, cantidad_elementos_col4, cantidad_elementos_col5)
            
            # 5. Añadimos la tupla a nuestra lista de resultados.
            resultado_final.append(tupla_linea)
            
    # 6. Retornamos la lista completa de tuplas.
    return resultado_final
print(pregunta_10())