# -*- coding: utf-8 -*-
# ==============================
# Programa              : csv_ingestor.py
# Version               : Version 2
# Descripcion           : lectura de un archivo csv
# Autor                 : Viviana Alcaino
# Argumentos de entrada : PATH, HEAD, DELIMITER
# ==============================

## Imports
import os, sys, datetime

## Variables globales
parametros = {"--path": None, "--head": None, "--delimiter": None}
args = sys.argv[1:]  # Ignoramos el primer argumento, que es el nombre del script
# Obtener la ruta absoluta del archivo log en relación con el directorio de scripts
path_py = os.path.abspath(os.path.dirname(__file__))
ruta_principal = os.path.abspath(os.path.join(path_py, os.pardir))
filepath=ruta_principal + '/LOGS/csv_ingestor_{0}_{1}.log'.format(os.getlogin(), datetime.datetime.now().strftime("%Y%m_%d %H_%M"))
#Obtengo fecha y hora para escribir en el log
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

## =================================================== ##
## Funciones Auxiliares
#Funcion para escribir en logfile.log los errores

def write_to_log(msg, filename=filepath):
    log_msg = f"[{timestamp}] {msg}\n"
    with open(filename, 'a') as log_file:
        log_file.write(log_msg)

#Mensaje de --help y funcion
mensaje_ayuda = """
Descripción: Este programa lee un csv, puede tener o no cabecera y puedes elegir la forma de la lectura de su contenido.
    1 para realizar una lectura completa del archivo
    2 para leer alguna o varias filas en particular

Para que pueda funcionar ambas opciones, debe recivir algunos parametros:

Parametros:
    PATH = Define la ruta y el nombre del archivo
    HEAD = Define si el archivo se lee o  no con cabecera, sus valores pueden ser True/False
    DELIMITER = Define que limitador del csv se esta utilizando
"""
#Funcion --help
def mensaje_help():
    print(mensaje_ayuda)

## =================================================== ##
## Cuerpo del programa

#Clase para leer los registros del csv
class Registro:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

#Funcion para leer y validar el csv
def leer_csv(PATH, HEAD, DELIMITER, READ_LINES):
    with open(PATH, 'r') as archivo:
        # Si tiene cabecera, leerla
        if HEAD.lower() == 'true':
            encabezados = archivo.readline().strip().split(DELIMITER)
        else:
            # Si no tiene cabecera, asignar nombres de columna como col0, col1, ...
            primera_linea = archivo.readline().strip().split(DELIMITER)
            encabezados = ['col{}'.format(i) for i in range(len(primera_linea))]

        # Reiniciar la lectura al principio del archivo si no tiene cabecera
        if HEAD.lower() == 'false':
            archivo.seek(0)

        if READ_LINES.lower() == 'true':
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()
            while True:
                lineas_numeros = input("Ingrese el número de línea(s) que desea leer (separados por comas o espacios) (o 'q' para salir): ")
                print() 
                if lineas_numeros.lower() == 'q':
                    break
                try:
                    lineas_numeros = [int(num) for num in lineas_numeros.replace(',', ' ').split()]
                    for linea_numero in lineas_numeros:
                        # Verificar si la línea solicitada está dentro del rango de líneas del archivo
                        if 0 < linea_numero <= len(lineas):
                            linea = lineas[linea_numero - 1]
                            valores = linea.strip().split(DELIMITER)
                            registro = Registro(**{encabezados[i]: valor for i, valor in enumerate(valores)})
                            for key, value in registro.__dict__.items():
                                print(f"{key}: {value}")
                            print()
                        else:
                            print(f"La línea {linea_numero} no existe en el archivo.")
                except ValueError:
                    print("Ingrese un valor de línea válido o q para salir")
        else:
            # Si no se desea leer líneas, se lee y muestra todo el contenido
            for linea in archivo:
                valores = linea.strip().split(DELIMITER)
                registro = Registro(**{encabezados[i]: valor for i, valor in enumerate(valores)})
                for key, value in registro.__dict__.items():
                    write_to_log(str({key}) + ": " + str({value}))
                write_to_log("")  # Agregar una línea en blanco entre cada línea del CSV

## =================================================== ##
## Llamada a funcion Main

if __name__ == "__main__":
    try:
        if '--help' in args:
            mensaje_help()
            sys.exit(0)
        if len(sys.argv) > 1:
            opcion=3
            for arg in args:
                key, value = arg.split("=")
                if key in parametros:
                    parametros[key] = value
            FILE_NAME = str(parametros["--path"])
            PATH=ruta_principal + '/FILES/' + FILE_NAME
            HEAD=parametros["--head"]
            DELIMITER=str(parametros["--delimiter"])
            leer_csv(PATH, HEAD, DELIMITER, 'False')
        else:
            print("Configuración de la lectura de CSV:")
            opcion = input("    ¿Qué desea hacer? (1: Leer todo el archivo, 2: Leer líneas específicas, --help: Para mostrar ayuda): ")
        if opcion == '1':
            FILE_NAME = input("  Ingrese el nombre del archivo CSV: ")
            PATH=ruta_principal + '/FILES/' + FILE_NAME
            HEAD = input("  ¿El archivo CSV tiene cabecera? (True/False): ")
            DELIMITER = input("  Ingrese el delimitador del CSV: ")
            print()
            leer_csv(PATH, HEAD, DELIMITER, 'False')  # No se leen líneas específicas
        elif opcion == '2':
            FILE_NAME = input("  Ingrese el nombre del archivo CSV: ")
            PATH=ruta_principal + '/FILES/' + FILE_NAME
            HEAD = input("  ¿El archivo CSV tiene cabecera? (True/False): ")
            DELIMITER = input("  Ingrese el delimitador del CSV: ")
            print()
            leer_csv(PATH, HEAD, DELIMITER, 'True')  # Se leen líneas específicas
        elif opcion == '--help':
            mensaje_help()
        else:
           raise ValueError("Opción no válida.")
    except Exception as e:
        msg="  ERROR: {0}".format(e) #TO-DO: Definir error 
        print(msg)
        write_to_log(msg)

