## Imports
import sys

file_conf="/Users/vivi/Documents/Python/CONF/conf.properties"

with open(file_conf) as file:
    lines=file.readlines()

variables = {}

for line in lines:
    name, value = line.strip().split("=")
    variables[name] = value

# Accede a las variables de sistema
path_csv = variables.get("PATH")
name_csv= variables.get("FILE_NAME")
delimiter_csv=variables.get("DELIMITER")

print("Ruta:", path_csv)
print("Nombre:", name_csv)
print("Delimitador", delimiter_csv)

## Variables globales
nombre_archivo=path_csv+name_csv
registros = []  
cabecera='S'
## Funciones Auxiliares
class Registro:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

            
def leer_csv(nombre_archivo,delimiter_csv,cabecera):

    # Abrir el archivo CSV
    with open(nombre_archivo, 'r') as archivo:

        if cabecera=='N':
            # Leer la primera línea para determinar el número de columnas
            primera_linea = archivo.readline().strip().split(delimiter_csv)
            num_columnas = len(primera_linea)
            print(num_columnas)
            # Reiniciar el cursor del archivo al principio
            archivo.seek(0)

            # Iterar sobre las líneas del archivo
            for linea in archivo:
                valores = linea.strip().split(delimiter_csv)

                # Crear un diccionario para almacenar los datos de la fila
                fila = {}
                
                # Asignar los valores a las columnas con nombres correlativos col0, col1, ..., colN
                for i in range(num_columnas):
                    columna = f"col{i}"
                    if i < len(valores):
                        fila[columna] = valores[i]
                    else:
                        fila[columna] = None  # Si no hay valor, asignar None
                
                # Agregar la fila al registro
                registros.append(fila)

        if cabecera=='S':
            lineas = archivo.readlines()
            nombres_atributos = lineas[0].strip().split(delimiter_csv)

            for linea in lineas[1:]:
                valores = linea.strip().split(delimiter_csv)
                if len(valores) == len(nombres_atributos):
                
                    args = {nombres_atributos[i]: valores[i] for i in range(len(nombres_atributos))}
                
                    registro = Registro(**args)
                    registros.append(registro)
    return registros

if cabecera=='N':
    
    def mostrar_registros(registros):
        for indice, fila in enumerate(registros):
            print(f"Fila {indice}:")
            for columna, valor in fila.items():
                print(f"{columna}: {valor}")
            print()  # Salto de línea entre filas

    # Suponiendo que tienes una función para leer el archivo CSV
    registros = leer_csv(nombre_archivo,delimiter_csv,cabecera)

    # Mostrar los registros en pantalla
   # mostrar_registros(registros)

if cabecera=='S':
    
    def mostrar_registros(registros):
     for fila in registros:
        print("Fila:")
        for columna, valor in fila.items():
            print(f"{columna}: {valor}")
        print("-" * 20)  # Separador entre filas

# Suponiendo que tienes una función para leer el archivo CSV
    registros = leer_csv(nombre_archivo, delimiter_csv,cabecera)

# Mostrar los registros en pantalla
  #  mostrar_registros(registros)
