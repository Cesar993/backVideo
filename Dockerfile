# Usa una imagen base que ya incluya ffmpeg
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Instala ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copia el contenido de tu aplicación
COPY . /app

# Instala las dependencias
RUN pip install -r /app/requirements.txt

# Define el comando de inicio

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
