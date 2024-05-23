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
parametros = {"PATH": None, "HEAD": None, "DELIMITER": None, "READ_LINES": None}

def main():

    file_conf="/Users/vivi/Documents/Python/CONF/conf.properties"

    with open(file_conf) as file:
        lines=file.readlines()

    variables = {}

    for line in lines:
        name, value = line.strip().split("=")
        variables[name] = value

# Accede a las variables de sistema
    global path_log
    path_log = variables.get("PATH_LOG")
    print("Ruta LOG:", path_log)

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
    print("Valor de READ LINE:", parametros["READ_LINES"])

if __name__ == "__main__":
    main()


## Funciones Auxiliares
#PATHa=/Users/vivi/Documents/Python/FILES/datos.csv HEADa=False DELIMITERa=, 

def leer_csv(PATH, HEAD, DELIMITER, READ_LINES, LOG_FILE=path_log):
    try:
        # Abrir el archivo de registro si se especifica
        if LOG_FILE:
            log = open(LOG_FILE, 'a')  # 'a' para adjuntar al archivo si existe, o crear uno nuevo si no existe
        else:
            log = None

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

                        # Escribir la salida en el archivo de registro si está especificado
                        if log:
                            log.write(str(linea_dict) + '\n')
                    except ValueError:
                        print("Ingrese un número válido.")
                    except StopIteration:
                        print("El archivo no tiene suficientes líneas.")
                        break
            else:
                # Si no se desea leer líneas, se lee y muestra todo el contenido
                for linea in archivo:
                    valores = linea.strip().split(DELIMITER)
                    linea_dict = {encabezados[i]: valor for i, valor in enumerate(valores)}
                    print(linea_dict)

                    # Escribir la salida en el archivo de registro si está especificado
                    if log:
                        log.write(str(linea_dict) + '\n')

        # Indicar que el proceso ha finalizado exitosamente en el archivo de registro
        if log:
            log.write("Proceso finalizado exitosamente.\n")
    except Exception as e:
        # Registrar cualquier excepción que ocurra durante el proceso en el archivo de registro
        if log:
            log.write("Error durante el proceso: {}\n".format(str(e)))
    finally:
        # Cerrar el archivo de registro si está abierto
        if log:
            log.close()


    # Ejemplo de uso
    #PATH = PATH
    #tiene_cabecera = False  # Cambiar a True o False según corresponda
leer_csv(parametros["PATH"], str(parametros["HEAD"]), parametros["DELIMITER"],str(parametros["READ_LINES"]))


## Cuerpo del programa
#def main():
 #   print("Hello World!")

## Llamada a funcion Main
#if _name_ == "_main_":
#    main()