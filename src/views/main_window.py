from PySide6.QtWidgets import QMainWindow



from views.ui.frm_main_ui import Ui_MainWindow



from views.programa_list_view import ProgramaListView



from views.rol_list_view import RolListView



from views.empleado_list_view import EmpleadoListView



from views.empleado_reporte_view import EmpleadoReporteView



#from views.dashboard_view import DashboardView











class MainWindow(QMainWindow, Ui_MainWindow):



    """Contenedor principal de navegación corporativa del sistema."""







    def __init__(self, usuario_actual=None):



        super().__init__()



        self.setupUi(self)



        self._usuario_actual = usuario_actual







        if self._usuario_actual:



            self.statusbar.showMessage(



                f"Operador conectado: {self._usuario_actual.nombre_completo}  |  Rol: {self._usuario_actual.rol}"



            )







        self._ventana_programas = None



        self._ventana_roles = None



        self._ventana_empleados = None



        self._ventana_reporte_empleados = None



        self._ventana_dashboard = None

        self._ventana_reporte_empleados = None


        self.action_programas.triggered.connect(self._abrir_modulo_programas)



        self.action_roles.triggered.connect(self._abrir_modulo_roles)



        self.action_empleados.triggered.connect(self._abrir_modulo_empleados)



        self.action_reporte_empleados.triggered.connect(self._abrir_reporte_empleados)



        #self.action_dashboard.triggered.connect(self._abrir_dashboard)

        self.action_reporte_empleados.triggered.connect(self._abrir_reporte_empleados)


    def _abrir_modulo_programas(self):



        if self._ventana_programas is None or not self._ventana_programas.isVisible():



            self._ventana_programas = ProgramaListView()



            self._ventana_programas.show()



        else:



            self._ventana_programas.activateWindow()



            self._ventana_programas.raise_()







    def _abrir_modulo_roles(self):



        if self._ventana_roles is None or not self._ventana_roles.isVisible():



            self._ventana_roles = RolListView()



            self._ventana_roles.show()



        else:



            self._ventana_roles.activateWindow()



            self._ventana_roles.raise_()







    def _abrir_modulo_empleados(self):



        if self._ventana_empleados is None or not self._ventana_empleados.isVisible():



            self._ventana_empleados = EmpleadoListView()



            self._ventana_empleados.show()



        else:



            self._ventana_empleados.activateWindow()



            self._ventana_empleados.raise_()







    def _abrir_reporte_empleados(self):



        if self._ventana_reporte_empleados is None or not self._ventana_reporte_empleados.isVisible():



            self._ventana_reporte_empleados = EmpleadoReporteView()



            self._ventana_reporte_empleados.show()



        else:



            self._ventana_reporte_empleados.activateWindow()



            self._ventana_reporte_empleados.raise_()







    #def _abrir_dashboard(self):



        #if self._ventana_dashboard is None or not self._ventana_dashboard.isVisible():



            #self._ventana_dashboard = DashboardView()



            #self._ventana_dashboard.show()



        #else:



            #self._ventana_dashboard.activateWindow()



            #self._ventana_dashboard.raise_()
    
    def _abrir_reporte_empleados(self):
        """Despliega la ventana de Consultas y Reportes manteniendo instancia única."""

        if (
            self._ventana_reporte_empleados is None
            or not self._ventana_reporte_empleados.isVisible()
        ):
            self._ventana_reporte_empleados = EmpleadoReporteView()
            self._ventana_reporte_empleados.show()

        else:
            self._ventana_reporte_empleados.activateWindow()
            self._ventana_reporte_empleados.raise_()
