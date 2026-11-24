class Empleado:
    """Clase pura de dominio que modela la herencia relacional Usuario + Empleado."""

    def __init__(
        self,
        id_usuario: int = None,
        numero_documento: str = "",
        nombres: str = "",
        apellidos: str = "",
        nombre_usuario: str = "",
        clave_hash: str = "",
        rol_id: int = None,
        codigo_empleado: str = "",
        cargo: str = "",
        turno: str = "Mañana"
    ):
        self.id_usuario = id_usuario
        self.numero_documento = numero_documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.nombre_usuario = nombre_usuario
        self.clave_hash = clave_hash
        self.rol_id = rol_id
        self.codigo_empleado = codigo_empleado
        self.cargo = cargo
        self.turno = turno