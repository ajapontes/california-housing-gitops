"""
Exploración inicial del dataset de California Housing.
Este script carga el archivo housing.csv y muestra estadísticas básicas.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Construir ruta absoluta al archivo housing.csv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'housing.csv')

# Leer archivo CSV
df = pd.read_csv(DATA_PATH)

# Mostrar primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Información general
print("\nResumen del dataset:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Histograma del valor medio de las casas
df["median_house_value"].hist(bins=50, figsize=(10, 5))
plt.title("Distribución del valor medio de las casas")
plt.xlabel("Valor ($)")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()
