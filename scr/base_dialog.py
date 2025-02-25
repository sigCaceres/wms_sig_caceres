# -*- coding: utf-8 -*-
"""
Dialog génerico

"""
__author__ = "SIG Caceres"
__copyright__ = "Copyright 2024, SIG Caceres"
__credits__ = ["SIG Caceres"]

__version__ = "1.1.0"
__maintainer__ = "SIG Cáceres"
__email__ = "https://sig.caceres.es/"
__status__ = "Production"

#___IMPORTACIÖN DE LIBRERÍAS

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import *

# Initialize Qt resources from file resources.py

from qgis.core import *  # No borrar
from ..rutas_capas.rutas_capas import *

from ..sig_caceres import *
from .funciones_util import cargar_todas_capas,cargar_capa_combobox



# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
#Indicar el nombre del archivo .ui
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'base_interfaz.ui'))


#generacoçpm de la CLASE
#Sustituir el parámetro NombreDeLaClase por el nombre de la clase deseado

class NombreDeLaClase(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        # Sustituir el parámetro NombreDeLaClase por el nombre de la clase deseado
        super(NombreDeLaClase, self).__init__(parent)
        self.setupUi(self)

        #Indicar la acción de los widget introducidos en la interfaz

        self.b_cargacapaejemplo.clicked.connect(lambda:cargar_todas_capas(dict_capas_carril_bici))
        self.b_cargacapacombobox.clicked.connect(lambda: cargar_capa_combobox(combobox=self.comboBox_capas,dict_capas=dict_capas_carril_bici))

















