"""
API REST para predecir el valor de viviendas usando un modelo de regresión lineal entrenado.
"""

from flask import Flask, request, jsonify
from predictor import predecir

app = Flask(__name__)

VERSION = "1.0"

@app.route("/")
def home():
    return "API de Predicción de Precios de Viviendas - California Housing"

@app.route("/predict", methods=["POST"])
def predict():
    if request.is_json:
        input_data = request.get_json()
        try:
            resultado = predecir(input_data)
            return jsonify({"prediccion": resultado})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "La solicitud debe ser JSON"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
