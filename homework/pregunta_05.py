"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    agrupador = {}

    # 2. Abrimos y leemos el archivo.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos cada línea por el tabulador ('\t') y eliminamos espacios en blanco.
            columnas = linea.strip().split('\t')
            
            # La letra está en la primera columna (índice 0)
            letra = columnas[0]
            # El valor numérico está en la segunda columna (índice 1).
            # Lo convertimos a entero para poder hacer cálculos.
            valor = int(columnas[1])

            # 3. Agregamos el valor a nuestro diccionario.
            if letra in agrupador:
                # Si la letra ya existe en el diccionario, añadimos el nuevo valor a su lista.
                agrupador[letra].append(valor)
            else:
                # Si es la primera vez que vemos esta letra, creamos una nueva entrada en el diccionario.
                agrupador[letra] = [valor]

    # Al final del bucle, 'agrupador' se verá así:
    # {'A': [5, 9, 2], 'B': [3, 9, 1], ...}

    # 4. Creamos la lista final de resultados.
    resultado = []
    
    # Iteramos sobre el diccionario. Lo ordenamos por clave (letra) para que el resultado
    # salga en orden alfabético ('A', 'B', 'C', ...).
    for letra, lista_valores in sorted(agrupador.items()):
        
        # Usamos las funciones nativas max() y min() para encontrar los valores en la lista.
        valor_maximo = max(lista_valores)
        valor_minimo = min(lista_valores)
        
        # Creamos la tupla con el formato pedido y la añadimos a la lista de resultados.
        tupla_resultado = (letra, valor_maximo, valor_minimo)
        resultado.append(tupla_resultado)

    # 5. Retornamos la lista de tuplas ya ordenada.
    return resultado
print(pregunta_05())