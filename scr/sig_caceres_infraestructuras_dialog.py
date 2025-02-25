# -*- coding: utf-8 -*-
"""
Modulo de infraestucturas

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
    os.path.dirname(__file__), 'sig_caceres_infraestructuras_base.ui'))


class SigCaceresInfraestructuras(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SigCaceresInfraestructuras, self).__init__(parent)
        self.setupUi(self)
        self.b_carriles_bici.clicked.connect(self.run_carril_bici)
        self.b_luminarias.clicked.connect(self.run_luminarias)
        self.b_saneamiento.clicked.connect(self.run_saneamiento)
        self.b_senalizacion_v.clicked.connect(self.run_senalizacion)
        self.b_contenedores.clicked.connect(self.run_contenedores)
        self.b_anadir_saneamiento.clicked.connect(self.run_button_saneamiento)
        self.b_abastecimiento.clicked.connect(self.run_abastecimiento)
        self.b_anadir_abastecimiento.clicked.connect(self.run_button_abastecimiento)
        self.frame_saneamiento.close()
        self.frame_abastecimiento_2.close()

    def run_senalizacion(self):
        """
        Carga todas las capas de senalizacion
        @return:
        """
        # este caso es especial de cargar las capas a  partir se su archivo  <<qlr>>
        # carga las capas que se encuentren en el directorio <<path_senalizacion_estilos>>
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_SENALIZACION) is None:
            iface.messageBar().pushMessage("Info", "Cargando capas.:"+NOMBRE_GRUPO_SENALIZACION, level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_SENALIZACION)
            QgsLayerDefinition().loadLayerDefinition(PATH_SENALIZACION, QgsProject.instance(),
                                                     rootGroup=group)
        else:
            iface.messageBar().pushMessage("Warning", "Las capas :" + NOMBRE_GRUPO_SENALIZACION + " ya estan cargadas",
                                           level=Qgis.Warning,
                                           duration=1)
    def run_carril_bici(self):
        """
        Carga todas las capas del carril bici
        @return:
        """
        # carga todas las capas que se hayan guardado en ese diccionario, si estan los archivos de estilos <<qml>>
        # en ese directorio, los coge por defecto
        cargar_todas_capas(dict_capas_carril_bici)

    def run_luminarias(self):
        """
        Carga todas las capas de luminarias
        @return:
        """
        # carga todas las capas que se hayan guardado en ese diccionario, si estan los archivos de estilos <<qml>>
        # en ese directorio, los coge por defecto
        cargar_todas_capas(dict_capas_luminarias)

    def run_saneamiento(self):
        """
        Cierra el elemento frame de abastecimiento y abre el de saneamiento con sus botones
         @return:
        """
        self.frame_abastecimiento_2.close()
        self.frame_saneamiento.show()

    def run_abastecimiento(self):
        """
        Cierra el elemento frame de saneamiento y abre el de abastecimiento con sus botones
        @return:
        """

        self.frame_saneamiento.close()
        self.frame_abastecimiento_2.show()

    def run_button_saneamiento(self):
        """
        Funcion que maneja los botones del menu saneamiento
        @return:
        """
        self.frame_saneamiento.close()

        if self.check_acometida.isChecked():
            cargar_capa(dict_capas_saneamiento["AcometidaSaneamiento"])
            self.check_acometida.setChecked(False)
        if self.check_edar.isChecked():
            cargar_capa(dict_capas_saneamiento["EDAR"])
            self.check_edar.setChecked(False)
        if self.check_nudo.isChecked():
            cargar_capa(dict_capas_saneamiento["Nudo"])
            self.check_nudo.setChecked(False)
        if self.check_aliviadero.isChecked():
            cargar_capa(dict_capas_saneamiento["Aliviadero"])
            self.check_aliviadero.setChecked(False)
        if self.check_estacion.isChecked():
            cargar_capa(dict_capas_saneamiento["EstacionBombeo"])
            self.check_estacion.setChecked(False)
        if self.check_pozo.isChecked():
            cargar_capa(dict_capas_saneamiento["Pozo"])
            self.check_pozo.setChecked(False)
        if self.check_colector.isChecked():
            cargar_capa(dict_capas_saneamiento["Colector"])
            self.check_colector.setChecked(False)
        if self.check_imbornal.isChecked():
            cargar_capa(dict_capas_saneamiento["Imbornal"])
            self.check_imbornal.setChecked(False)
        if self.check_puntovertido.isChecked():
            cargar_capa(dict_capas_saneamiento["PuntoVertido"])
            self.check_puntovertido.setChecked(False)

    def run_button_abastecimiento(self):
        """
        Funcion que maneja los botones del menu abastecimiento
        @return:
        """

        if self.check_acometidadistrib.isChecked():
            cargar_capa(dict_capas_abastecimiento["AcometidaDistribucion"])
            self.check_acometidadistrib.setChecked(False)
        if self.check_bocariego.isChecked():
            cargar_capa(dict_capas_abastecimiento["InjertoBocaRiego"])
            self.check_bocariego.setChecked(False)
        if self.check_desague.isChecked():
            cargar_capa(dict_capas_abastecimiento["Desague"])
            self.check_desague.setChecked(False)
        if self.check_fuente.isChecked():
            cargar_capa(dict_capas_abastecimiento["Fuente"])
            self.check_fuente.setChecked(False)
        if self.check_hidrante.isChecked():
            cargar_capa(dict_capas_abastecimiento["Hidrante"])
            self.check_hidrante.setChecked(False)
        if self.check_llave.isChecked():
            cargar_capa(dict_capas_abastecimiento["LlavePaso"])
            self.check_llave.setChecked(False)
        if self.check_nudoacometida.isChecked():
            cargar_capa(dict_capas_abastecimiento["NudoAcometida"])
            self.check_nudoacometida.setChecked(False)
        if self.check_nudodistribuc.isChecked():
            cargar_capa(dict_capas_abastecimiento["NudoDistribucion"])
            self.check_nudodistribuc.setChecked(False)
        if self.check_puntoacometida.isChecked():
            cargar_capa(dict_capas_abastecimiento["PuntoAcometida"])
            self.check_puntoacometida.setChecked(False)
        if self.check_tubo.isChecked():
            cargar_capa(dict_capas_abastecimiento["Tubo"])
            self.check_tubo.setChecked(False)
        if self.check_valvulacorte.isChecked():
            cargar_capa(dict_capas_abastecimiento["ValvulaCorte"])
            self.check_valvulacorte.setChecked(False)
        if self.check_valvulareguladora.isChecked():
            cargar_capa(dict_capas_abastecimiento["ValvulaReguladoraPresion"])
            self.check_valvulareguladora.setChecked(False)
        if self.check_ventosa.isChecked():
            cargar_capa(dict_capas_abastecimiento["Ventosa"])
            self.check_ventosa.setChecked(False)
        self.frame_abastecimiento_2.close()

    def run_contenedores(self):
        """
        Carga todas las capas de contenedores de basura
        """

        # carga todas las capas que se hayan guardado en ese diccionario, si estan los archivos de estilos <<qml>>
        # en ese directorio, los coge por defecto
        cargar_todas_capas(dict_capas_basura)
