# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_empleado_list.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(920, 520)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hl_top = QHBoxLayout()
        self.hl_top.setObjectName(u"hl_top")
        self.txt_buscar = QLineEdit(Form)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.hl_top.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(Form)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.hl_top.addWidget(self.btn_buscar)

        self.btn_nuevo = QPushButton(Form)
        self.btn_nuevo.setObjectName(u"btn_nuevo")

        self.hl_top.addWidget(self.btn_nuevo)

        self.btn_editar = QPushButton(Form)
        self.btn_editar.setObjectName(u"btn_editar")

        self.hl_top.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(Form)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.hl_top.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.hl_top)

        self.tbl_empleados = QTableWidget(Form)
        if (self.tbl_empleados.columnCount() < 7):
            self.tbl_empleados.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tbl_empleados.setObjectName(u"tbl_empleados")
        self.tbl_empleados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_empleados.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayout.addWidget(self.tbl_empleados)

        self.lbl_contador = QLabel(Form)
        self.lbl_contador.setObjectName(u"lbl_contador")

        self.verticalLayout.addWidget(self.lbl_contador)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cat\u00e1logo de Empleados", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar por DNI, C\u00f3digo o Apellidos...", None))
        self.btn_buscar.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.btn_nuevo.setText(QCoreApplication.translate("Form", u"Nuevo Empleado", None))
        self.btn_editar.setText(QCoreApplication.translate("Form", u"Editar Empleado", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form", u"Eliminar Empleado", None))
        ___qtablewidgetitem = self.tbl_empleados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        ___qtablewidgetitem1 = self.tbl_empleados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"DNI", None))
        ___qtablewidgetitem2 = self.tbl_empleados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Apellidos y Nombres", None))
        ___qtablewidgetitem3 = self.tbl_empleados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Cargo", None))
        ___qtablewidgetitem4 = self.tbl_empleados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Turno", None))
        ___qtablewidgetitem5 = self.tbl_empleados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Rol", None))
        ___qtablewidgetitem6 = self.tbl_empleados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Estado", None))
        self.lbl_contador.setText(QCoreApplication.translate("Form", u"Mostrando 0 colaboradores", None))
    # retranslateUi

