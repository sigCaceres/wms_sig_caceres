from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import *

# Initialize Qt resources from file resources.py

from qgis.core import *  # No borrar
from ..rutas_capas.rutas_capas import *
from qgis.utils import iface
from ..sig_caceres import *
from .funciones_util import *

 # This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sig_caceres_censo_base.ui'))
	

class SigCaceresDatosdelCenso(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresDatosdelCenso, self).__init__(parent)
        self.setupUi(self)
            
        rellena_combobox(dict_capas=secciones_censales, combobox=self.combo_secciones_censales)
        self.b_carga_secciones_censales.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_secciones_censales,
                                                                     dict_capas=secciones_censales))
                                                                     
        rellena_combobox(dict_capas=colegios_electorales, combobox=self.combo_colegios_electorales)
        self.b_carga_colegios_electorales.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_colegios_electorales,
                                                                     dict_capas=colegios_electorales))

    def carga_combo_capas(self):
        """
        Carga todas las capas de los combobox
        """        

    def carga_capas_canvas(self):
        """
        Carga las capas en el lienzo del proyecto
        """
        iface.messageBar().pushMessage("Info","Capa cargada correctamente en el lienzo.", level=Qgis.Info)