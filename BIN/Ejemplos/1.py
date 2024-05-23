class Registro:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

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

        # Leer y mostrar las líneas especificadas si READ_LINES es 'True'
        if READ_LINES == 'True':
            while True:
                lineas_numeros = input("Ingrese el número de línea(s) que desea leer (separados por comas o espacios) (o 'q' para salir): ")
                if lineas_numeros.lower() == 'q':
                    break
                lineas_numeros = [int(num) for num in lineas_numeros.replace(',', ' ').split()]
                if HEAD == 'True':
                    next(archivo)  # Salta la cabecera si existe
                for linea_numero in lineas_numeros:
                    archivo.seek(0)  # Reiniciar la lectura desde el principio
                    if HEAD == 'True':
                        next(archivo)  # Salta la cabecera si existe
                    for _ in range(linea_numero - 1):
                        next(archivo)  # Salta las líneas anteriores
                    linea = next(archivo)
                    valores = linea.strip().split(DELIMITER)
                    registro = Registro(**{encabezados[i]: valor for i, valor in enumerate(valores)})
                    for key, value in registro.__dict__.items():
                        print(f"{key}: {value}")
                    print()  # Agregar una línea en blanco entre cada línea del CSV
        else:
            # Si no se desea leer líneas, se lee y muestra todo el contenido
            for linea in archivo:
                valores = linea.strip().split(DELIMITER)
                registro = Registro(**{encabezados[i]: valor for i, valor in enumerate(valores)})
                for key, value in registro.__dict__.items():
                    print(f"{key}: {value}")
                print()  # Agregar una línea en blanco entre cada línea del CSV

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
