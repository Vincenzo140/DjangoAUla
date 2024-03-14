from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configurando o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    Sensor: bool
    Botao: bool
    LigaRobo: bool
    ResetContador: bool
    ValorContagem: int


@app.post("/receive-data/")
async def receive_data(sensor_data: SensorData):
    # Aqui você pode manipular os dados recebidos como desejar
    return {"message": "Data received successfully", "data": sensor_data.dict()}
