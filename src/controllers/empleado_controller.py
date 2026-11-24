import re
import bcrypt
from typing import List, Dict, Any
from models.empleado_model import EmpleadoModel
from models.entities.empleado import Empleado
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException

class EmpleadoController:
    """Controlador que valida reglas de negocio y orquesta la persistencia de Empleados."""

    def __init__(self):

        self._modelo_empleado = EmpleadoModel()


    def registrar_empleado(

        self, documento: str, nombres: str, apellidos: str,
        username: str, clave_plana: str, rol_id: int,
        codigo: str, cargo: str, turno: str

    ) -> int:

        doc, nom, ape, user, cod, car = self._sanitizar_campos(
            documento, nombres, apellidos, username, codigo, cargo

        )

        if not all([doc, nom, ape, user, clave_plana, cod, car]):

            raise ValidacionDatosError("Todos los campos marcados son obligatorios.")

        self._validar_reglas_comunes(doc, user, rol_id)

        if len(clave_plana) < 6:
            raise ValidacionDatosError("La contraseña debe tener una longitud mínima de 6 caracteres.")

        clave_bytes = clave_plana.encode('utf-8')
        sal_segura = bcrypt.gensalt(rounds=12)
        clave_hash = bcrypt.hashpw(clave_bytes, sal_segura).decode('utf-8')
        nuevo_empleado = Empleado(
            numero_documento=doc,
            nombres=nom,
            apellidos=ape,
            nombre_usuario=user,
            clave_hash=clave_hash,
            rol_id=rol_id,
            codigo_empleado=cod,
            cargo=car,
            turno=turno


        )

        return self._modelo_empleado.registrar(nuevo_empleado)



    def actualizar_empleado(
        self, id_usuario: int, documento: str, nombres: str, apellidos: str,
        username: str, clave_plana: str, rol_id: int,
        codigo: str, cargo: str, turno: str
    ) -> bool:
        if id_usuario is None or id_usuario <= 0:
            raise ValidacionDatosError("Identificador relacional de colaborador no válido.")
        doc, nom, ape, user, cod, car = self._sanitizar_campos(
            documento, nombres, apellidos, username, codigo, cargo

        )
        if not all([doc, nom, ape, user, cod, car]):

            raise ValidacionDatosError("Todos los campos marcados son obligatorios.")

        self._validar_reglas_comunes(doc, user, rol_id)
        clave_hash = ""

        if clave_plana.strip():
            if len(clave_plana) < 6:

                raise ValidacionDatosError("La nueva contraseña debe tener un mínimo de 6 caracteres.")

            clave_bytes = clave_plana.encode('utf-8')
            sal_segura = bcrypt.gensalt(rounds=12)
            clave_hash = bcrypt.hashpw(clave_bytes, sal_segura).decode('utf-8')
            empleado_actualizado = Empleado(
            id_usuario=id_usuario,

            numero_documento=doc,
            nombres=nom,

            apellidos=ape,
            nombre_usuario=user,
            clave_hash=clave_hash,
            rol_id=rol_id,
            codigo_empleado=cod,
            cargo=car,
            turno=turno

        )

        return self._modelo_empleado.actualizar(empleado_actualizado)



    def obtener_empleado_por_id(self, id_usuario: int) -> Dict[str, Any]:

        if id_usuario is None or id_usuario <= 0:
            raise ValidacionDatosError("Identificador no válido.")

        datos = self._modelo_empleado.obtener_por_id(id_usuario)

        if not datos:
            raise BibliotecaException("El colaborador no fue encontrado en la base de datos.")

        return datos




    def listar_empleados(self, criterio: str = "") -> List[Dict[str, Any]]:
        return self._modelo_empleado.listar(criterio.strip())



    def eliminar_empleado(self, id_usuario: int, logico: bool = True) -> bool:

        if id_usuario is None or id_usuario <= 0:
            raise ValidacionDatosError("Identificador de empleado no válido.")

        if id_usuario == 1:

            raise ValidacionDatosError("Operación denegada: No se puede eliminar al Administrador Principal del sistema.")

        return self._modelo_empleado.eliminar(id_usuario, logico)



    

  


    def _sanitizar_campos(self, doc, nom, ape, user, cod, car):

        return (

            doc.strip(),
            nom.strip(),
            ape.strip(),
            user.strip().lower(),
            cod.strip().upper(),
            car.strip()


        )



    def _validar_reglas_comunes(self, doc: str, user: str, rol_id: int):

        if len(doc) != 8 or not doc.isdigit():

            raise ValidacionDatosError("El DNI debe contener exactamente 8 dígitos numéricos.")
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron_correo, user):

            raise ValidacionDatosError("El formato del usuario/correo electrónico no es válido.")

        if rol_id is None or rol_id <= 0:

            raise ValidacionDatosError("Debe asignar un rol válido al colaborador.")
        
    
    def filtrar_reporte(self,rol_id=0,turno="",solo_activos=False,criterio=""):
    # Reutilizamos el método listar existente
        empleados = self._modelo_empleado.listar(criterio)

        resultado = []

        # Obtener roles asociados a los usuarios
        conexion = None
        cursor = None

        try:
            from database.conexion_bd import ConexionBD

            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)

            cursor.execute("""
                SELECT id_usuario, rol_id
                FROM usuarios
            """)

            roles = {
                fila["id_usuario"]: fila["rol_id"]
                for fila in cursor.fetchall()
        }

        finally:
            if cursor:
                cursor.close()

            if conexion and conexion.is_connected():
                conexion.close()

        for emp in empleados:

        # FILTRO POR ROL
            if rol_id and roles.get(emp["id_usuario"]) != rol_id:
                continue

        # FILTRO POR TURNO
            if turno and "todos" not in turno.lower():
                if emp["turno"].strip().lower() != turno.lower():
                    continue

        # FILTRO POR ESTADO
            if solo_activos and emp["estado"] != "Activo":
                continue

            resultado.append(emp)

        return resultado