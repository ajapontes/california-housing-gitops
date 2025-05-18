"""
Entrena un modelo de regresión lineal con el dataset de California Housing.
Guarda el modelo entrenado y muestra métricas de evaluación.
"""

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from utils import calcular_metricas

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'housing_clean.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'modelo_regresion.pkl')

# Crear carpeta del modelo si no existe
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

# Cargar datos
df = pd.read_csv(DATA_FILE)

# Separar features y target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Dividir en entrenamiento y prueba (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar y entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir y evaluar
y_pred = modelo.predict(X_test)
mae, rmse, r2 = calcular_metricas(y_test, y_pred)

# Mostrar métricas
print("📊 Evaluación del modelo de regresión lineal:")
print(f"MAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²  : {r2:.4f}")

import json

# Guardar el modelo
joblib.dump(modelo, MODEL_PATH)

# Guardar el orden de columnas
columns_path = os.path.join(os.path.dirname(MODEL_PATH), "columns.json")
with open(columns_path, "w") as f:
    json.dump(X.columns.tolist(), f)

print(f"✅ Modelo guardado en: {MODEL_PATH}")
print(f"📄 Columnas guardadas en: {columns_path}")
