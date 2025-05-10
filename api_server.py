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
API_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImEyN2Q3Mjk3LWM1OWUtNGExYi05N2M5LThkOGUyOTA1MGNkYyIsImlhdCI6MTc0Njg4ODIzOCwic3ViIjoiZGV2ZWxvcGVyL2M4ZjQyOTU0LTZlNzktYzFiNy1mMTY0LTcyZWY1ODQ5ZTNhMSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM0LjIxMy4yMTQuNTUiXSwidHlwZSI6ImNsaWVudCJ9XX0.8TcsEzjPN4FSxB7wLRBb-yVsBmRatdGbMBlqIeMA6A-QO2qAumjWi5PC0RvFss3ESjfVCyD0__IPFegJBQp4Jw"

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
