def leer_csv(PATH, HEAD, DELIMITER, READ_LINES):
    with open(PATH, 'r') as archivo:
        # Si tiene cabecera, leerla
        if HEAD == 'True':
            encabezados = archivo.readline().strip().split(DELIMITER)
        else:
            # Si no tiene cabecera, asignar nombres de columna como col0, col1, ...
            primera_linea = archivo.readline().strip().split(DELIMITER)
            encabezados = ['col{}'.format(i) for i in range(len(primera_linea))]

        # Reiniciar la lectura al principio del archivo si no tiene cabecera
        if HEAD == 'False':
            archivo.seek(0)

        # Leer y mostrar la línea especificada si READ_LINES es 'True'
        if READ_LINES == 'True':
            while True:
                linea_numero = input("Ingrese el número de línea que desea leer (o 'q' para salir): ")
                if linea_numero.lower() == 'q':
                    break
                try:
                    linea_numero = int(linea_numero)
                    archivo.seek(0)  # Reiniciar la lectura desde el principio
                    if HEAD == 'True':
                        next(archivo)  # Salta la cabecera si existe
                    for _ in range(linea_numero - 1):
                        next(archivo)  # Salta las líneas anteriores
                    linea = next(archivo)
                    valores = linea.strip().split(DELIMITER)
                    linea_dict = {encabezados[i]: valor for i, valor in enumerate(valores)}
                    print(linea_dict)
                except ValueError:
                    print("Ingrese un valor válido.")
                except StopIteration:
                    print("El archivo no tiene suficientes líneas.")
                    break
        else:
            # Si no se desea leer líneas, se lee y muestra todo el contenido
            for linea in archivo:
                valores = linea.strip().split(DELIMITER)
                linea_dict = {encabezados[i]: valor for i, valor in enumerate(valores)}
                print(linea_dict)

print("Configuración de la lectura de CSV:")
opcion = input("¿Qué desea hacer? (1: Leer todo el archivo, 2: Leer líneas específicas): ")

if opcion == '1':
    PATH = input("Ingrese la ruta del archivo CSV: ")
    HEAD = input("¿El archivo CSV tiene cabecera? (True/False): ")
    DELIMITER = input("Ingrese el delimitador del CSV: ")
    leer_csv(PATH, HEAD, DELIMITER, 'False')  # No se leen líneas específicas
elif opcion == '2':
    PATH = input("Ingrese la ruta del archivo CSV: ")
    HEAD = input("¿El archivo CSV tiene cabecera? (True/False): ")
    DELIMITER = input("Ingrese el delimitador del CSV: ")
    leer_csv(PATH, HEAD, DELIMITER, 'True')  # Se leen líneas específicas
else:
    print("Opción no válida.")

#leer_csv(PATH="/Users/vivi/Documents/Python/FILES/datos.csv", HEAD="True", DELIMITER=",", READ_LINES="False")