
## Imports
import os
import datetime

## Variables globales
filename='../Python/LOGS/logfile.log'
    # Obtener la ruta absoluta del archivo logfile.log en relación con el directorio de scripts
filepath = os.path.abspath(filename)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timestamp)