"""
Script para descargar el dataset de California Housing desde Kaggle.
Requiere tener el archivo kaggle.json ubicado en la ruta base del proyecto.
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Definir ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE_JSON_PATH = os.path.join(BASE_DIR, 'kaggle.json')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Crear directorio de datos si no existe
os.makedirs(DATA_DIR, exist_ok=True)

# Configurar variable de entorno para autenticación de Kaggle
os.environ['KAGGLE_CONFIG_DIR'] = BASE_DIR

# Descargar dataset desde Kaggle
def descargar_dataset():
    print("📥 Descargando el dataset de Kaggle...")
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('camnugent/california-housing-prices', path=DATA_DIR, unzip=True)
    print("✅ Dataset descargado y descomprimido en:", DATA_DIR)

if __name__ == '__main__':
    descargar_dataset()
