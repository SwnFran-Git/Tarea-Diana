from PySide6.QtWidgets import QDialog, QMessageBox
from views.ui.frm_login_ui import Ui_LoginDialog
from controllers.auth_controller import AuthController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class LoginDialog(QDialog, Ui_LoginDialog):
    """Vista modal encargada de capturar credenciales y validar acceso con BCrypt."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._controlador_autenticacion = AuthController()
        self.usuario_autenticado = None

        self.btn_ingresar.clicked.connect(self._al_hacer_clic_ingresar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _al_hacer_clic_ingresar(self):
        usuario_tipeado = self.txt_usuario.text()
        clave_tipeada = self.txt_password.text()
        try:
            self.usuario_autenticado = self._controlador_autenticacion.iniciar_sesion(
                usuario_tipeado, clave_tipeada
            )
            self.accept()
        except ValidacionDatosError as advertencia:
            QMessageBox.warning(self, "Acceso Denegado", str(advertencia))
            self.txt_password.clear()
            self.txt_password.setFocus()
        except BibliotecaException as error_sistema:
            QMessageBox.critical(self, "Error de Sistema", str(error_sistema))
