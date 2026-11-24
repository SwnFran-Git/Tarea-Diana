# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 640)
        self.action_programas = QAction(MainWindow)
        self.action_programas.setObjectName(u"action_programas")
        self.action_roles = QAction(MainWindow)
        self.action_roles.setObjectName(u"action_roles")
        self.action_empleados = QAction(MainWindow)
        self.action_empleados.setObjectName(u"action_empleados")
        self.action_reporte_empleados = QAction(MainWindow)
        self.action_reporte_empleados.setObjectName(u"action_reporte_empleados")
        self.action_dashboard = QAction(MainWindow)
        self.action_dashboard.setObjectName(u"action_dashboard")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_portada = QLabel(self.centralwidget)
        self.lbl_portada.setObjectName(u"lbl_portada")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lbl_portada.setFont(font)
        self.lbl_portada.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_portada)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 24))
        self.menuMantenimiento = QMenu(self.menubar)
        self.menuMantenimiento.setObjectName(u"menuMantenimiento")
        self.menuReportes = QMenu(self.menubar)
        self.menuReportes.setObjectName(u"menuReportes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMantenimiento.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menuMantenimiento.addAction(self.action_programas)
        self.menuMantenimiento.addAction(self.action_roles)
        self.menuMantenimiento.addSeparator()
        self.menuMantenimiento.addAction(self.action_empleados)
        self.menuReportes.addAction(self.action_reporte_empleados)
        self.menuReportes.addAction(self.action_dashboard)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Gesti\u00f3n de Biblioteca - Arquitectura MVC + DAO", None))
        self.action_programas.setText(QCoreApplication.translate("MainWindow", u"Programas de Estudio", None))
        self.action_roles.setText(QCoreApplication.translate("MainWindow", u"Roles", None))
        self.action_empleados.setText(QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.action_reporte_empleados.setText(QCoreApplication.translate("MainWindow", u"Consulta de Personal", None))
        self.action_dashboard.setText(QCoreApplication.translate("MainWindow", u"Tablero Estad\u00edstico (Dashboard)", None))
        self.lbl_portada.setText(QCoreApplication.translate("MainWindow", u"Sistema Corporativo de Biblioteca \u2014 Seleccione una opci\u00f3n en el men\u00fa superior", None))
        self.menuMantenimiento.setTitle(QCoreApplication.translate("MainWindow", u"&Mantenimiento", None))
        self.menuReportes.setTitle(QCoreApplication.translate("MainWindow", u"&Reportes", None))
    # retranslateUi

