"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    # 1. Usamos un diccionario para acumular la suma por cada letra de la columna 1.
    # Clave: Letra de la columna 1 (ej: 'A').
    # Valor: Suma acumulada de los valores de la columna 5 para esa letra.
    sumador_por_letra_col1 = {}

    # 2. Abrimos y leemos el archivo.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos la línea en sus columnas.
            columnas = linea.strip().split('\t')
            
            # 3. Extraemos la clave principal de esta línea.
            letra_clave = columnas[0]
            
            # 4. Procesamos la columna 5 para obtener la suma de sus valores para ESTA LÍNEA.
            cadena_col5 = columnas[4]
            suma_linea_actual = 0
            
            # Separamos los pares clave:valor (ej: 'aaa:1', 'bbb:5', ...).
            lista_de_pares = cadena_col5.split(',')
            
            # Iteramos sobre cada par para extraer y sumar su valor numérico.
            for par in lista_de_pares:
                # 'aaa:1' -> .split(':') -> ['aaa', '1'] -> [1] -> '1'
                valor_numerico_str = par.split(':')[1]
                # Sumamos el valor convertido a entero.
                suma_linea_actual += int(valor_numerico_str)
            
            # 5. Acumulamos la suma de esta línea en nuestro diccionario principal.
            if letra_clave in sumador_por_letra_col1:
                # Si la letra ya existe, le añadimos la suma que acabamos de calcular.
                sumador_por_letra_col1[letra_clave] += suma_linea_actual
            else:
                # Si es la primera vez que vemos esta letra, la inicializamos con la suma de esta línea.
                sumador_por_letra_col1[letra_clave] = suma_linea_actual

    # 6. Ordenamos el diccionario final por clave para que coincida con la respuesta.
    resultado_ordenado = dict(sorted(sumador_por_letra_col1.items()))
    
    # 7. Retornamos el diccionario.
    return resultado_ordenado
print(pregunta_12())