"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18
    """
    # 1. Usamos un diccionario para llevar la cuenta.
    # La clave será la cadena de tres letras (ej: 'aaa') y el valor será
    # el número de veces que ha aparecido.
    contador_claves = {}

    # 2. Abrimos y leemos el archivo.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos las columnas.
            columnas = linea.strip().split('\t')
            
            # La información está en la columna 5 (índice 4).
            cadena_dict = columnas[4]
            
            # Separamos los pares clave:valor por la coma.
            lista_de_pares = cadena_dict.split(',')
            
            # 3. Recorremos cada par (ej: 'aaa:1').
            for par in lista_de_pares:
                # Solo necesitamos la clave, que es la parte antes de los dos puntos.
                # 'aaa:1' -> .split(':') -> ['aaa', '1'] -> [0] -> 'aaa'
                clave = par.split(':')[0]
                
                # 4. Actualizamos el contador.
                if clave in contador_claves:
                    # Si la clave ya está en el diccionario, le sumamos 1.
                    contador_claves[clave] += 1
                else:
                    # Si es la primera vez que la vemos, la inicializamos en 1.
                    contador_claves[clave] = 1

    # 5. El problema pide retornar el diccionario. No es necesario ordenarlo
    #    a menos que la respuesta de ejemplo esté ordenada. Para que coincida
    #    con la Rta/ del ejemplo, lo mejor es ordenarlo.
    #    Un diccionario no puede estar "ordenado", pero podemos crear uno nuevo
    #    a partir de los items ordenados del anterior.

    # Creamos un diccionario ordenado a partir de los items del contador.
    # sorted(contador_claves.items()) crea una lista de tuplas ('clave', valor) ordenadas por clave.
    # dict(...) convierte esa lista de tuplas de nuevo en un diccionario.
    resultado_ordenado = dict(sorted(contador_claves.items()))

    return resultado_ordenado
print(pregunta_09())