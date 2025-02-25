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

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sig_caceres_movilidad_servicios_base.ui'))


class SigCaceresMovilidadServicios(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresMovilidadServicios, self).__init__(parent)
        self.setupUi(self)




    def carga_capas_gasolinera(self):
        """
        Carga todas las capas de gasolinera
        """


    def carga_capas_puntos_recarga(self):
        """
        Carga las capas puntos de recarga
        """

    def carga_capas_taxi(self):
        """
        Carga las capas taxi
        """

    def carga_capas_estacion_bus_tren(self):
        """
        Carga las capas en de estaciones bus y de tren
        """



