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
cabecera='N'
## Funciones Auxiliares

class Registro:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def leer_csv(nombre_archivo,delimiter_csv,cabecera):

    # Abrir el archivo CSV
    with open(nombre_archivo, 'r') as archivo:
      lineas = archivo.readlines()
      if cabecera=='N':
        nombres_atributos=["col"+str(i) for i in range(len(lineas[0].strip().split(delimiter_csv)))]
        start=0
      if cabecera=='S':
        nombres_atributos = lineas[0].strip().split(delimiter_csv)
        start=1
      for linea in lineas[start:]:
        valores = linea.strip().split(delimiter_csv)
      if len(valores) == len(nombres_atributos):
        args = {nombres_atributos[i]: valores[i] for i in range(len(nombres_atributos))}
        print(args)
        registro = Registro(**args)
        registros.append(registro)
    return registros


#def mostrar_registros(registros):
# Suponiendo que tienes una función para leer el archivo CSV
registros = leer_csv(nombre_archivo, delimiter_csv,cabecera)
for i, registro in enumerate(registros, 1):
    print(f"Registro {i}:")
    for attr, value in registro.__dict__.items():
        print(f"{attr}: {value}")
    print("-" * 20) # Imprimir línea en blanco entre registros

# Mostrar los registros en pantalla
  #  mostrar_registros(registros)