# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_programa_form.ui'
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

class Ui_ProgramaFormDialog(object):
    def setupUi(self, ProgramaFormDialog):
        if not ProgramaFormDialog.objectName():
            ProgramaFormDialog.setObjectName(u"ProgramaFormDialog")
        ProgramaFormDialog.resize(460, 220)
        self.verticalLayout = QVBoxLayout(ProgramaFormDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.l1 = QLabel(ProgramaFormDialog)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.txt_codigo_programa = QLineEdit(ProgramaFormDialog)
        self.txt_codigo_programa.setObjectName(u"txt_codigo_programa")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_codigo_programa)

        self.l2 = QLabel(ProgramaFormDialog)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.txt_nombre_programa = QLineEdit(ProgramaFormDialog)
        self.txt_nombre_programa.setObjectName(u"txt_nombre_programa")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_nombre_programa)

        self.chk_estado = QCheckBox(ProgramaFormDialog)
        self.chk_estado.setObjectName(u"chk_estado")
        self.chk_estado.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.chk_estado)


        self.verticalLayout.addLayout(self.formLayout)

        self.hl_btns = QHBoxLayout()
        self.hl_btns.setObjectName(u"hl_btns")
        self.btn_guardar = QPushButton(ProgramaFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.hl_btns.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(ProgramaFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.hl_btns.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.hl_btns)


        self.retranslateUi(ProgramaFormDialog)

        QMetaObject.connectSlotsByName(ProgramaFormDialog)
    # setupUi

    def retranslateUi(self, ProgramaFormDialog):
        ProgramaFormDialog.setWindowTitle(QCoreApplication.translate("ProgramaFormDialog", u"Programa de Estudio", None))
        self.l1.setText(QCoreApplication.translate("ProgramaFormDialog", u"C\u00f3digo (M\u00e1x. 10):", None))
        self.l2.setText(QCoreApplication.translate("ProgramaFormDialog", u"Nombre del Programa:", None))
        self.chk_estado.setText(QCoreApplication.translate("ProgramaFormDialog", u"Programa Activo", None))
        self.btn_guardar.setText(QCoreApplication.translate("ProgramaFormDialog", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("ProgramaFormDialog", u"Cancelar", None))
    # retranslateUi

