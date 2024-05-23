# -- coding: utf-8 --
# ==============================
# Programa: Programa creado para leer y manipular un archivo csv
# Descripcion:
# Autor: Viviana Alcaino
# Argumentos de entrada:
# ==============================

## Imports
import sys
#PATH=
#DELIMITER=
#HEAD=(TRUE O FALSE transformado a str)

## Variables globales
# Definir variables globales para los parámetros
parametros = {"PATH": None, "HEAD": None, "DELIMITER": None}

def main():
    global parametros  # Indicar que se está utilizando la variable global

    # Obtener los argumentos de la línea de comandos
    args = sys.argv[1:]  # Ignoramos el primer argumento, que es el nombre del script

    # Iterar sobre los argumentos para asignar los valores a los parámetros
    for arg in args:
        key, value = arg.split("=")
        if key in parametros:
            parametros[key] = value
        else:
            print(f"Parámetro desconocido: {key}")
            return

    # Hacer algo con los parámetros
    print("Valor de PATH:", parametros["PATH"])
    print("Valor de HEAD:", parametros["HEAD"])
    print("Valor de DELIMITER:", parametros["DELIMITER"])

if __name__ == "__main__":
    main()

## Funciones Auxiliares
#PATHa=/Users/vivi/Documents/Python/FILES/datos.csv HEADa=False DELIMITERa=, 

def leer_csv(PATH, HEAD, DELIMITER):
    with open(PATH, 'r') as archivo:
        # Si tiene cabecera, leerla
        print(HEAD)
        if HEAD=='True':
            encabezados = archivo.readline().strip().split(DELIMITER)
        else:
            # Si no tiene cabecera, asignar nombres de columna como col0, col1, ...
            encabezados = ['col{}'.format(i) for i in range(len(archivo.readline().strip().split(DELIMITER)))]

        # Reiniciar la lectura al principio del archivo si no tiene cabecera
        if HEAD=='False':
            archivo.seek(0)

        # Leer y mostrar cada línea
        for linea in archivo:
            valores = linea.strip().split(DELIMITER)
            linea_dict = {encabezados[i]: valor for i, valor in enumerate(valores)}
            print(linea_dict)

    # Ejemplo de uso
    #PATH = PATH
    #tiene_cabecera = False  # Cambiar a True o False según corresponda

opcion = input("Ingrese la opción deseada (1: Leer con cabecera, 2: Leer sin cabecera): ")
if opcion == '1':
    PATH = input("Ingrese la ruta del archivo CSV: ")
    HEAD = 'True'
    DELIMITER = input("Ingrese el delimitador del CSV: ")
    leer_csv(PATH, HEAD, DELIMITER)
elif opcion == '2':
    PATH = input("Ingrese la ruta del archivo CSV: ")
    HEAD = 'False'
    DELIMITER = input("Ingrese el delimitador del CSV: ")
    leer_csv(PATH, HEAD, DELIMITER)
else:
    print("Opción no válida.")
#leer_csv(parametros["PATH"], str(parametros["HEAD"]), parametros["DELIMITER"])


## Cuerpo del programa
#def main():
 #   print("Hello World!")

## Llamada a funcion Main
#if _name_ == "_main_":
#    main()