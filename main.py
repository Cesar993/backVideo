
#uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
import yt_dlp
import os
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "https://videoappmusica.netlify.app/"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

def descargar_audio(link):
    #Recortar enlace
    posicion_amper = link.find('&')
    linkRecortado = link[:posicion_amper]

    download_folder = str(Path.home() / "Desktop" / "MisAudios")

    if not os.path.exists(download_folder):
        os.makedirs(download_folder) 

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(linkRecortado, download=True)  
        titulo = info_dict.get("title", "audio_temp")  

    return f"{download_folder}/{titulo}.wav"



@app.post("/download_audio/")
async def download_audio(video: VideoRequest):
    file_name = descargar_audio(video.url)
    return {"message": f"Descarga completada: {file_name}"}