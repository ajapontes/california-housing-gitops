"""
Script de limpieza del dataset California Housing.
Este proceso incluye:
- Eliminación de valores nulos
- Conversión de tipos de datos si es necesario
- Guardado del dataset limpio
"""

import os
import pandas as pd

print("🧹 Iniciando limpieza del dataset...")
# Rutas del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_FILE = os.path.join(DATA_DIR, 'housing.csv')
CLEAN_FILE = os.path.join(DATA_DIR, 'housing_clean.csv')

def limpiar_dataset():
    print("🔍 Cargando datos crudos...")
    df = pd.read_csv(RAW_FILE)

    print("🔧 Iniciando proceso de limpieza...")
    print(f"Dimensiones originales: {df.shape}")
    
    # Verificar valores nulos
    missing_values = df.isnull().sum()
    print("Valores faltantes por columna:\n", missing_values)

    # Eliminamos filas con valores nulos (solo 'total_bedrooms' tiene nulos)
    df = df.dropna()

    print(f"Dimensiones después de eliminar nulos: {df.shape}")

    # Verificar tipos de datos
    print("\nTipos de datos:")
    print(df.dtypes)

    # Convertir la columna categórica en variables dummies (One-Hot Encoding)
    df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)

    print(f"\nColumnas finales después de codificación: {df.columns.tolist()}")
    print(f"Dimensiones finales: {df.shape}")
    print("✅ Proceso de limpieza completado.") 
    
    # Guardar dataset limpio
    df.to_csv(CLEAN_FILE, index=False)
    print(f"✅ Dataset limpio guardado en: {CLEAN_FILE}")

if __name__ == '__main__':
    limpiar_dataset()
