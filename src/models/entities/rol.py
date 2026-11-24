class Rol:
    """Clase pura de dominio que representa un Rol del sistema."""

    def __init__(
        self,
        id_rol: int = None,
        nombre_rol: str = "",
        descripcion: str = "",
        estado: str = "Activo"
    ):
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.descripcion = descripcion
        self.estado = estado

    def __repr__(self) -> str:
        return f"<Rol id={self.id_rol} nombre='{self.nombre_rol}'>"