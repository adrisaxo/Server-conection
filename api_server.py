from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tu token de Clash of Clans (desde https://developer.clashofclans.com/)
API_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNmNWEzOTc5LTEyMmMtNDJhNC1hZjlhLTYxNDJkODRiMjM2YiIsImlhdCI6MTc0Njg2NjY5Mywic3ViIjoiZGV2ZWxvcGVyL2M4ZjQyOTU0LTZlNzktYzFiNy1mMTY0LTcyZWY1ODQ5ZTNhMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjgzLjM1LjIwNy4yNDYiXSwidHlwZSI6ImNsaWVudCJ9XX0.WR1Uw4kd7xmL_MB_Yov9kec1usGKYW1bU1hGDt9b6l_d4eOwCB-1JQ2mZF6GKXCSTkeFJU866ikFH-oj--cdDw"

# Headers para autenticación
HEADERS = {
    "Authorization": API_TOKEN,
    "Accept": "application/json"
}

@app.get("/clan/{tag}")
def get_clan_info(tag: str):
    tag = tag.replace("#", "%23")  # Escapar el # para URLs
    url = f"https://api.clashofclans.com/v1/clans/{tag}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()
