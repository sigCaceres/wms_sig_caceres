# -*- coding: utf-8 -*-
__author__ = "SIG Caceres"
__copyright__ = "Copyright 2024, SIG Caceres"
__credits__ = ["SIG Caceres"]

__version__ = "1.1.0"
__maintainer__ = "SIG Cáceres"
__email__ = "https://sig.caceres.es/"
__status__ = "Production"


from re import S
import qgis
from PyQt5.QtWidgets import QMenu
from PyQt5.uic.properties import QtGui
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import Qgis
from qgis.core import *
# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the dialog
from .sig_caceres_dialog import SigCaceresDialog
import os.path
from .scr.sig_caceres_servicios_dialog import SigCaceresServiciosServicios
from .scr.sig_caceres_infraestructuras_dialog import SigCaceresInfraestructuras
from .scr.sig_caceres_cartografia_dialog import SigCaceresCartografiaCartografia
from .scr.sig_caceres_movilidad_servicios_dialog import SigCaceresMovilidadServicios
from .scr.sig_caceres_catastro_anterior_dialog import SigCaceresCatastroAnterior
from .scr.base_dialog import NombreDeLaClase
from .rutas_capas.rutas_capas import *
from .scr.funciones_util import *


class SigCaceres:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'SigCaceres_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&SIG Cáceres')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.toolbar = self.iface.addToolBar(u'SigCaceres')
        self.toolbar.setObjectName(u'SigCaceres')

    # noinspection PyMethodMayBeStatic

    def creacion_submenus(self, dict_menu, _submenu):
        """
        Crear submenus a apartir de un diccionario de datos
        @param dict_menu:
        @param _submenu:
        @return:
        """

        for k, v in zip(dict_menu.keys(),
                        dict_menu.values()):
            if v['visible'] == 'si':
                menu_funcion = QAction(QIcon(v['icon']), v['name'], self.iface.mainWindow())
                menu_funcion.setObjectName(v['name'])
                menu_funcion.setWhatsThis(v['name'])
                menu_funcion.setStatusTip(v['name'])
                menu_funcion.triggered.connect(v['funcion'])


                _submenu.addAction(menu_funcion)
        return _submenu

    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('SigCaceres', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """
 
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # modificado para barra independiente
            self.toolbar.addAction(action)

        if add_to_menu:
            # modificacion para añadir un menu nuevo
            self.menu_ppal.addAction(
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.menu_ppal = self.iface.mainWindow().findChild(QMenu, '&SIG Cáceres WMS')

        if not self.menu_ppal:
            self.menu_ppal = QMenu(self.iface.mainWindow())
            self.menu_ppal.setObjectName('&SIG Cáceres WMS')
            self.menu_ppal.setTitle('&SIG Cáceres WMS')

        dict_menu = {}

        # _DATOS
        # _________________________________________________________________________________________________________

        dict_menu['cartografia_ortofotos'] = {}
        dict_menu['callejero_toponimia'] = {}
        dict_menu['catastro'] = {}
        dict_menu['planeamiento'] = {}
        dict_menu['expediente_urbanismo'] = {}
        dict_menu['infraestructuras'] = {}
        dict_menu['redes_viarias'] = {}
        dict_menu['movilidad'] = {}
        dict_menu['inventario_patrimonio'] = {}
        dict_menu['archivo_historico'] = {}
        dict_menu['servicios'] = {}
        dict_menu['parcelarios'] = {}
        dict_menu['medioambiente'] = {}
        dict_menu['tematicos'] = {}

        # _________________________________________________________________________________________________

        # #######################################  CREACIÓN DE SUBMENUS
        # _________________________________________________________________________________________________


        # ****************************************** CARTOGRAFIA Y ORTOFOTOS

        dict_menu['cartografia_ortofotos']['ortofotos'] = {'icon':' ',
                                                           'name': 'Ortofotos',
                                                           'funcion': self.run_ortofotos,
                                                           'visible': 'si'}

        dict_menu['cartografia_ortofotos']['ortofotos_historicas'] = {'icon':' ',
                                                           'name': 'Ortofotos Históricas',
                                                           'funcion': self.run_ortofotos_historicas,
                                                           'visible': 'si'}

        dict_menu['cartografia_ortofotos']['pnoa_anual'] = {'icon':' ',
                                                           'name': 'PNOA Anual',
                                                           'funcion': self.run_pnoa_anual,
                                                           'visible': 'si'}

        dict_menu['cartografia_ortofotos']['cartografia'] = {'icon': '',
                                                             'name': 'Cartografia',
                                                             'funcion': self.run_cartografia_cartografia,
                                                             'visible': 'si'}

        dict_menu['cartografia_ortofotos']['mapas_base'] = {'icon':' ',
                                                           'name': 'Mapas Base',
                                                           'funcion': self.run_mapas_base,
                                                           'visible': 'si'}

        # ************************************************** CALLEJERO Y TOPONIMIA

        dict_menu['callejero_toponimia']['barrios_distritos'] = {'icon': '',
                                                                 'name': 'Barrios y Distritos',
                                                                 'funcion': self.run_barrios,
                                                                 'visible': 'si'}

        dict_menu['callejero_toponimia']['callejero'] = {'icon': '',
                                                         'name': 'Callejero',
                                                         'funcion': self.run_callejero,
                                                         'visible': 'si'}


        # ************************************************************ CATASTRO

        dict_menu['catastro']['catastro_actual'] = {'icon': '', 
                                                    'name': 'Catastro Actual',
                                                    'funcion': self.run_catastro_actual,
                                                    'visible': 'si'}

        dict_menu['catastro']['catastro_anterior'] = {'icon': '', 
                                                      'name': 'Catastro Anterior',
                                                      'funcion': self.run_catastro_anterior,
                                                      'visible': 'no'}

        # ************************************************************** PLANEAMIENTO

        dict_menu['planeamiento']['pgm_2010'] = {'icon': '  ', 
                                                 'name': 'PGM 2010',
                                                 'funcion': self.run_pgm_2010,
                                                 'visible': 'si'}

        dict_menu['planeamiento']['plan_especial'] = {'icon': ' ',
                                                      'name': 'Plan Especial (PEPRPA)',
                                                      'funcion': self.run_pe_peprpa,
                                                      'visible': 'si'}

        dict_menu['planeamiento']['pgou_1999'] = {'icon': ' ',
                                                  'name': 'PGOU 1999',
                                                  'funcion': self.run_pgou_1999,
                                                  'visible': 'si'}

        dict_menu['planeamiento']['pgou_1985'] = {'icon': ' ',
                                                  'name': 'PGOU 1985',
                                                  'funcion': self.run_pgou_1985,
                                                  'visible': 'si'}

        dict_menu['planeamiento']['pgm_1961'] = {'icon': '  ',
                                                 'name': 'PGOU 1961',
                                                 'funcion': self.run_pgou_1961,
                                                 'visible': 'si'}

        dict_menu['planeamiento']['plan_director_muralla'] = {'icon': ' ', 
                                                              'name': 'Plan Director de la Muralla',
                                                              'funcion': self.run_pd_muralla,
                                                              'visible': 'si'}

        dict_menu['planeamiento']['plan_ordenes_sectoriales'] = {'icon': '  ',
                                                              'name': 'Órdenes Sectoriales',
                                                              'funcion': self.run_ordenes_sectoriales,
                                                              'visible': 'si'}

        dict_menu['planeamiento']['BIC'] = {'icon': '',
                                                    'name': 'BIC',
                                                    'funcion': self.run_bienes_interes,
                                                    'visible': 'si'}

        # *********************************************************** INFRAESTRUCTURAS
                                                                   
        dict_menu['infraestructuras']['abastecimiento'] = {'icon': '',
                                                            'name': 'Abastecimiento',
                                                            'funcion': self.run_abastecimiento,
                                                            'visible': 'no'}

        dict_menu['infraestructuras']['saneamiento'] = {'icon': '',
                                                            'name': 'Saneamiento',
                                                            'funcion': self.run_saneamiento,
                                                            'visible': 'no'}

        dict_menu['infraestructuras']['gas_extremadura'] = {'icon': '',
                                                            'name': 'Gas Extremadura',
                                                            'funcion': self.run_gas_extremadura,
                                                            'visible': 'no'}

        dict_menu['infraestructuras']['luminarias'] = {'icon': '',
                                                            'name': 'Luminarias',
                                                            'funcion': self.run_luminarias,
                                                            'visible': 'no'}
        
        dict_menu['infraestructuras']['contenedores_basura'] = {'icon': '',
                                                            'name': 'Contenedores Basura',
                                                            'funcion': self.run_contenedores_basura,
                                                            'visible': 'si'}
                                                      
        # ********************************************************** REDES VIARIAS
        dict_menu['redes_viarias']['senalizacion_vertical'] = {'icon': '',
                                                'name': 'Señalización Vertical',
                                                'funcion': self.run_senalizacion_vertical,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['carreteras'] = {'icon': '',
                                                'name': 'Carreteras',
                                                'funcion': self.run_carreteras,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['ferrocarril'] = {'icon': '',
                                                'name': 'Ferrocarril',
                                                'funcion': self.run_ferrocarril,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['puntos_kilometricos'] = {'icon': '',
                                                'name': 'Puntos Kilométricos',
                                                'funcion': self.run_puntos_kilometricos,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['carril_bici'] = {'icon': '',
                                                'name': 'Carril Bici',
                                                'funcion': self.run_carril_bici,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['vias_pecuarias'] = {'icon': '',
                                                'name': 'Vias Pecuarias',
                                                'funcion': self.run_vias_pecuarias,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['red_de_calles'] = {'icon': '',
                                                'name': 'Red de Calles',
                                                'funcion': self.run_red_de_calles,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['calles_peatonales'] = {'icon': '',
                                                'name': 'Calles Peatonales',
                                                'funcion': self.run_calles_peatonales,
                                                'visible': 'si'}
                                                
        dict_menu['redes_viarias']['pintura_trafico'] = {'icon': '',
                                                'name': 'Pintura Trafico',
                                                'funcion': self.run_pintura_trafico,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['anchura_acerados'] = {'icon': '',
                                                'name': 'Ancho de Aceras',
                                                'funcion': self.run_anchura_acerados,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['glorietas_isletas'] = {'icon': '',
                                                'name': 'Glorietas e Isletas',
                                                'funcion': self.run_glorietas_isletas,
                                                'visible': 'si'}

        dict_menu['redes_viarias']['sentido_circulacion'] = {'icon': '',
                                                'name': 'Sentido de Circulacion',
                                                'funcion': self.run_sentido_circulacion,
                                                'visible': 'si'}

        # ********************************************************** MOVILIDAD

        dict_menu['movilidad']['bus_urbano'] = {'icon': '',
                                                'name': 'Bus Urbano',
                                                'funcion': self.run_bus_urbano,
                                                'visible': 'si'}

        dict_menu['movilidad']['aparcamientos'] = {'icon': '',
                                                   'name': 'Aparcamientos',
                                                   'funcion': self.run_aparcamientos,
                                                   'visible': 'si'}

        dict_menu['movilidad']['vados'] = {'icon': '',
                                                   'name': 'Vados',
                                                   'funcion': self.run_vados,
                                                   'visible': 'si'}

        dict_menu['movilidad']['zona_azul'] = {'icon': '',
                                                   'name': 'Zona Azul',
                                                   'funcion': self.run_zona_azul,
                                                   'visible': 'si'}   

        dict_menu['movilidad']['parking_motos'] = {'icon': '',
                                                   'name': 'Parking Motos',
                                                   'funcion': self.run_parking_motos,
                                                   'visible': 'si'}      

        dict_menu['movilidad']['movilidad_reducida'] = {'icon': '',
                                                        'name': 'Movilidad Reducida',
                                                        'funcion': self.run_movilidad_reducida,
                                                        'visible': 'si'}

        dict_menu['movilidad']['puntos_recarga'] = {'icon': '',
                                                   'name': 'Puntos de Recarga',
                                                   'funcion': self.run_puntos_recarga,
                                                   'visible': 'si'}

        dict_menu['movilidad']['zona_carga_descarga'] = {'icon': '',
                                                         'name': 'Zona carga y descarga',
                                                         'funcion': self.run_carga_descarga,
                                                         'visible': 'si'}
                                                         
        dict_menu['movilidad']['pasos_peatones'] = {'icon': '',
                                                         'name': 'Pasos de peatoenes',
                                                         'funcion': self.run_pasos_peatones,
                                                         'visible': 'si'}

        # ******************************************************* INVENTARIO PATRIMONIO

        dict_menu['inventario_patrimonio']['unesco_ciudad_vieja'] = {'icon': '',
                                                                           'name': 'UNESCO Ciudad Vieja',
                                                                           'funcion': self.run_unesco_ciudad_vieja,
                                                                           'visible': 'si'}

        dict_menu['inventario_patrimonio']['inventario'] = {'icon': '',
                                                            'name': 'Inventario',
                                                            'funcion': self.run_inventario,
                                                            'visible': 'si'}

        dict_menu['inventario_patrimonio']['catalogo_caminos_publicos'] = {'icon': '',
                                                                           'name': 'Catálogo de Caminos Públicos',
                                                                           'funcion': self.run_caminos_publicos,
                                                                           'visible': 'si'}
                                                            
        dict_menu['inventario_patrimonio']['ribera_marco'] = {'icon': '',
                                                                           'name': 'Inventario Ribera del Marco',
                                                                           'funcion': self.run_ribera_marco,
                                                                           'visible': 'si'}
                                                            
        dict_menu['inventario_patrimonio']['libro_yerbas'] = {'icon': '',
                                                                           'name': 'Libro de Yerbas',
                                                                           'funcion': self.run_libro_yerbas,
                                                                           'visible': 'si'}

        # ******************************************************* ARCHIVO HISTORICO

        dict_menu['archivo_historico']['expedientes_obra'] = {'icon': '',
                                                              'name': 'Expedientes de Obra anteriores a 1950',
                                                              'funcion': self.run_exp_obra_historicos,
                                                              'visible': 'si'}

        dict_menu['archivo_historico']['padrones_historicos'] = {'icon': '',
                                                                 'name': 'Padrones Históricos',
                                                                 'funcion': self.run_padrones_historicos,
                                                                 'visible': 'si'}

        dict_menu['archivo_historico']['fotos_historicas'] = {'icon': '',
                                                              'name': 'Fotos históricas',
                                                              'funcion': self.run_fotos_historicas,
                                                              'visible': 'si'}

        dict_menu['archivo_historico']['heraldica'] = {'icon': '',
                                                       'name': 'Heráldica',
                                                       'funcion': self.run_heraldica,
                                                       'visible': 'si'}
       
        dict_menu['archivo_historico']['audioguias'] = {'icon': '',
                                                       'name': 'Audioguías',
                                                       'funcion': self.run_audioguias,
                                                       'visible': 'si'}

        # ****************************************** SERVICIOS
        
        dict_menu['servicios']['servicios'] = {'icon': '',
                                                             'name': 'Servicios',
                                                             'funcion': self.run_servicios_servicios,
                                                             'visible': 'si'}
                                                             

        dict_menu['servicios']['beacons'] = {'icon': '',
                                                             'name': 'CC Pat inteligente beacons',
                                                             'funcion': self.run_beacons,
                                                             'visible': 'si'}
                                                             

        # ****************************************** PARCELARIOS
        
        dict_menu['parcelarios']['poligono_ganadero'] = {'icon': '',
                                                             'name': 'Poligono Ganadero',
                                                             'funcion': self.run_poligono_ganadero,
                                                             'visible': 'si'}
                                                             

        dict_menu['parcelarios']['ferial'] = {'icon': '',
                                                             'name': 'Ferial',
                                                             'funcion': self.run_ferial,
                                                             'visible': 'si'}
                                                             

        # ****************************************** MEDIOAMBIENTE
        
        dict_menu['medioambiente']['arbolado'] = {'icon': '',
                                                             'name': 'Inventario de árboles',
                                                             'funcion': self.run_arbolado,
                                                             'visible': 'si'}
                                                             

        dict_menu['medioambiente']['parques_jardines'] = {'icon': '',
                                                             'name': 'Parques y jardines',
                                                             'funcion': self.run_parques_jardines,
                                                             'visible': 'si'}
                                                             

        # ******************************************************* TEMATICOS

        dict_menu['tematicos']['fotovoltaicas'] = {'icon': '',
                                                   'name': 'Fotovoltaicas',
                                                   'funcion': self.run_fotovoltaicas,
                                                   'visible': 'no'}

        dict_menu['tematicos']['geologico_minero'] = {'icon': '',
                                                   'name': 'Mapa Geológico Minero',
                                                   'funcion': self.run_geologico_minero,
                                                   'visible': 'si'}

        dict_menu['tematicos']['mapa_pendientes'] = {'icon': '',
                                                   'name': 'Mapa de Pendientes',
                                                   'funcion': self.run_mapa_pendientes,
                                                   'visible': 'si'}

        dict_menu['tematicos']['relieve'] = {'icon': '',
                                                   'name': 'Relieve',
                                                   'funcion': self.run_relieve,
                                                   'visible': 'si'}
												   
        # ____________________________________________________________________________________
        #  ############################### CREACIÓN DE LOS SUBMENUS
        # ____________________________________________________________________________________

        submenu_cartografia_ortofotos = self.menu_ppal.addMenu(QIcon(''), "Cartografia y ortofotos")

        submenu_callejero_toponimia = self.menu_ppal.addMenu(QIcon(''), "Callejero y Toponimia")

        submenu_catastro = self.menu_ppal.addMenu(QIcon(''), "Catastro")

        submenu_planeamiento = self.menu_ppal.addMenu(QIcon(''), "Planeamiento")

        submenu_expediente_urbanismo = self.menu_ppal.addMenu(QIcon(''), "Expedientes de Urbanismo")

        submenu_infraestructuras = self.menu_ppal.addMenu(QIcon(''), "Infraestructuras")

        submenu_redes_viarias = self.menu_ppal.addMenu(QIcon(''), "Redes Viarias")

        submenu_movilidad = self.menu_ppal.addMenu(QIcon(''), "Movilidad")

        submenu_inventario_patrimonio = self.menu_ppal.addMenu(QIcon(''), "Patrimonio")

        submenu_archivo_historico = self.menu_ppal.addMenu(QIcon(':/plugins/sig_caceres/iconos/vias_comunicación.png'),
                                                           "Archivo Histórico")

        submenu_servicios = self.menu_ppal.addMenu(QIcon(''), "Servicios")
        
        submenu_parcelarios = self.menu_ppal.addMenu(QIcon(''), "Parcelarios")
        
        submenu_medioambiente = self.menu_ppal.addMenu(QIcon(''), "Medioambiente")

        submenu_tematicos = self.menu_ppal.addMenu(QIcon(':/plugins/sig_caceres/iconos/vias_comunicación.png'),
                                                   "Temáticos")

        self.creacion_submenus(dict_menu=dict_menu['cartografia_ortofotos'], _submenu=submenu_cartografia_ortofotos)

        self.creacion_submenus(dict_menu=dict_menu['callejero_toponimia'], _submenu=submenu_callejero_toponimia)

        self.creacion_submenus(dict_menu=dict_menu['catastro'], _submenu=submenu_catastro)

        self.creacion_submenus(dict_menu=dict_menu['planeamiento'], _submenu=submenu_planeamiento)

        self.creacion_submenus(dict_menu=dict_menu['expediente_urbanismo'], _submenu=submenu_expediente_urbanismo)

        self.creacion_submenus(dict_menu=dict_menu['infraestructuras'], _submenu=submenu_infraestructuras)

        self.creacion_submenus(dict_menu=dict_menu['redes_viarias'], _submenu=submenu_redes_viarias)

        self.creacion_submenus(dict_menu=dict_menu['movilidad'], _submenu=submenu_movilidad)

        self.creacion_submenus(dict_menu=dict_menu['inventario_patrimonio'], _submenu=submenu_inventario_patrimonio)

        self.creacion_submenus(dict_menu=dict_menu['archivo_historico'], _submenu=submenu_archivo_historico)

        self.creacion_submenus(dict_menu=dict_menu['servicios'], _submenu=submenu_servicios)
        
        self.creacion_submenus(dict_menu=dict_menu['parcelarios'], _submenu=submenu_parcelarios)
        
        self.creacion_submenus(dict_menu=dict_menu['medioambiente'], _submenu=submenu_medioambiente)

        self.creacion_submenus(dict_menu=dict_menu['tematicos'], _submenu=submenu_tematicos)

        menuBar = self.iface.mainWindow().menuBar()
        menuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.menu_ppal)
        # will be set False in run()
        self.first_start = True

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        # personalizacion del original
        self.menu_ppal.clear()
        self.menu_ppal.deleteLater()

     # ********************************************************** CARTOGRAFIA Y ORTOFOTOS

    def run_ortofotos(self):
        """
        Carga el catastro actual a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ORTOFOTOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ORTOFOTOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ORTOFOTOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_ORTOFOTOS, QgsProject.instance(), rootGroup=group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ORTOFOTOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_ortofotos_historicas(self):
        """
        Carga las ORTOFOTOS HISTORICAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ORTOFOTOS_HISTORICAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ORTOFOTOS_HISTORICAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ORTOFOTOS_HISTORICAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_ORTOFOTOS_HISTORICAS, QgsProject.instance(), rootGroup=group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ORTOFOTOS_HISTORICAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_pnoa_anual(self):
        """
        Carga las ORTOFOTOS PNOA ANUALES a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PNOA_ANUAL) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PNOA_ANUAL,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PNOA_ANUAL)
            QgsLayerDefinition().loadLayerDefinition(PATH_PNOA_ANUAL, QgsProject.instance(), rootGroup=group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PNOA_ANUAL + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_mapas_base(self):
        """
        Carga los MAPAS BASE a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_MAPAS_BASE) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_MAPAS_BASE,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_MAPAS_BASE)
            QgsLayerDefinition().loadLayerDefinition(PATH_MAPAS_BASE, QgsProject.instance(), rootGroup=group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_MAPAS_BASE + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)


    def run_catastro_actual(self):
        """
        Carga el catastro actual a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CATASTRO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CATASTRO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CATASTRO)
            QgsLayerDefinition().loadLayerDefinition(PATH_CATASTRO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CATASTRO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_callejero(self):
        """
        Carga el callejero a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CALLEJERO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CALLEJERO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CALLEJERO)
            QgsLayerDefinition().loadLayerDefinition(PATH_CALLEJERO, QgsProject.instance(),rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CALLEJERO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_barrios(self):
        """
        Carga el BARRIOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_BARRIOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_BARRIOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_BARRIOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_BARRIOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_BARRIOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

     # ********************************************************** PLANEAMIENTO
    def run_pgm_2010(self):
        """
        Carga el PGM 2010 a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PGM_2010) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PGM_2010,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PGM_2010)
            QgsLayerDefinition().loadLayerDefinition(PATH_PGM_2010, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PGM_2010 + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30) 
                                                      
    def run_pe_peprpa(self):
        """
        Carga el PLAN ESPECIAL PEPRPA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PEPRPA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PEPRPA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PEPRPA)
            QgsLayerDefinition().loadLayerDefinition(PATH_PE_PEPRPA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PEPRPA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30) 

    def run_pgou_1999(self):
        """
        Carga el PGOU 1999 a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PGOU_1999) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PGOU_1999,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PGOU_1999)
            QgsLayerDefinition().loadLayerDefinition(PATH_PGOU_1999, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PGOU_1999 + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
    def run_pgou_1985(self):
        """
        Carga el PGOU 1985 a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PGOU_1985) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PGOU_1985,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PGOU_1985)
            QgsLayerDefinition().loadLayerDefinition(PATH_PGOU_1985, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PGOU_1985 + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
    def run_pgou_1975(self):
        """
        Carga el PGOU 1975 a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PGOU_1975) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PGOU_1975,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PGOU_1975)
            QgsLayerDefinition().loadLayerDefinition(PATH_PGOU_1975, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PGOU_1975 + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
    def run_pgou_1961(self):
        """
        Carga el PGOU 1961 a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PGOU_1961) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PGOU_1961,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PGOU_1961)
            QgsLayerDefinition().loadLayerDefinition(PATH_PGOU_1961, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PGOU_1961 + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_pd_muralla(self):
        """
        Carga el PLAN DIRECTOR MURALLA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PD_MURALLA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PD_MURALLA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PD_MURALLA)
            QgsLayerDefinition().loadLayerDefinition(PATH_PD_MURALLA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PD_MURALLA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30) 

    def run_ordenes_sectoriales(self):
        """
        Carga el ORDENES SECTORIALES a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ORDENES_SECTORIALES) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ORDENES_SECTORIALES,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ORDENES_SECTORIALES)
            QgsLayerDefinition().loadLayerDefinition(PATH_ORDENES_SECTORIALES, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ORDENES_SECTORIALES + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30) 
                                                      
    def run_bienes_interes(self):
        """
        Carga el BIC a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_BIC) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_BIC,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_BIC)
            QgsLayerDefinition().loadLayerDefinition(PATH_BIC, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_BIC + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)                                                
                                                      
     # ********************************************************** INFRAESTRUCTURAS

    def run_abastecimiento(self):
        """
        Carga el ABASTECIMIENTO a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ABASTECIMIENTO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ABASTECIMIENTO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ABASTECIMIENTO)
            QgsLayerDefinition().loadLayerDefinition(PATH_ABASTECIMIENTO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ABASTECIMIENTO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_gas_extremadura(self):
        """
        Carga el GAS EXTREMADURA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_GAS_EXTREMADURA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_GAS_EXTREMADURA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_GAS_EXTREMADURA)
            QgsLayerDefinition().loadLayerDefinition(PATH_GAS_EXTREMADURA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_GAS_EXTREMADURA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_luminarias(self):
        """
        Carga el LUMINARIAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_LUMINARIAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_LUMINARIAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_LUMINARIAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_LUMINARIAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_LUMINARIAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_saneamiento(self):
        """
        Carga el SANEAMIENTO a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_SANEAMIENTO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_SANEAMIENTO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_SANEAMIENTO)
            QgsLayerDefinition().loadLayerDefinition(PATH_SANEAMIENTO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_SANEAMIENTO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_contenedores_basura(self):
        """
        Carga el CONTENEDORES DE BASURA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CONTENEDORES_BASURA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CONTENEDORES_BASURA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CONTENEDORES_BASURA)
            QgsLayerDefinition().loadLayerDefinition(PATH_CONTENEDORES_BASURA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CONTENEDORES_BASURA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
     # ********************************************************** REDES VIARIAS

    def run_senalizacion_vertical(self):
        """
        Carga el SEÑALIZACIÓN VERTICAL a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_SENALIZACION_VERTICAL) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_SENALIZACION_VERTICAL,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_SENALIZACION_VERTICAL)
            QgsLayerDefinition().loadLayerDefinition(PATH_SENALIZACION_VERTICAL, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_SENALIZACION_VERTICAL + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_carreteras(self):
        """
        Carga el CARRETERAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CARRETERAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CARRETERAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CARRETERAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_CARRETERAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CARRETERAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_ferrocarril(self):
        """
        Carga el FERROCARRIL a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_FERROCARRIL) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_FERROCARRIL,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_FERROCARRIL)
            QgsLayerDefinition().loadLayerDefinition(PATH_FERROCARRIL, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_FERROCARRIL + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_puntos_kilometricos(self):
        """
        Carga el PUNTOS KILOMÉTRICOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PUNTOS_KILOMETRICOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PUNTOS_KILOMETRICOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PUNTOS_KILOMETRICOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_PUNTOS_KILOMETRICOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PUNTOS_KILOMETRICOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_carril_bici(self):
        """
        Carga el CARRIL BICI a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CARRIL_BICI) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CARRIL_BICI,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CARRIL_BICI)
            QgsLayerDefinition().loadLayerDefinition(PATH_CARRIL_BICI, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CARRIL_BICI + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      

    def run_vias_pecuarias(self):
        """
        Carga el VIAS PECUARIAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_VIAS_PECUARIAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_VIAS_PECUARIAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_VIAS_PECUARIAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_VIAS_PECUARIAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_VIAS_PECUARIAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)                                                 
                                                      

    def run_red_de_calles(self):
        """
        Carga el RED DE CALLES a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_RED_DE_CALLES) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_RED_DE_CALLES,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_RED_DE_CALLES)
            QgsLayerDefinition().loadLayerDefinition(PATH_RED_DE_CALLES, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_RED_DE_CALLES + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)  
                            
    def run_calles_peatonales(self):
        """
        Carga el CALLES PEATONALES a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CALLES_PEATONALES) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CALLES_PEATONALES,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CALLES_PEATONALES)
            QgsLayerDefinition().loadLayerDefinition(PATH_CALLES_PEATONALES, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CALLES_PEATONALES + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_pintura_trafico(self):
        """
        Carga el PINTURA TRAFICO a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PINTURA_TRAFICO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PINTURA_TRAFICO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PINTURA_TRAFICO)
            QgsLayerDefinition().loadLayerDefinition(PATH_PINTURA_TRAFICO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PINTURA_TRAFICO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
    def run_anchura_acerados(self):
        """
        Carga el ANCHURA ACERADOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ANCHURA_ACERADOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ANCHURA_ACERADOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ANCHURA_ACERADOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_ANCHURA_ACERADOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ANCHURA_ACERADOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
    def run_glorietas_isletas(self):
        """
        Carga el GLORIETAS ISLETAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_GLORIETAS_ISLETAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_GLORIETAS_ISLETAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_GLORIETAS_ISLETAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_GLORIETAS_ISLETAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_GLORIETAS_ISLETAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
    def run_sentido_circulacion(self):
        """
        Carga el SENTIDO CIRCULACIOM a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_SENTIDO_CIRCULACION) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_SENTIDO_CIRCULACION,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_SENTIDO_CIRCULACION)
            QgsLayerDefinition().loadLayerDefinition(PATH_SENTIDO_CIRCULACION, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_SENTIDO_CIRCULACION + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      
     # ********************************************************** MOVILIDAD

    def run_bus_urbano(self):
        """
        Carga el BUS URBANO a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_BUS_URBANO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_BUS_URBANO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_BUS_URBANO)
            QgsLayerDefinition().loadLayerDefinition(PATH_BUS_URBANO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_BUS_URBANO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_aparcamientos(self):
        """
        Carga el APARCAMIENTOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_APARCAMIENTOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_APARCAMIENTOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_APARCAMIENTOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_APARCAMIENTOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_APARCAMIENTOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_vados(self):
        """
        Carga el VADOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_VADOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_VADOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_VADOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_VADOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_VADOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_zona_azul(self):
        """
        Carga el ZONA AZUL a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ZONA_AZUL) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ZONA_AZUL,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ZONA_AZUL)
            QgsLayerDefinition().loadLayerDefinition(PATH_ZONA_AZUL, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ZONA_AZUL + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_parking_motos(self):
        """
        Carga el PARKING MOTOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PARKING_MOTOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PARKING_MOTOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PARKING_MOTOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_PARKING_MOTOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PARKING_MOTOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_movilidad_reducida(self):
        """
        Carga el PLAZAS DE MOVILIDAD REDUCIDA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_MOVILIDAD_REDUCIDA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_MOVILIDAD_REDUCIDA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_MOVILIDAD_REDUCIDA)
            QgsLayerDefinition().loadLayerDefinition(PATH_MOVILIDAD_REDUCIDA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_MOVILIDAD_REDUCIDA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_puntos_recarga(self):
        """
        Carga el PUNTOS DE RECARGA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PUNTOS_RECARGA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PUNTOS_RECARGA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PUNTOS_RECARGA)
            QgsLayerDefinition().loadLayerDefinition(PATH_PUNTOS_RECARGA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PUNTOS_RECARGA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_carga_descarga(self):
        """
        Carga el CARGA Y DESCARGA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CARGA_DESCARGA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CARGA_DESCARGA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CARGA_DESCARGA)
            QgsLayerDefinition().loadLayerDefinition(PATH_CARGA_DESCARGA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CARGA_DESCARGA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
                                                      

    def run_pasos_peatones(self):
        """
        Carga el PASOS DE PEATONES a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PASOS_PEATONES) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PASOS_PEATONES,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PASOS_PEATONES)
            QgsLayerDefinition().loadLayerDefinition(PATH_PASOS_PEATONES, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PASOS_PEATONES + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

     # ******************************************************* INVENTARIO PATRIMONIO

    def run_unesco_ciudad_vieja(self):
        """
        Carga el UNESCO CIUDAD VIEJA a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_UNESCO_CIUDAD_VIEJA) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_UNESCO_CIUDAD_VIEJA,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_UNESCO_CIUDAD_VIEJA)
            QgsLayerDefinition().loadLayerDefinition(PATH_UNESCO_CIUDAD_VIEJA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_UNESCO_CIUDAD_VIEJA + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_inventario(self):
        """
        Carga el INVENTARIO MUNICIPAL a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_INVENTARIO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_INVENTARIO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_INVENTARIO)
            QgsLayerDefinition().loadLayerDefinition(PATH_INVENTARIO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_INVENTARIO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_caminos_publicos(self):
        """
        Carga el CAMINOS PUBLICOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_CAMINOS_PUBLICOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_CAMINOS_PUBLICOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_CAMINOS_PUBLICOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_CAMINOS_PUBLICOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_CAMINOS_PUBLICOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_ribera_marco(self):
        """
        Carga el RIBERA DEL MARCO a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_RIBERA_MARCO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_RIBERA_MARCO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_RIBERA_MARCO)
            QgsLayerDefinition().loadLayerDefinition(PATH_RIBERA_MARCO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_RIBERA_MARCO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_libro_yerbas(self):
        """
        Carga el LIBRO DE YERBAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_LIBRO_YERBAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_LIBRO_YERBAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_LIBRO_YERBAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_LIBRO_YERBAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_LIBRO_YERBAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

     # ******************************************************* ARCHIVO HISTORICO

    def run_exp_obra_historicos(self):
        """
        Carga el EXPEDIENTES DE OBRA HISTORICOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_EXPEDIENTES_OBRA_HISTORICOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_EXPEDIENTES_OBRA_HISTORICOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_EXPEDIENTES_OBRA_HISTORICOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_EXPEDIENTES_OBRA_HISTORICOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_EXPEDIENTES_OBRA_HISTORICOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_padrones_historicos(self):
        """
        Carga el PADRONES HISTORICOS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PADRONES_HISTORICOS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PADRONES_HISTORICOS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PADRONES_HISTORICOS)
            QgsLayerDefinition().loadLayerDefinition(PATH_PADRONES_HISTORICOS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PADRONES_HISTORICOS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_fotos_historicas(self):
        """
        Carga el FOTOS HISTORICAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_FOTOS_HISTORICAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_FOTOS_HISTORICAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_FOTOS_HISTORICAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_FOTOS_HISTORICAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_FOTOS_HISTORICAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_heraldica(self):
        """
        Carga el HERALDICAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_HERALDICAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_HERALDICAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_HERALDICAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_HERALDICA, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_HERALDICAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_audioguias(self):
        """
        Carga el AUDIOGUIAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_AUDIOGUIAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_AUDIOGUIAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_AUDIOGUIAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_AUDIOGUIAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_AUDIOGUIAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

     # ******************************************************* SERVICIOS

    def run_beacons(self):
        """
        Carga el Beacon a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_BEACONS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_BEACONS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_BEACONS)
            QgsLayerDefinition().loadLayerDefinition(PATH_BEACONS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_BEACONS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)
     
     # ******************************************************* PARCELARIOS

    def run_poligono_ganadero(self):
        """
        Carga el Poligono Ganadero a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_POLIGONO_GANADERO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_POLIGONO_GANADERO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_POLIGONO_GANADERO)
            QgsLayerDefinition().loadLayerDefinition(PATH_POLIGONO_GANADERO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_POLIGONO_GANADERO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_ferial(self):
        """
        Carga el Ferial a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_FERIAL) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_FERIAL,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_FERIAL)
            QgsLayerDefinition().loadLayerDefinition(PATH_FERIAL, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_FERIAL + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

     # ******************************************************* MEDIOAMBIENTE

    def run_arbolado(self):
        """
        Carga el Arbolado a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_ARBOLADO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_ARBOLADO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_ARBOLADO)
            QgsLayerDefinition().loadLayerDefinition(PATH_ARBOLADO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_ARBOLADO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_parques_jardines(self):
        """
        Carga los Parques y jardines a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_PARQUES_JARDINES) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_PARQUES_JARDINES,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_PARQUES_JARDINES)
            QgsLayerDefinition().loadLayerDefinition(PATH_PARQUES_JARDINES, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_PARQUES_JARDINES + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

     # ******************************************************* TEMÁTICAS

    def run_fotovoltaicas(self):
        """
        Carga el FOTOVOLTAICAS a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_FOTOVOLTAICAS) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_FOTOVOLTAICAS,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_FOTOVOLTAICAS)
            QgsLayerDefinition().loadLayerDefinition(PATH_FOTOVOLTAICAS, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_FOTOVOLTAICAS + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_geologico_minero(self):
        """
        Carga el MAPA GEOLÓGICO MINERO a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_GEOLOGICO_MINERO) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_GEOLOGICO_MINERO,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_GEOLOGICO_MINERO)
            QgsLayerDefinition().loadLayerDefinition(PATH_GEOLOGICO_MINERO, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_GEOLOGICO_MINERO + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_mapa_pendientes(self):
        """
        Carga el MAPA DE PENDIENTES a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_MAPA_PENDIENTES) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_MAPA_PENDIENTES,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_MAPA_PENDIENTES)
            QgsLayerDefinition().loadLayerDefinition(PATH_MAPA_PENDIENTES, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_MAPA_PENDIENTES + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    def run_relieve(self):
        """
        Carga el RELIEVE a partir de un archivo qlr, carga todas las capas que se encuentren definidas
        @return:
        """
        root = QgsProject.instance().layerTreeRoot()
        if root.findGroup(NOMBRE_GRUPO_RELIEVE) is None:
            qgis.utils.iface.messageBar().pushMessage("Info", "Cargando capas.:" + NOMBRE_GRUPO_RELIEVE,
                                                      level=Qgis.Info)
            group = root.addGroup(NOMBRE_GRUPO_RELIEVE)
            QgsLayerDefinition().loadLayerDefinition(PATH_RELIEVE, QgsProject.instance(), rootGroup=group)
            "cargamos QLR al inicio del arbol de capas"
            cloned_group1 = group.clone()
            root.insertChildNode(0, cloned_group1)
            root.removeChildNode(group)
        else:          
            qgis.utils.iface.messageBar().pushMessage("Warning",
                                                      "Las capas :" + NOMBRE_GRUPO_RELIEVE + " ya estan cargadas",
                                                      level=Qgis.Warning,
                                                      duration=30)

    # ******************************************************* MENU CON VENTANA EMERGENTE

    def run_cartografia_cartografia(self):

        dlg_cart = SigCaceresCartografiaCartografia()
        dlg_cart.show()
        result = dlg_cart.exec_()
        if result:
            pass

    def run_servicios_servicios(self):

        dlg_cart = SigCaceresServiciosServicios()
        dlg_cart.show()
        result = dlg_cart.exec_()
        if result:
            pass

    def run_catastro_anterior(self):

        dlg_cat = SigCaceresCatastroAnterior()
        dlg_cat.show()
        result = dlg_cat.exec_()

    def run_movilidad_servicios(self):

        dlg_serv = SigCaceresMovilidadServicios()
        dlg_serv.show()
        result = dlg_serv.exec_()
        if result:
            pass

    def run_infraestructuras(self):

        dlg_inf = SigCaceresInfraestructuras()
        dlg_inf.show()
        result = dlg_inf.exec_()

        if result:
            pass

