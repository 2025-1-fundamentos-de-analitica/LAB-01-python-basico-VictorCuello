"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    agrupador_por_numero = {}

    # 2. Abrimos y leemos el archivo.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos cada línea en sus columnas.
            columnas = linea.strip().split('\t')
            
            # Extraemos los datos que nos interesan.
            letra = columnas[0]
            # Convertimos el valor de la columna 2 a entero para usarlo como clave.
            valor = int(columnas[1])
            
            # 3. Llenamos nuestro diccionario.
            if valor in agrupador_por_numero:
                # Si el número (clave) ya existe, añadimos la letra a su lista.
                agrupador_por_numero[valor].append(letra)
            else:
                # Si es la primera vez que vemos este número, creamos una nueva
                # entrada con el número como clave y una lista con la letra como primer elemento.
                agrupador_por_numero[valor] = [letra]

    # Al final del bucle, el diccionario estará completo.
    # Ej: { 3: ['A', 'B', 'D', ...], 0: ['C'], 1: ['E', 'B', 'E'], ... }
    # Nota: El diccionario no está ordenado por clave en este punto.

    # 4. Convertimos el diccionario en la lista de tuplas ordenada que se pide.
    # .items() convierte el diccionario en una lista de pares (clave, valor).
    # sorted() ordena esta lista. Por defecto, ordena por el primer elemento de cada par,
    # que es la clave (el número), ¡justo lo que necesitamos!
    resultado_final = sorted(agrupador_por_numero.items())

    # 5. Retornamos la lista ordenada.
    return resultado_final
print(pregunta_07())
