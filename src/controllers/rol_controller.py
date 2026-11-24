from typing import List, Optional
from models.rol_model import RolModel
from models.entities.rol import Rol
from exceptions.biblioteca_exceptions import ValidacionDatosError



class RolController:

    """Controlador que orquesta la lógica de negocio para Roles."""

    def __init__(self):

        self._modelo_rol = RolModel()




    def obtener_roles(self) -> List[Rol]:

        todos = self._modelo_rol.listar_todos()

        return [

            r for r in todos

            if str(r.estado).strip().lower() in ("activo", "1", "true")

            and str(r.nombre_rol).strip().lower() != "estudiante"

        ]


    def listar_roles(self, criterio: str = "") -> List[Rol]:

        texto = criterio.strip()

        if not texto:

            return self._modelo_rol.listar_todos()

        return self._modelo_rol.buscar_por_criterio(texto)






    def obtener_rol_por_id(self, id_rol: int) -> Optional[Rol]:

        if not id_rol or id_rol <= 0:

            raise ValidacionDatosError("Identificador de rol no válido.")

        return self._modelo_rol.obtener_por_id(id_rol)




    def registrar_rol(self, nombre_rol: str, descripcion: str) -> bool:

        nombre = nombre_rol.strip()

        if not nombre:

            raise ValidacionDatosError("El nombre del rol es obligatorio.")

        nuevo = Rol(nombre_rol=nombre, descripcion=descripcion.strip())

        return self._modelo_rol.registrar(nuevo)










    def actualizar_rol(self, id_rol: int, nombre_rol: str, descripcion: str, estado: str) -> bool:



        if not id_rol or id_rol <= 0:



            raise ValidacionDatosError("Identificador de rol no válido.")



        nombre = nombre_rol.strip()





        if not nombre:





            raise ValidacionDatosError("El nombre del rol es obligatorio.")





        if id_rol == 1 and estado == "Inactivo":



            raise ValidacionDatosError("No se puede desactivar el rol Administrador principal.")





        rol_mod = Rol(id_rol=id_rol, nombre_rol=nombre, descripcion=descripcion.strip(), estado=estado)



        return self._modelo_rol.actualizar(rol_mod)









    def eliminar_rol(self, id_rol: int, logico: bool = True) -> bool:



        if not id_rol or id_rol <= 0:



            raise ValidacionDatosError("Identificador de rol no válido.")



        if id_rol in (1, 2, 3):



            raise ValidacionDatosError("Operación denegada: Los roles base del sistema están protegidos.")



        return self._modelo_rol.eliminar(id_rol, logico)