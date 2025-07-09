"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    # 1. Usamos un diccionario para acumular las sumas.
    # La clave será la letra de la columna 4 (ej: 'a') y el valor será
    # la suma acumulada de los valores de la columna 2 para esa letra.
    sumador_por_letra = {}

    # 2. Abrimos y leemos el archivo.
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            # Separamos la línea en columnas.
            columnas = linea.strip().split('\t')
            
            # 3. Extraemos los datos relevantes de la línea.
            # El valor numérico de la columna 2. ¡Importante convertirlo a entero!
            valor_a_sumar = int(columnas[1])
            # La cadena con las letras de la columna 4.
            cadena_letras = columnas[3]
            
            # 4. Procesamos las letras de la columna 4.
            # Separamos la cadena por comas para obtener una lista de letras.
            # "a,f,c" se convierte en ['a', 'f', 'c']
            lista_de_letras = cadena_letras.split(',')
            
            # 5. Iteramos sobre cada letra de la lista y actualizamos el sumador.
            for letra in lista_de_letras:
                if letra in sumador_por_letra:
                    # Si la letra ya existe en el diccionario, le sumamos el valor de esta línea.
                    sumador_por_letra[letra] += valor_a_sumar
                else:
                    # Si es la primera vez que vemos la letra, la inicializamos con el valor de esta línea.
                    sumador_por_letra[letra] = valor_a_sumar

    # 6. Ordenamos el diccionario por clave para que coincida con la Rta/.
    # sorted(sumador_por_letra.items()) crea una lista de tuplas (clave, valor)
    # ordenadas por la clave (la letra).
    # dict(...) convierte esa lista de tuplas de nuevo en un diccionario.
    resultado_ordenado = dict(sorted(sumador_por_letra.items()))
    
    # 7. Retornamos el diccionario ordenado.
    return resultado_ordenado
print(pregunta_11())