# Dockerfile para una aplicación de Python
# Path: backend/Dockerfile
# Utilizamos la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

#  Instalamos las dependencias
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copiamos el código de la aplicación al directorio de trabajo
COPY . .

# Ejecuta la aplicación
CMD ["python", "app.py"]