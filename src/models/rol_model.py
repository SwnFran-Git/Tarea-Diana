from typing import List, Optional
from database.conexion_bd import ConexionBD
from models.entities.rol import Rol
from exceptions.biblioteca_exceptions import BibliotecaException


class RolModel:
    """Capa DAO: Persistencia completa (CRUD) para el catálogo de Roles."""

    @staticmethod
    def listar_todos() -> List[Rol]:
        conexion = None
        cursor = None
        lista: List[Rol] = []
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_roles_listar')
            for res in cursor.stored_results():
                for fila in res.fetchall():
                    lista.append(Rol(
                        id_rol=fila['id_rol'],
                        nombre_rol=fila['nombre_rol'],
                        descripcion=fila['descripcion'],
                        estado=fila['estado']
                    ))
            return lista
        except Exception as error:
            raise BibliotecaException(f"Error al listar roles: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def buscar_por_criterio(criterio: str) -> List[Rol]:
        conexion = None
        cursor = None
        lista: List[Rol] = []
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_roles_buscar', (criterio,))
            for res in cursor.stored_results():
                for fila in res.fetchall():
                    lista.append(Rol(
                        id_rol=fila['id_rol'],
                        nombre_rol=fila['nombre_rol'],
                        descripcion=fila['descripcion'],
                        estado=fila['estado']
                    ))
            return lista
        except Exception as error:
            raise BibliotecaException(f"Error al buscar roles: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(id_rol: int) -> Optional[Rol]:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_roles_obtener_por_id', (id_rol,))
            for res in cursor.stored_results():
                fila = res.fetchone()
                if fila:
                    return Rol(
                        id_rol=fila['id_rol'],
                        nombre_rol=fila['nombre_rol'],
                        descripcion=fila['descripcion'],
                        estado=fila['estado']
                    )
            return None
        except Exception as error:
            raise BibliotecaException(f"Error al obtener rol por ID: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def registrar(rol: Rol) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            cursor.callproc('sp_roles_registrar', (rol.nombre_rol, rol.descripcion))
            conexion.commit()
            return True
        except Exception as error:
            if conexion and conexion.is_connected():
                conexion.rollback()
            raise BibliotecaException(f"Error al registrar rol: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(rol: Rol) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            cursor.callproc('sp_roles_actualizar', (rol.id_rol, rol.nombre_rol, rol.descripcion, rol.estado))
            conexion.commit()
            return True
        except Exception as error:
            if conexion and conexion.is_connected():
                conexion.rollback()
            raise BibliotecaException(f"Error al actualizar rol: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(id_rol: int, logico: bool = True) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            sp = 'sp_roles_eliminar_logico' if logico else 'sp_roles_eliminar_fisico'
            cursor.callproc(sp, (id_rol,))
            conexion.commit()
            return True
        except Exception as error:
            if conexion and conexion.is_connected():
                conexion.rollback()
            if "1451" in str(error) or "foreign key" in str(error).lower():
                raise BibliotecaException("Integridad Referencial: Existen usuarios asignados a este rol.")
            raise BibliotecaException(f"Error al eliminar rol: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()