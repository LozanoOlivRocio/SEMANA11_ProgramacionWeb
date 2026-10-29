from ..schemas.estudiante import Estudiante, EstudianteActualizar

class EstudianteRepositorio:
    def __init__(self):
        self.__listaEstudiantes: list[Estudiante] = []

    def guardarEstudiante(self, estudianteNuevo: Estudiante):
        try:
            self.__listaEstudiantes.append(estudianteNuevo)
            return estudianteNuevo
        except Exception as e:
                    raise str(e)

    def mostrarEstudiante(self):
        return self.__listaEstudiantes

    def actualizarEstudiante(self, id: int, estudianteActualizar: EstudianteActualizar):
        try:
            for _, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    valor.nombre = estudianteActualizar.nombre
                    valor.edad = estudianteActualizar.edad
                    valor.correo = estudianteActualizar.correo
                    return valor
            return None
        except Exception as e:
            raise str(e)

    def eliminararEstudiante(self, id: int):
        try:
            for indice, valor in enumerate(self.__listaEstudiantes):
                if valor.id == id:
                    self.__listaEstudiantes.pop(indice)
                    return id
                return None
        except Exception as e:
            raise str(e)
