from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView, QDialog
from PySide6.QtCore import Qt
from views.ui.frm_empleado_list_ui import Ui_Form
from views.empleado_form_dialog import EmpleadoFormDialog
from controllers.empleado_controller import EmpleadoController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class EmpleadoListView(QWidget, Ui_Form):
    """Controlador visual del catálogo CRUD de Empleados."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._controlador = EmpleadoController()
        self.txt_buscar.setClearButtonEnabled(True)

        cab = self.tbl_empleados.horizontalHeader()
        cab.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cab.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        cab.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)

        self.btn_buscar.clicked.connect(self._cargar_grilla)
        self.txt_buscar.returnPressed.connect(self._cargar_grilla)
        self.txt_buscar.textChanged.connect(self._al_cambiar_texto_busqueda)

        self.btn_nuevo.clicked.connect(self._al_hacer_clic_nuevo)
        self.btn_editar.clicked.connect(self._al_hacer_clic_editar)
        self.btn_eliminar.clicked.connect(self._al_hacer_clic_eliminar)

        self._cargar_grilla()

    def _cargar_grilla(self):
        try:
            criterio = self.txt_buscar.text()
            lista = self._controlador.listar_empleados(criterio)
            self._renderizar_tabla(lista)
        except BibliotecaException as ex:
            QMessageBox.critical(self, "Error", str(ex))

    def _al_cambiar_texto_busqueda(self, texto: str):
        if not texto.strip():
            self._cargar_grilla()

    def _renderizar_tabla(self, lista):
        self.tbl_empleados.setRowCount(0)
        for fila_idx, emp in enumerate(lista):
            self.tbl_empleados.insertRow(fila_idx)

            item_cod = QTableWidgetItem(emp['codigo_empleado'])
            item_cod.setData(99, emp['id_usuario'])
            item_cod.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_dni = QTableWidgetItem(emp['numero_documento'])
            item_dni.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nom = QTableWidgetItem(emp['nombre_completo'])
            item_cargo = QTableWidgetItem(emp['cargo'])

            item_turno = QTableWidgetItem(emp['turno'])
            item_turno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_rol = QTableWidgetItem(emp['rol'])
            item_rol.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_estado = QTableWidgetItem(emp['estado'])
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            for item in (item_cod, item_dni, item_nom, item_cargo, item_turno, item_rol, item_estado):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

            self.tbl_empleados.setItem(fila_idx, 0, item_cod)
            self.tbl_empleados.setItem(fila_idx, 1, item_dni)
            self.tbl_empleados.setItem(fila_idx, 2, item_nom)
            self.tbl_empleados.setItem(fila_idx, 3, item_cargo)
            self.tbl_empleados.setItem(fila_idx, 4, item_turno)
            self.tbl_empleados.setItem(fila_idx, 5, item_rol)
            self.tbl_empleados.setItem(fila_idx, 6, item_estado)

        self.lbl_contador.setText(f"Mostrando {len(lista)} colaboradores")

    def _al_hacer_clic_nuevo(self):
        modal = EmpleadoFormDialog(parent=self)
        if modal.exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()

    def _al_hacer_clic_editar(self):
        fila_actual = self.tbl_empleados.currentRow()
        if fila_actual < 0:
            QMessageBox.warning(self, "Selección Requerida", "Seleccione un empleado de la lista para editar.")
            return
        id_usuario = self.tbl_empleados.item(fila_actual, 0).data(99)
        modal_edicion = EmpleadoFormDialog(parent=self, id_usuario_editar=id_usuario)
        if modal_edicion.exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()

    def _al_hacer_clic_eliminar(self):
        fila = self.tbl_empleados.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Selección Requerida", "Seleccione un empleado de la lista.")
            return
        id_oculto = self.tbl_empleados.item(fila, 0).data(99)
        nombre_empleado = self.tbl_empleados.item(fila, 2).text()

        respuesta = QMessageBox.question(
            self,
            "Confirmar Baja de Personal",
            f"¿Está seguro de dar de baja (borrado lógico) al colaborador:\n\n{nombre_empleado}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if respuesta == QMessageBox.StandardButton.Yes:
            try:
                self._controlador.eliminar_empleado(id_oculto, logico=True)
                QMessageBox.information(self, "Baja Confirmada", "El colaborador ha sido desactivado del sistema.")
                self._cargar_grilla()
            except ValidacionDatosError as adv:
                QMessageBox.warning(self, "Operación No Permitida", str(adv))
            except BibliotecaException as err:
                QMessageBox.critical(self, "Error de Integridad", str(err))
