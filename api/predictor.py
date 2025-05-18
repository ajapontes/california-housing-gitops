import os
import joblib
import pandas as pd
import json

# Ruta del modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'modelo_regresion.pkl')
COLUMNS_PATH = os.path.join(BASE_DIR, 'columns.json')

# Cargar modelo
modelo = joblib.load(MODEL_PATH)

# Cargar columnas esperadas
with open(COLUMNS_PATH, "r") as f:
    column_order = json.load(f)

def predecir(data_json):
    df = pd.DataFrame([data_json])
    df = df.reindex(columns=column_order)  # reordenar columnas
    pred = modelo.predict(df)[0]
    return round(pred, 2)
