from ..repositories.estudiante_repository import EstudianteRepositorio
from ..schemas.estudiante import Estudiante, EstudianteActualizar

class EstudianteServicio:
    def __init__(self):
        self.__estudianteRepositorio = EstudianteRepositorio()

    def guardarEstudiante(self, estudianteNuevo: Estudiante):
        return self.__estudianteRepositorio.guardarEstudiante(estudianteNuevo)

    def mostrarEstudiantes(self):
        return self.__estudianteRepositorio.mostrarEstudiantes()

    def actualizarEstudiante(self, id:int, estudianteActualizar: EstudianteActualizar):
        return self.__estudianteRepositorio.actualizarEstudiante(id, estudianteActualizar)

    def eliminarEstudiante(self, id: int):
        return self.__estudianteRepositorio.eliminararEstudiante(id)