# Imagen base liviana de Python
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos dependencias primero (aprovecha caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la app
COPY calculadora_app/ .

# Variable de entorno para UTF-8
ENV PYTHONIOENCODING=utf-8
ENV PYTHONUTF8=1

# Comando por defecto al correr el contenedor
CMD ["python", "calculadora.py"]
