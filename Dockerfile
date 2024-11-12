# Usa una imagen base que ya incluya ffmpeg
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Instala ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copia el contenido de tu aplicación
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto para Railway
EXPOSE 8000

# Define el comando de inicio
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
