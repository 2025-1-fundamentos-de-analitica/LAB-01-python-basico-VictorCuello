"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    # 1. La agrupación inicial es idéntica a la pregunta anterior.
    # Clave: número (columna 2), Valor: lista de letras (columna 1).
    agrupador_por_numero = {}

    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            valor = int(columnas[1])
            
            if valor in agrupador_por_numero:
                agrupador_por_numero[valor].append(letra)
            else:
                agrupador_por_numero[valor] = [letra]

    # En este punto, 'agrupador_por_numero' tiene listas con letras repetidas.
    # Ej: {1: ['E', 'B', 'E'], 3: ['A', 'B', 'D', 'E', 'E', 'D'], ...}

    # 2. Ahora, procesamos este diccionario para cumplir los nuevos requisitos.
    resultado_final = []
    
    # Iteramos sobre el diccionario ordenado por clave (el número).
    for valor, lista_letras in sorted(agrupador_por_numero.items()):
        
        # 3. Eliminar duplicados y ordenar.
        # a) Convertimos la lista de letras a un 'set'.
        #    Un 'set' por definición no puede tener elementos duplicados.
        #    set(['E', 'B', 'E']) se convierte en {'E', 'B'}.
        letras_unicas_set = set(lista_letras)
        
        # b) Convertimos el 'set' de nuevo a una lista.
        #    list({'E', 'B'}) se convierte en ['E', 'B'] (el orden no está garantizado).
        letras_unicas_lista = list(letras_unicas_set)
        
        # c) Ordenamos alfabéticamente la lista de letras únicas.
        #    sorted(['E', 'B']) devuelve ['B', 'E'].
        letras_ordenadas = sorted(letras_unicas_lista)
        
        # --- Forma compacta de hacer el paso 3 ---
        # letras_ordenadas = sorted(list(set(lista_letras)))

        # 4. Creamos la tupla con el valor y la nueva lista procesada.
        tupla_resultado = (valor, letras_ordenadas)
        resultado_final.append(tupla_resultado)
        
    # 5. Retornamos la lista de tuplas.
    return resultado_final
print(pregunta_08())