from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView, QDialog
from PySide6.QtCore import Qt
from views.ui.frm_rol_list_ui import Ui_RolListForm
from views.rol_form_dialog import RolFormDialog
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class RolListView(QWidget, Ui_RolListForm):
    """Controlador visual del catálogo de Roles."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._controlador = RolController()
        self.txt_buscar.setClearButtonEnabled(True)

        cab = self.tbl_roles.horizontalHeader()
        cab.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cab.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        self.btn_buscar.clicked.connect(self._cargar_grilla)
        self.txt_buscar.textChanged.connect(self._cargar_grilla)
        self.btn_nuevo.clicked.connect(self._nuevo)
        self.btn_editar.clicked.connect(self._editar)
        self.btn_eliminar.clicked.connect(self._eliminar)
        self.tbl_roles.itemSelectionChanged.connect(self._al_cambiar_seleccion)

        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)
        self._cargar_grilla()

    def _al_cambiar_seleccion(self):
        hay = len(self.tbl_roles.selectedItems()) > 0
        self.btn_editar.setEnabled(hay)
        self.btn_eliminar.setEnabled(hay)

    def _cargar_grilla(self):
        try:
            lista = self._controlador.listar_roles(self.txt_buscar.text())
            self.tbl_roles.setRowCount(0)
            for idx, r in enumerate(lista):
                self.tbl_roles.insertRow(idx)
                it_id = QTableWidgetItem(str(r.id_rol))
                it_id.setData(99, r.id_rol)
                it_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                it_nom = QTableWidgetItem(r.nombre_rol)
                it_des = QTableWidgetItem(r.descripcion)
                it_est = QTableWidgetItem(r.estado)
                it_est.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                for it in (it_id, it_nom, it_des, it_est):
                    it.setFlags(it.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tbl_roles.setItem(idx, 0, it_id)
                self.tbl_roles.setItem(idx, 1, it_nom)
                self.tbl_roles.setItem(idx, 2, it_des)
                self.tbl_roles.setItem(idx, 3, it_est)
            self.label_2.setText(f"Mostrando ({len(lista)}) roles")
        except BibliotecaException as err:
            QMessageBox.critical(self, "Error", str(err))

    def _nuevo(self):
        if RolFormDialog(self).exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()

    def _editar(self):
        fila = self.tbl_roles.currentRow()
        if fila >= 0:
            id_rol = self.tbl_roles.item(fila, 0).data(99)
            if RolFormDialog(self, id_rol).exec() == QDialog.DialogCode.Accepted:
                self._cargar_grilla()

    def _eliminar(self):
        fila = self.tbl_roles.currentRow()
        if fila < 0:
            return
        id_rol = self.tbl_roles.item(fila, 0).data(99)
        nombre = self.tbl_roles.item(fila, 1).text()
        resp = QMessageBox.question(
            self, "Confirmar Baja", f"¿Dar de baja el rol '{nombre}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if resp == QMessageBox.StandardButton.Yes:
            try:
                self._controlador.eliminar_rol(id_rol, logico=True)
                self._cargar_grilla()
            except (ValidacionDatosError, BibliotecaException) as err:
                QMessageBox.warning(self, "Aviso", str(err))
