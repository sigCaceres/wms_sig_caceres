from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import *

# Initialize Qt resources from file resources.py

from qgis.core import *  # No borrar
from ..rutas_capas.rutas_capas import *
from qgis.utils import iface
#from ..sig_caceres import *
from .funciones_util import *

 # This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sig_caceres_poblacion_base.ui'))
	

class SigCaceresDatosdePoblacion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresDatosdePoblacion, self).__init__(parent)
        self.setupUi(self)
            
        rellena_combobox(dict_capas=barrios, combobox=self.combo_barrios)
        self.b_carga_barrios.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_barrios,
                                                                     dict_capas=barrios))
                                                                     
        rellena_combobox(dict_capas=calles, combobox=self.combo_calles)
        self.b_carga_calles.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_calles,
                                                                     dict_capas=calles))

        rellena_combobox(dict_capas=poblacion_secciones, combobox=self.combo_poblacion_secciones)
        self.b_carga_poblacion_secciones.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_poblacion_secciones,
                                                                     dict_capas=poblacion_secciones))

        rellena_combobox(dict_capas=poblacion_manzanas, combobox=self.combo_poblacion_manzanas)
        self.b_carga_poblacion_manzanas.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_poblacion_manzanas,
                                                                     dict_capas=poblacion_manzanas))

    def carga_combo_capas(self):
        """
        Carga todas las capas de los combobox
        """        

    def carga_capas_canvas(self):
        """
        Carga las capas en el lienzo del proyecto
        """
        iface.messageBar().pushMessage("Info", "Capa cargada correctamente en el lienzo.", level=Qgis.Info)