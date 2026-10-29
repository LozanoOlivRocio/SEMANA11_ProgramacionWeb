from fastapi import FastAPI
from .apis.estudiante_api import rutasEstudiante

app = FastAPI()

app.include_router(rutasEstudiante, prefix='/api')
