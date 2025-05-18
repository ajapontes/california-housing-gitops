# Imagen base
FROM python:3.10-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar todos los archivos de API (incluyendo el modelo ya copiado)
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de la API
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
