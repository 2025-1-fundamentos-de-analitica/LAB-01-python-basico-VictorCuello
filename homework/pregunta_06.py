"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    agrupador_valores = {}

    # 2. Abrimos y leemos el archivo línea por línea.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos las columnas por el tabulador.
            columnas = linea.strip().split('\t')
            
            # 3. La información que necesitamos está en la columna 5 (índice 4).
            # Esto nos da una cadena como 'aaa:1,bbb:2,ccc:3'
            cadena_dict = columnas[4]
            
            # 4. Ahora procesamos esta cadena. Primero, la separamos por la coma ','
            # para obtener cada par clave-valor.
            # 'aaa:1,bbb:2,ccc:3' se convierte en ['aaa:1', 'bbb:2', 'ccc:3']
            lista_de_pares = cadena_dict.split(',')
            
            # 5. Recorremos cada par (ej: 'aaa:1') para extraer la clave y el valor.
            for par in lista_de_pares:
                # Separamos el par por el dos puntos ':'.
                # 'aaa:1' se convierte en ['aaa', '1']
                clave, valor_str = par.split(':')
                valor = int(valor_str) # ¡Importante convertir a entero!
                
                # 6. Agregamos el valor al diccionario principal (agrupador_valores).
                if clave in agrupador_valores:
                    # Si la clave ya existe, añadimos el valor a su lista.
                    agrupador_valores[clave].append(valor)
                else:
                    # Si es la primera vez que vemos la clave, creamos la entrada.
                    agrupador_valores[clave] = [valor]
    
    # Al final del bucle, 'agrupador_valores' contendrá todas las claves y sus valores de todo el archivo.
    # Ej: {'aaa': [1, 9, 4, ...], 'bbb': [2, 1, 5, ...], ...}

    # 7. Preparamos la lista final de resultados.
    resultado = []
    
    # 8. Iteramos sobre el diccionario ordenado por clave para generar el resultado final.
    for clave, lista_numeros in sorted(agrupador_valores.items()):
        
        # Usamos las funciones nativas max() y min() sobre la lista de números.
        valor_minimo = min(lista_numeros)
        valor_maximo = max(lista_numeros)
        
        # Creamos la tupla de resultado y la añadimos a la lista.
        tupla_resultado = (clave, valor_minimo, valor_maximo)
        resultado.append(tupla_resultado)

    # 9. Retornamos la lista final.
    return resultado
print(pregunta_06())
