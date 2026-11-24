from typing import List, Optional
from database.conexion_bd import ConexionBD
from models.entities.programa_estudio import ProgramaEstudio
from exceptions.biblioteca_exceptions import BibliotecaException


class ProgramaModel:
    """Capa DAO: Responsable exclusivo de la persistencia para Programas de Estudio."""

    @staticmethod
    def listar_todos() -> List[ProgramaEstudio]:
        conexion = None
        cursor = None
        lista_programas: List[ProgramaEstudio] = []
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_programas_listar')
            for resultado in cursor.stored_results():
                for fila in resultado.fetchall():
                    lista_programas.append(ProgramaEstudio(
                        id_programa=fila['id_programa'],
                        codigo_programa=fila['codigo_programa'],
                        nombre_programa=fila['nombre_programa'],
                        estado=fila['estado'],
                        creado_en=fila['creado_en']
                    ))
            return lista_programas
        except Exception as error:
            raise BibliotecaException(f"Error en DAO al listar programas: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def buscar_por_criterio(criterio: str) -> List[ProgramaEstudio]:
        conexion = None
        cursor = None
        lista_resultados: List[ProgramaEstudio] = []
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            criterio_sanitizado = criterio.strip() if criterio else ""
            cursor.callproc('sp_programas_buscar', (criterio_sanitizado,))
            for resultado in cursor.stored_results():
                for fila in resultado.fetchall():
                    lista_resultados.append(ProgramaEstudio(
                        id_programa=fila['id_programa'],
                        codigo_programa=fila['codigo_programa'],
                        nombre_programa=fila['nombre_programa'],
                        estado=fila['estado'],
                        creado_en=fila['creado_en']
                    ))
            return lista_resultados
        except Exception as error:
            raise BibliotecaException(f"Error en DAO al buscar programas: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(id_programa: int) -> Optional[ProgramaEstudio]:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_programas_obtener_por_id', (id_programa,))
            for res in cursor.stored_results():
                fila = res.fetchone()
                if fila:
                    return ProgramaEstudio(
                        id_programa=fila['id_programa'],
                        codigo_programa=fila['codigo_programa'],
                        nombre_programa=fila['nombre_programa'],
                        estado=fila['estado'],
                        creado_en=fila['creado_en']
                    )
            return None
        except Exception as error:
            raise BibliotecaException(f"Error al consultar programa por ID: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def registrar(programa: ProgramaEstudio) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            cursor.callproc('sp_programas_registrar', (programa.codigo_programa, programa.nombre_programa))
            conexion.commit()
            return True
        except Exception as error:
            if conexion and conexion.is_connected():
                conexion.rollback()
            raise BibliotecaException(f"Error al registrar programa: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(programa: ProgramaEstudio) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            cursor.callproc('sp_programas_actualizar', (
                programa.id_programa, programa.codigo_programa, programa.nombre_programa, programa.estado
            ))
            conexion.commit()
            return True
        except Exception as error:
            if conexion and conexion.is_connected():
                conexion.rollback()
            raise BibliotecaException(f"Error al actualizar programa: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(id_programa: int, logico: bool = True) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            sp = 'sp_programas_eliminar_logico' if logico else 'sp_programas_eliminar_fisico'
            cursor.callproc(sp, (id_programa,))
            conexion.commit()
            return True
        except Exception as error:
            if conexion and conexion.is_connected():
                conexion.rollback()
            if "1451" in str(error) or "foreign key" in str(error).lower():
                raise BibliotecaException("Integridad Referencial: El programa tiene estudiantes o libros vinculados.")
            raise BibliotecaException(f"Error al eliminar programa: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()