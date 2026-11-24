# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_rol_list.ui'
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

class Ui_RolListForm(object):
    def setupUi(self, RolListForm):
        if not RolListForm.objectName():
            RolListForm.setObjectName(u"RolListForm")
        RolListForm.resize(760, 480)
        self.verticalLayout = QVBoxLayout(RolListForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hl_top = QHBoxLayout()
        self.hl_top.setObjectName(u"hl_top")
        self.txt_buscar = QLineEdit(RolListForm)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.hl_top.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(RolListForm)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.hl_top.addWidget(self.btn_buscar)

        self.btn_nuevo = QPushButton(RolListForm)
        self.btn_nuevo.setObjectName(u"btn_nuevo")

        self.hl_top.addWidget(self.btn_nuevo)

        self.btn_editar = QPushButton(RolListForm)
        self.btn_editar.setObjectName(u"btn_editar")

        self.hl_top.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(RolListForm)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.hl_top.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.hl_top)

        self.tbl_roles = QTableWidget(RolListForm)
        if (self.tbl_roles.columnCount() < 4):
            self.tbl_roles.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_roles.setObjectName(u"tbl_roles")
        self.tbl_roles.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_roles.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayout.addWidget(self.tbl_roles)

        self.label_2 = QLabel(RolListForm)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(RolListForm)

        QMetaObject.connectSlotsByName(RolListForm)
    # setupUi

    def retranslateUi(self, RolListForm):
        RolListForm.setWindowTitle(QCoreApplication.translate("RolListForm", u"Gesti\u00f3n de Roles", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("RolListForm", u"Buscar rol...", None))
        self.btn_buscar.setText(QCoreApplication.translate("RolListForm", u"Buscar", None))
        self.btn_nuevo.setText(QCoreApplication.translate("RolListForm", u"Nuevo Rol", None))
        self.btn_editar.setText(QCoreApplication.translate("RolListForm", u"Editar Rol", None))
        self.btn_eliminar.setText(QCoreApplication.translate("RolListForm", u"Eliminar Rol", None))
        ___qtablewidgetitem = self.tbl_roles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RolListForm", u"ID", None))
        ___qtablewidgetitem1 = self.tbl_roles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RolListForm", u"Nombre del Rol", None))
        ___qtablewidgetitem2 = self.tbl_roles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("RolListForm", u"Descripci\u00f3n", None))
        ___qtablewidgetitem3 = self.tbl_roles.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("RolListForm", u"Estado", None))
        self.label_2.setText(QCoreApplication.translate("RolListForm", u"Mostrando 0 roles", None))
    # retranslateUi

