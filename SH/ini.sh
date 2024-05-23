#!/bin/bash
# Script para ejecutar un archivo Python pasando el nombre del programa como parámetro

# Verificar si se pasó el nombre del script Python como argumento
if [ -z "$1" ]; then
    echo "No se proporcionó el nombre del script Python."
    exit 1
fi

# Obtener la ruta de la carpeta superior y la subcarpeta
PARENT_DIR="$(dirname "$(pwd)")"
SUBCARPETA="BIN"
PYTHON_SCRIPT="$PARENT_DIR/$SUBCARPETA/$1"

# Verificar si el archivo existe en la subcarpeta de la carpeta superior
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "El archivo $1 no existe en la subcarpeta de la carpeta superior."
    exit 1
fi

# Ejecutar el script Python con la ruta proporcionada y pasar argumentos adicionales
python3 "$PYTHON_SCRIPT" "${@:2}"