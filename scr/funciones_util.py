# -*- coding: utf-8 -*-
"""
Modulo de funciones generale SIG CACERES

"""
__author__ = "SIG Caceres"
__copyright__ = "Copyright 2024, SIG Caceres"
__credits__ = ["SIG Caceres"]

__version__ = "1.1.0"
__maintainer__ = "SIG Cáceres"
__email__ = "https://sig.caceres.es/"
__status__ = "Production"


from PyQt5 import QtGui
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets, QtCore
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import *
import os
import qgis
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCompleter
from qgis.PyQt.QtCore import *
# Initialize Qt resources from file resources.py

from qgis.core import *  # No borrar


def cargar_capa_combobox(combobox, dict_capas):
    """
    Función que carga la capa seleccionada en el ComboBox
    @param combobox:
    @param dict_capas:
    @return:
    """
    capa_text = combobox.currentText()
    for grupo, ruta in zip(dict_capas.keys(), dict_capas.values()):
        root = QgsProject.instance().layerTreeRoot()
        if grupo == capa_text:
            print(ruta)
            if root.findGroup(grupo) is None:
                qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + grupo,
                                                          level=Qgis.Info)
                group = root.addGroup(grupo)
                QgsLayerDefinition().loadLayerDefinition(ruta['path'], QgsProject.instance(),
                                                         rootGroup=group)
                "cargamos QLR al inicio del arbol de capas"
                cloned_group1 = group.clone()
                root.insertChildNode(0, cloned_group1)
                root.removeChildNode(group)
            else:
                qgis.utils.iface.messageBar().pushMessage("Warning", "Las capas :" + grupo + " ya estan cargadas",
                                                          level=Qgis.Warning,
                                                          duration=30)


def rellena_combobox(dict_capas, combobox):
    """
    Función rellena un combobox a partir de un diccionario de python
    @param dict_capas:
    @param combobox:
    @return:
    """
    for grupo in dict_capas.keys():
        combobox.addItems([str(grupo)])


def busqueda_campo(_self, capa, campo):
    """
    Genera la búsqueda a partir del campo de una capa
    @param _self:
    @param capa:
    @param campo:
    @return:
    """

    vlayer = QgsVectorLayer(capa["ruta"], capa["nombre"], "ogr")
    vlayer.setProviderEncoding(u'ISO 8859-1')
    features = set()
    for feature in vlayer.getFeatures():
        features.add(feature[campo])

    completer = QCompleter(features, _self)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    completer.setFilterMode(Qt.MatchContains)
    completer.setMaxVisibleItems(14)
    return completer


def busqueda_campo_doble(_self, capa, campo_1, texto_1, campo_2):
    """
     Genera la búsqueda a partir de la selección del valor de otro campo
    @param _self:
    @param capa:
    @param campo_1:
    @param texto_1:
    @param campo_2:
    @return:
    """
    capa_select = QgsVectorLayer(capa["ruta"], capa["nombre"], "ogr")
    capa_select.setProviderEncoding(u'ISO 8859-1')

    capa_select.selectByExpression(campo_1 + '=\'' + texto_1 + '\'')
    selection = capa_select.selectedFeatures()

    features = set()
    for feature in selection:
        features.add(str(feature[campo_2]))

    completer = QCompleter(features, _self)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    completer.setFilterMode(Qt.MatchContains)
    completer.setMaxVisibleItems(14)
    return completer


def cargar_capa(capa):
    """
    Crea la capa temporal para obtener los datos y la carga si es necesario
    return: layer
    """
    capas = []
    vlayer = QgsVectorLayer(capa["ruta"], capa["nombre"], "ogr")
    vlayer.setProviderEncoding(u'ISO 8859-1')
    check_capa_cargada(vlayer, capa["nombre"])
    return vlayer


def cargar_todas_capas(dict_capas):
    """
    Carga un conjunto de capas contenidas en un diccionario
    @param dict_capas:
    @return:
    """
    for capa in dict_capas.values():
        vlayer = QgsVectorLayer(capa["ruta"], capa["nombre"], "ogr")
        vlayer.setProviderEncoding(u'ISO 8859-1')
        check_capa_cargada(vlayer, capa["nombre"])


def check_capa_cargada(capa, nombre_capa):
    """
    Comprueba si una capa esta cargada en qgis, es una capa procedente de un shp, no de un qlr
    @param capa:
    @param nombre_capa:
    @return:
    """
    capas_cargadas_toc = set()

    for layer in QgsProject.instance().mapLayers().values():
        capas_cargadas_toc.add(layer.name())

    if nombre_capa in capas_cargadas_toc:
        qgis.utils.iface.messageBar().pushMessage("Warning", "La capa: " + nombre_capa + " ya esta cargada",
                                                  level=Qgis.Warning,
                                                  duration=30)
    else:
        qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capa: " + nombre_capa, level=Qgis.Info)
        QgsProject.instance().addMapLayer(capa)


def buscar_archivos_recursivamente(dir_entrada, extension_archivo):
    """
    Funcion que busca los archivos en un arbol de directorios ,
    con una extension pasada como argumento y retorna una lista con el nombre de los archivos.
    :param extension_archivo:
    :param dir_entrada:
    :return:
    """

    lista_shapes_encontrados = []
    lista_nombres = []
    for ruta, nombre_directorio, archivos in os.walk(dir_entrada):
        for archivo in archivos:
            if archivo.split(".")[-1] == extension_archivo:
                lista_shapes_encontrados.append(os.path.join(ruta, archivo))
                lista_nombres.append(archivo.split(".")[0])

    return lista_shapes_encontrados, lista_nombres

def cargar_capas_qlr(_self, grupo, path_qlr_general, nombre_capa,path_qlr_capa):
    """
    Funcion para cargar las capas de tipo qlr
    @param _self: equivalente al parametro self de la clase
    @param grupo: grupo de capas a crear o donde introducir las capas
    @param path_qlr: path de los archivos qlr todas las capas
    @param nombre_capa: capa que se puede haber eliminado de ese grupo y se necesita recargar
    @param path_qlr_capa: path de los archivos capa individual
    @return: nada
    """
    # se define objeto root, necesario para trabajar con grupos en el TOC
    root = QgsProject.instance().layerTreeRoot()
    # si no existe el grupo
    if root.findGroup(grupo) is None:
        # mensaje , cargar cpas
        qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + grupo,
                                                  level=Qgis.Info)
        # anade el grupo al TOC
        _self.group = root.addGroup(grupo)
        # anade capas a ese grupo
        QgsLayerDefinition().loadLayerDefinition(path_qlr_general, QgsProject.instance(),
                                                 rootGroup=_self.group)
    # si existe el grupo  y se ha eliminado una capa hay que recargarla
    elif root.findGroup(grupo).name() == grupo and check_capa_cargada_qlr(
            nombre_capa) is False:
        # se define el grupo donde se introduciran las capas
        _self.group = root.findGroup(grupo)
        # se cargan las capas en ese grupo
        QgsLayerDefinition().loadLayerDefinition(path_qlr_capa, QgsProject.instance(),
                                                 rootGroup=_self.group)

def check_capa_cargada_qlr(nombre_capa):
    """
    Comprueba si una capa esta cargada en qgis, es una capa procedente de un qlr
    @param capa:
    @param nombre_capa:
    @return: True /False
    """
    capas_cargadas_toc = set()

    for layer in QgsProject.instance().mapLayers().values():
        capas_cargadas_toc.add(layer.name())

    if nombre_capa in capas_cargadas_toc:
        return True
    else:
        return False                                                 