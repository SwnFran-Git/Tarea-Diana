import sys
from PySide6.QtWidgets import QApplication, QDialog
from views.login_dialog import LoginDialog
from views.main_window import MainWindow


def principal():
    aplicacion = QApplication(sys.argv)
    aplicacion.setStyle("Fusion")

    cuadro_login = LoginDialog()
    if cuadro_login.exec() == QDialog.DialogCode.Accepted:
        ventana_principal = MainWindow(usuario_actual=cuadro_login.usuario_autenticado)
        ventana_principal.show()
        sys.exit(aplicacion.exec())
    else:
        sys.exit(0)


if __name__ == "__main__":
    principal()