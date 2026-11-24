from typing import List, Optional
from models.programa_model import ProgramaModel
from models.entities.programa_estudio import ProgramaEstudio
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException

class ProgramaController:

    """Controlador que orquesta la lógica de negocio para Programas de Estudio."""

    def __init__(self):
        self._modelo_programa = ProgramaModel()


    def obtener_todos(self) -> List[ProgramaEstudio]:

        try:

            return self._modelo_programa.listar_todos()

        except BibliotecaException as error:

            raise error


        except Exception as error_inesperado:

            raise BibliotecaException(f"Falla inesperada al listar programas: {error_inesperado}")




    def buscar_programas(self, criterio_ingresado: str) -> List[ProgramaEstudio]:

        try:

            criterio_limpio = criterio_ingresado.strip() if criterio_ingresado else ""

            if not criterio_limpio:

                return self._modelo_programa.listar_todos()

            return self._modelo_programa.buscar_por_criterio(criterio_limpio)

        except BibliotecaException as error:

            raise error

        except Exception as error_inesperado:

            raise BibliotecaException(f"Falla inesperada al buscar programas: {error_inesperado}")



    def obtener_programa_por_id(self, id_programa: int) -> Optional[ProgramaEstudio]:

        if not id_programa or id_programa <= 0:

            raise ValidacionDatosError("Identificador de programa no válido.")

        return self._modelo_programa.obtener_por_id(id_programa)


    def registrar_programa(self, codigo: str, nombre: str) -> bool:

        cod = codigo.strip().upper()
        nom = nombre.strip().upper()

        if not cod or not nom:

            raise ValidacionDatosError("El código y el nombre del programa son obligatorios.")

        if len(cod) > 10:

            raise ValidacionDatosError("El código no debe exceder 10 caracteres.")

        nuevo = ProgramaEstudio(codigo_programa=cod, nombre_programa=nom)

        return self._modelo_programa.registrar(nuevo)




    def actualizar_programa(self, id_programa: int, codigo: str, nombre: str, estado: str) -> bool:

        if not id_programa or id_programa <= 0:

            raise ValidacionDatosError("Identificador de programa no válido.")

        cod = codigo.strip().upper()
        nom = nombre.strip().upper()

        if not cod or not nom:

            raise ValidacionDatosError("El código y el nombre del programa son obligatorios.")

        modificado = ProgramaEstudio(

            id_programa=id_programa,
            codigo_programa=cod,
            nombre_programa=nom,
            estado=estado



        )

        return self._modelo_programa.actualizar(modificado)



    def eliminar_programa(self, id_programa: int, logico: bool = True) -> bool:

        if not id_programa or id_programa <= 0:

            raise ValidacionDatosError("Identificador de programa no válido.")

        return self._modelo_programa.eliminar(id_programa, logico)



    