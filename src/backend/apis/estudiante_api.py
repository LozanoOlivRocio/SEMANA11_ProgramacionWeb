from fastapi import APIRouter, HTTPException, status
from ..services.estudiantes_service import EstudianteServicio
from ..schemas.estudiante import Estudiante, EstudianteActualizar

rutasEstudiante  = APIRouter(prefix='/estudiante', tags=['Estudiante'])
estudianteServicio = EstudianteServicio()

@rutasEstudiante.post('/')
def guardarEstudiante(estudianteNuevo: Estudiante):
    try:
        return estudianteServicio.guardarEstudiante(estudianteNuevo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))

@rutasEstudiante.get('/')
def mostrarEstudiante():
    return estudianteServicio.mostrarEstudiantes()

@rutasEstudiante.put('/{id}')
def actualizarEstudiante(id: int, estudianteActualizar: EstudianteActualizar):
    try:
        return estudianteServicio.actualizarEstudiante(id, estudianteActualizar)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@rutasEstudiante.delete('/{id}')
def eliminarEstudiante(id: int):
    try:
        return estudianteServicio.eliminarEstudiante(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    
