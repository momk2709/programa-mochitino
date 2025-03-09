def tabular(opciones, headers):
    """
    Muestra una tabla de menú de opciones.
    :param opciones: Lista de listas con las opciones del menú.
    :param headers: Lista con los encabezados de la tabla.
    """
    # Determinar el ancho máximo de cada columna para garantizar un formato uniforme
    # FOR LOOP PARA DETERMINAR EL ANCHO DE CADA COLUMNA
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *opciones)]
    
    # Función para formatear filas de la tabla con el ancho determinado
    # FOR LOOP PARA FORMATEAR CADA FILA DE LA TABLA
    def format_row(row):
        return " | ".join(str(item).ljust(width) for item, width in zip(row, col_widths))
    
    # Calcular la línea divisoria basada en la suma de los anchos de las columnas y los separadores
    separator = "-" * (sum(col_widths) + 3 * (len(headers) - 1))
    
    # Imprimir la línea divisoria superior
    print(separator)
    
    # Imprimir los encabezados con formato
    print(format_row(headers))
    
    # Imprimir la línea divisoria entre encabezados y datos
    print(separator)
    
    # Imprimir cada fila de la tabla con formato
    # FOR LOOP PARA IMPRIMIR CADA FILA DE LA TABLA
    for row in opciones:
        print(format_row(row))
    
    # Imprimir la línea divisoria final
    print(separator)