# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_programa_list.ui'
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
        Form.resize(820, 500)
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

        self.tbl_programas = QTableWidget(Form)
        if (self.tbl_programas.columnCount() < 4):
            self.tbl_programas.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_programas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_programas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_programas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_programas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_programas.setObjectName(u"tbl_programas")
        self.tbl_programas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_programas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayout.addWidget(self.tbl_programas)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cat\u00e1logo de Programas de Estudio", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar por c\u00f3digo o nombre...", None))
        self.btn_buscar.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.btn_nuevo.setText(QCoreApplication.translate("Form", u"Nuevo Programa", None))
        self.btn_editar.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        ___qtablewidgetitem = self.tbl_programas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        ___qtablewidgetitem1 = self.tbl_programas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Estado", None))
        ___qtablewidgetitem2 = self.tbl_programas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nombre", None))
        ___qtablewidgetitem3 = self.tbl_programas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Creaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Se muestran los \u00faltimos (0) registros", None))
    # retranslateUi

