FROM python:3.9-slim

WORKDIR /app

# Instalar solo las dependencias necesarias
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY app.py .
COPY .env .

# Variables de entorno para optimizar memoria
ENV MALLOC_TRIM_THRESHOLD_=100000
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Exponemos el puerto dinámico
ENV PORT=10001
EXPOSE $PORT

# Comando para ejecutar la aplicación
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 app:app