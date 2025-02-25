# -*- coding: utf-8 -*-
"""
Modulo de Servicios, submenú Servicios

"""
__author__ = "SIG Caceres"
__copyright__ = "Copyright 2024, SIG Caceres"
__credits__ = ["SIG Caceres"]

__version__ = "1.1.0"
__maintainer__ = "SIG Cáceres"
__email__ = "https://sig.caceres.es/"
__status__ = "Production"


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
    os.path.dirname(__file__), 'sig_caceres_servicios_base.ui'))


class SigCaceresServiciosServicios(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresServiciosServicios, self).__init__(parent)
        self.setupUi(self)
                                                                     
        rellena_combobox(dict_capas=centrosadministrativos, combobox=self.combo_centrosadministrativos)
        self.b_carga_centrosadministrativos.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_centrosadministrativos,
                                                                     dict_capas=centrosadministrativos))
            
        rellena_combobox(dict_capas=centrossanitarios, combobox=self.combo_centrossanitarios)
        self.b_carga_centrossanitarios.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_centrossanitarios,
                                                                     dict_capas=centrossanitarios))
            
        rellena_combobox(dict_capas=serviciosturisticos, combobox=self.combo_serviciosturisticos)
        self.b_carga_serviciosturisticos.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_serviciosturisticos,
                                                                     dict_capas=serviciosturisticos))
            
        rellena_combobox(dict_capas=ocio_entretenimiento, combobox=self.combo_ocioentretenimiento)
        self.b_carga_ocioentretenimiento.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_ocioentretenimiento,
                                                                     dict_capas=ocio_entretenimiento))
                                                                     
        rellena_combobox(dict_capas=mobiliario_urbano, combobox=self.combo_mobiliariourbano)
        self.b_carga_mobiliariourbano.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_mobiliariourbano,
                                                                     dict_capas=mobiliario_urbano))

    def carga_combo_capas(self):
        """
        Carga todas las capas de los combobox
        """        

    def carga_capas_canvas(self):
        """
        Carga las capas en el lienzo del proyecto
        """
        iface.messageBar().pushMessage("Info", msg_capas, level=Qgis.Info)
