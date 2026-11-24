# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(480, 240)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(LoginDialog)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.l1 = QLabel(LoginDialog)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.txt_usuario = QLineEdit(LoginDialog)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_usuario)

        self.l2 = QLabel(LoginDialog)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.txt_password = QLineEdit(LoginDialog)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_password)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ingresar = QPushButton(LoginDialog)
        self.btn_ingresar.setObjectName(u"btn_ingresar")

        self.horizontalLayout.addWidget(self.btn_ingresar)

        self.btn_cancelar = QPushButton(LoginDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Inicio de Sesi\u00f3n - Sistema de Biblioteca", None))
        self.lbl_titulo.setText(QCoreApplication.translate("LoginDialog", u"SISTEMA DE GESTI\u00d3N DE BIBLIOTECA", None))
        self.l1.setText(QCoreApplication.translate("LoginDialog", u"Usuario / Correo:", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"admin@sistema.com", None))
        self.l2.setText(QCoreApplication.translate("LoginDialog", u"Contrase\u00f1a:", None))
        self.btn_ingresar.setText(QCoreApplication.translate("LoginDialog", u"Ingresar al Sistema", None))
        self.btn_cancelar.setText(QCoreApplication.translate("LoginDialog", u"Cancelar", None))
    # retranslateUi

