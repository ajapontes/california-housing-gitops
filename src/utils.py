"""
Funciones auxiliares para el entrenamiento y evaluación de modelos.
"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def calcular_metricas(y_true, y_pred):
    """
    Calcula MAE, RMSE y R² para evaluar el modelo.
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2
