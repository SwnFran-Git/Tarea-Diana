from PySide6.QtWidgets import QDialog, QMessageBox
from views.ui.frm_rol_form_ui import Ui_RolFormDialog
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class RolFormDialog(QDialog, Ui_RolFormDialog):
    """Formulario modal polimórfico (Crear / Editar) para Roles."""

    def __init__(self, parent=None, id_rol_editar: int = None):
        super().__init__(parent)
        self.setupUi(self)
        self._controlador = RolController()
        self._id_rol = id_rol_editar

        if self._id_rol is not None:
            self.setWindowTitle("Modificar Rol")
            self.btn_guardar.setText("Actualizar")
            self._cargar_datos()
        else:
            self.setWindowTitle("Registrar Nuevo Rol")
            self.chk_estado.setEnabled(False)

        self.btn_guardar.clicked.connect(self._guardar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _cargar_datos(self):
        try:
            rol = self._controlador.obtener_rol_por_id(self._id_rol)
            if rol:
                self.txt_nombre_rol.setText(rol.nombre_rol)
                self.txt_descripcion.setText(rol.descripcion)
                self.chk_estado.setChecked(rol.estado == "Activo")
        except BibliotecaException as err:
            QMessageBox.critical(self, "Error", str(err))

    def _guardar(self):
        nombre = self.txt_nombre_rol.text()
        desc = self.txt_descripcion.text()
        estado = "Activo" if self.chk_estado.isChecked() else "Inactivo"
        try:
            if self._id_rol is None:
                self._controlador.registrar_rol(nombre, desc)
                QMessageBox.information(self, "Éxito", "Rol registrado correctamente.")
            else:
                self._controlador.actualizar_rol(self._id_rol, nombre, desc, estado)
                QMessageBox.information(self, "Éxito", "Rol actualizado correctamente.")
            self.accept()
        except ValidacionDatosError as adv:
            QMessageBox.warning(self, "Validación", str(adv))
        except BibliotecaException as err:
            QMessageBox.critical(self, "Error de Base de Datos", str(err))
