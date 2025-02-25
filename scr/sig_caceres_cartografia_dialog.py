# -*- coding: utf-8 -*-
"""
Modulo de Cartografía, submenú cartografía

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
    os.path.dirname(__file__), 'sig_caceres_cartografia_base.ui'))


class SigCaceresCartografiaCartografia(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresCartografiaCartografia, self).__init__(parent)
        self.setupUi(self)
            
        rellena_combobox(dict_capas=urbana_vectorial, combobox=self.combo_urbanavectorial)
        self.b_carga_urbanavectorial.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_urbanavectorial,
                                                                     dict_capas=urbana_vectorial))
                                                                     
        rellena_combobox(dict_capas=urbana_escaneada, combobox=self.combo_urbanaescaneada)
        self.b_carga_urbanaescaneada.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_urbanaescaneada,
                                                                     dict_capas=urbana_escaneada))

        rellena_combobox(dict_capas=TM_vectorial, combobox=self.combo_tmvectorial)
        self.b_carga_tmvectorial.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_tmvectorial,
                                                                     dict_capas=TM_vectorial))

        rellena_combobox(dict_capas=TM_escaneada, combobox=self.combo_tmescaneada)
        self.b_carga_tmescaneada.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_tmescaneada,
                                                                     dict_capas=TM_escaneada))

        rellena_combobox(dict_capas=Planos_escaneados, combobox=self.combo_planosescaneados)
        self.b_carga_planosescaneados.clicked.connect(lambda: cargar_capa_combobox(combobox=self.combo_planosescaneados,
                                                                     dict_capas=Planos_escaneados))

    def carga_combo_capas(self):
        """
        Carga todas las capas de los combobox
        """        

    def carga_capas_canvas(self):
        """
        Carga las capas en el lienzo del proyecto
        """
        iface.messageBar().pushMessage("Info", msg_capas, level=Qgis.Info)
