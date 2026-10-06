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
    os.path.dirname(__file__), 'sig_caceres_resultados_electorales_base.ui'))
	

class SigCaceresResultadosElectorales(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresResultadosElectorales, self).__init__(parent)
        self.setupUi(self)
            
        rellena_combobox(dict_capas=municipales, combobox=self.combo_municipales)
        self.b_carga_municipales.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_municipales,
                                                                     dict_capas=municipales))
                                                                     
        rellena_combobox(dict_capas=autonomicas, combobox=self.combo_autonomicas)
        self.b_carga_autonomicas.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_autonomicas,
                                                                     dict_capas=autonomicas))

        rellena_combobox(dict_capas=generales, combobox=self.combo_generales)
        self.b_carga_generales.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_generales,
                                                                     dict_capas=generales))

        rellena_combobox(dict_capas=europeas, combobox=self.combo_europeas)
        self.b_carga_europeas.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_europeas,
                                                                     dict_capas=europeas))

    def carga_combo_capas(self):
        """
        Carga todas las capas de los combobox
        """        

    def carga_capas_canvas(self):
        """
        Carga las capas en el lienzo del proyecto
        """
        iface.messageBar().pushMessage("Info", "Capa cargada correctamente en el lienzo.", level=Qgis.Info)