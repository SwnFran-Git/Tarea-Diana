# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_empleado_form.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_EmpleadoFormDialog(object):
    def setupUi(self, EmpleadoFormDialog):
        if not EmpleadoFormDialog.objectName():
            EmpleadoFormDialog.setObjectName(u"EmpleadoFormDialog")
        EmpleadoFormDialog.resize(480, 410)
        self.verticalLayout = QVBoxLayout(EmpleadoFormDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.l1 = QLabel(EmpleadoFormDialog)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.txt_numero_documento = QLineEdit(EmpleadoFormDialog)
        self.txt_numero_documento.setObjectName(u"txt_numero_documento")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_numero_documento)

        self.l2 = QLabel(EmpleadoFormDialog)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.txt_nombres = QLineEdit(EmpleadoFormDialog)
        self.txt_nombres.setObjectName(u"txt_nombres")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_nombres)

        self.l3 = QLabel(EmpleadoFormDialog)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.txt_apellidos = QLineEdit(EmpleadoFormDialog)
        self.txt_apellidos.setObjectName(u"txt_apellidos")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txt_apellidos)

        self.l4 = QLabel(EmpleadoFormDialog)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.txt_username = QLineEdit(EmpleadoFormDialog)
        self.txt_username.setObjectName(u"txt_username")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txt_username)

        self.l5 = QLabel(EmpleadoFormDialog)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.txt_password = QLineEdit(EmpleadoFormDialog)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txt_password)

        self.l6 = QLabel(EmpleadoFormDialog)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.cbo_rol = QComboBox(EmpleadoFormDialog)
        self.cbo_rol.setObjectName(u"cbo_rol")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cbo_rol)

        self.l7 = QLabel(EmpleadoFormDialog)
        self.l7.setObjectName(u"l7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.l7)

        self.txt_codigo_empleado = QLineEdit(EmpleadoFormDialog)
        self.txt_codigo_empleado.setObjectName(u"txt_codigo_empleado")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txt_codigo_empleado)

        self.l8 = QLabel(EmpleadoFormDialog)
        self.l8.setObjectName(u"l8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.l8)

        self.txt_cargo = QLineEdit(EmpleadoFormDialog)
        self.txt_cargo.setObjectName(u"txt_cargo")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.txt_cargo)

        self.l9 = QLabel(EmpleadoFormDialog)
        self.l9.setObjectName(u"l9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.l9)

        self.cbo_turno = QComboBox(EmpleadoFormDialog)
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.setObjectName(u"cbo_turno")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.cbo_turno)


        self.verticalLayout.addLayout(self.formLayout)

        self.hl_btns = QHBoxLayout()
        self.hl_btns.setObjectName(u"hl_btns")
        self.btn_guardar = QPushButton(EmpleadoFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.hl_btns.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(EmpleadoFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.hl_btns.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.hl_btns)


        self.retranslateUi(EmpleadoFormDialog)

        QMetaObject.connectSlotsByName(EmpleadoFormDialog)
    # setupUi

    def retranslateUi(self, EmpleadoFormDialog):
        EmpleadoFormDialog.setWindowTitle(QCoreApplication.translate("EmpleadoFormDialog", u"Gesti\u00f3n de Personal", None))
        self.l1.setText(QCoreApplication.translate("EmpleadoFormDialog", u"DNI:", None))
        self.l2.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Nombres:", None))
        self.l3.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Apellidos:", None))
        self.l4.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Correo / Usuario:", None))
        self.l5.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Contrase\u00f1a:", None))
        self.l6.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Rol:", None))
        self.l7.setText(QCoreApplication.translate("EmpleadoFormDialog", u"C\u00f3digo Empleado:", None))
        self.l8.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Cargo:", None))
        self.l9.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Turno:", None))
        self.cbo_turno.setItemText(0, QCoreApplication.translate("EmpleadoFormDialog", u"Ma\u00f1ana", None))
        self.cbo_turno.setItemText(1, QCoreApplication.translate("EmpleadoFormDialog", u"Tarde", None))
        self.cbo_turno.setItemText(2, QCoreApplication.translate("EmpleadoFormDialog", u"Noche", None))
        self.cbo_turno.setItemText(3, QCoreApplication.translate("EmpleadoFormDialog", u"Completo", None))

        self.btn_guardar.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Guardar Empleado", None))
        self.btn_cancelar.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Cancelar", None))
    # retranslateUi

