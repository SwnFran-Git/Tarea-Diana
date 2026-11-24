from PySide6.QtWidgets import QDialog, QMessageBox
from views.ui.frm_programa_form_ui import Ui_ProgramaFormDialog
from controllers.programa_controller import ProgramaController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class ProgramaFormDialog(QDialog, Ui_ProgramaFormDialog):
    """Formulario modal polimórfico (Crear / Editar) para Programas de Estudio."""

    def __init__(self, parent=None, id_programa_editar: int = None):
        super().__init__(parent)
        self.setupUi(self)
        self._controlador = ProgramaController()
        self._id_programa = id_programa_editar
        self.txt_codigo_programa.setMaxLength(10)

        if self._id_programa is not None:
            self.setWindowTitle("Modificar Programa de Estudio")
            self.btn_guardar.setText("Actualizar")
            self._cargar_datos()
        else:
            self.setWindowTitle("Registrar Nuevo Programa de Estudio")
            self.chk_estado.setEnabled(False)

        self.btn_guardar.clicked.connect(self._guardar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _cargar_datos(self):
        try:
            prog = self._controlador.obtener_programa_por_id(self._id_programa)
            if prog:
                self.txt_codigo_programa.setText(prog.codigo_programa)
                self.txt_nombre_programa.setText(prog.nombre_programa)
                self.chk_estado.setChecked(prog.estado == "Activo")
        except BibliotecaException as err:
            QMessageBox.critical(self, "Error", str(err))

    def _guardar(self):
        cod = self.txt_codigo_programa.text()
        nom = self.txt_nombre_programa.text()
        est = "Activo" if self.chk_estado.isChecked() else "Inactivo"
        try:
            if self._id_programa is None:
                self._controlador.registrar_programa(cod, nom)
                QMessageBox.information(self, "Éxito", "Programa registrado correctamente.")
            else:
                self._controlador.actualizar_programa(self._id_programa, cod, nom, est)
                QMessageBox.information(self, "Éxito", "Programa actualizado correctamente.")
            self.accept()
        except ValidacionDatosError as adv:
            QMessageBox.warning(self, "Validación", str(adv))
        except BibliotecaException as err:
            QMessageBox.critical(self, "Error de Base de Datos", str(err))
