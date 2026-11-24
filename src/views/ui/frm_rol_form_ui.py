# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_rol_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_RolFormDialog(object):
    def setupUi(self, RolFormDialog):
        if not RolFormDialog.objectName():
            RolFormDialog.setObjectName(u"RolFormDialog")
        RolFormDialog.resize(420, 220)
        self.verticalLayout = QVBoxLayout(RolFormDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.l1 = QLabel(RolFormDialog)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.txt_nombre_rol = QLineEdit(RolFormDialog)
        self.txt_nombre_rol.setObjectName(u"txt_nombre_rol")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_nombre_rol)

        self.l2 = QLabel(RolFormDialog)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.txt_descripcion = QLineEdit(RolFormDialog)
        self.txt_descripcion.setObjectName(u"txt_descripcion")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_descripcion)

        self.chk_estado = QCheckBox(RolFormDialog)
        self.chk_estado.setObjectName(u"chk_estado")
        self.chk_estado.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.chk_estado)


        self.verticalLayout.addLayout(self.formLayout)

        self.hl_btns = QHBoxLayout()
        self.hl_btns.setObjectName(u"hl_btns")
        self.btn_guardar = QPushButton(RolFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.hl_btns.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(RolFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.hl_btns.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.hl_btns)


        self.retranslateUi(RolFormDialog)

        QMetaObject.connectSlotsByName(RolFormDialog)
    # setupUi

    def retranslateUi(self, RolFormDialog):
        RolFormDialog.setWindowTitle(QCoreApplication.translate("RolFormDialog", u"Formulario de Rol", None))
        self.l1.setText(QCoreApplication.translate("RolFormDialog", u"Nombre del Rol:", None))
        self.l2.setText(QCoreApplication.translate("RolFormDialog", u"Descripci\u00f3n:", None))
        self.chk_estado.setText(QCoreApplication.translate("RolFormDialog", u"Rol Activo", None))
        self.btn_guardar.setText(QCoreApplication.translate("RolFormDialog", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("RolFormDialog", u"Cancelar", None))
    # retranslateUi

