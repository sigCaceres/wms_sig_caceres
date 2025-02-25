# -*- coding: utf-8 -*-
"""
Modulo de rutas a las capas de la aplicacion
"""
__author__ = "SIG Caceres"
__copyright__ = "Copyright 2024, SIG Caceres"
__credits__ = ["SIG Caceres"]

__version__ = "1.1.0"
__maintainer__ = "SIG Cáceres"
__email__ = "https://sig.caceres.es/"
__status__ = "Production"


import os
from ..scr.funciones_util import buscar_archivos_recursivamente


# Se define aqui el nombre del grupo dondes van a cargar  las capas.

# GRUPOS -> CARTOGRAFÍA Y ORTOFOTOS
NOMBRE_GRUPO_ORTOFOTOS = "ORTOFOTOS"
NOMBRE_GRUPO_ORTOFOTOS_HISTORICAS = "Ortofotos Históricas"
NOMBRE_GRUPO_PNOA_ANUAL = "PNOA anual"
NOMBRE_GRUPO_MAPAS_BASE= "Mapas Base"
# GRUPOS -> CARTOGRAFIA Y ORTOFOTOS -> URBANA VECTORIAL
NOMBRE_GRUPO_URBANA_ACTUALIZADA = "Trama Urbana Actualizada"
NOMBRE_GRUPO_URBANA_2012 = "Trama Urbana 2012"
NOMBRE_GRUPO_URBANA_2012_3D = "Trama Urbana 2012 3D"
NOMBRE_GRUPO_URBANA_2003 = "Trama Urbana 2003 1/500"
NOMBRE_GRUPO_URBANA_1996 = "Trama Urbana 1996 1/500"
# GRUPOS -> CARTOGRAFIA Y ORTOFOTOS -> URBANA ESCANEADA
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1900 = "Cartografía Escaneada 1900"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1900_AGUAS = "Cartografía Escaneada 1900 Aguas"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1922 = "Cartografía Escaneada 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1931 = "Cartografía Escaneada 1931"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1942 = "Cartografía Escaneada 1942"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1947 = "Cartografía Escaneada 1947"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1961_E2000 = "Cartografía Escaneada 1961 1/2000"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1971 = "Cartografía Escaneada 1971"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1975 = "Cartografía Escaneada 1975"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1981 = "Cartografía Escaneada 1981"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1984 = "Cartografía Escaneada 1984"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E2000 = "Cartografía Escaneada 1993 1/2000"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E2000T = "Cartografía Escaneada 1993 1/2000 transparente"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E5000 = "Cartografía Escaneada 1993 1/5000"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E5000T = "Cartografía Escaneada 1993 1/5000 transparente"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANIMETRIA_HISTORICA = "Planimetría Histórica"
# GRUPOS -> CARTOGRAFIA Y ORTOFOTOS -> PLANOS ESCANEADOS
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_BAIER_1813 = "Plano Baier 1813"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1845 = "Plano Vicente Maestre 1845"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_COELLO_1853 = "Plano Coello 1853"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_TUBERIAS_1895 = "Plano de Alineación de Tuberías 1895"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_AGUAS_POTABLES_1895 = "Plano de Aguas Potables 1895"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_ALUMBRADO_1895 = "Plano de Alumbrado 1895"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_ENSANCHE_1922 = "Plano Ensanche 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_REFORMA_1922 = "Plano Reforma 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_MANANTIALES_1922 = "Plano de Manantiales de El Marco 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_ZONA_REGABLE_1922 = "Plano de Zonas Regables 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PROYECTO_ALCANTARILLADO_1922 = "Proyecto de Alcantarillado 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PROYECTO_PARQUE_1922 = "Proyecto de Parque 1922"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_DISTRIBUCION_1930 = "Plano de Distribución 1930"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_INSTALACIONES_1930 = "Plano de Instalaciones 1930"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_RED_SUPERIOR_1930 = "Plano de Red Superior especiales 1930"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_CAPTACION_AGUA_1930 = "Captación de Agua 1930"
NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_RIEGO_HUERTAS_1930 = "Riego Huertas 1930"
# GRUPOS -> CARTOGRAFIA Y ORTOFOTOS -> TM VECTORIAL
NOMBRE_GRUPO_TM_2008_E10000 = "Cartografía TM 2008 1/10000"
# GRUPOS -> CARTOGRAFIA Y ORTOFOTOS -> TM ESCANEADA
NOMBRE_GRUPO_MINUTAS_1EDICIONES_E25000 = "Minutas 1ras ediciones 1/25000"
NOMBRE_GRUPO_MINUTAS_1EDICIONES_E50000 = "Minutas 1ras ediciones 1/50000"
NOMBRE_GRUPO_MINUTAS_CATASTRONES = "Minutas MTN50 (catastrones)"
NOMBRE_GRUPO_MTN_RASTER_HD = "MTN RASTER alta definición"
NOMBRE_GRUPO_PLANIMETRIA_HIST_CNIG = "Planimetría Histórica CNIG"
NOMBRE_GRUPO_PLANIMETRIA_HIST_IDECC = "Planimetría Histórica IDE Cáceres"

# GRUPOS -> CALLEJERO Y TOPONIMIA
NOMBRE_GRUPO_CALLEJERO = "CALLEJERO"
NOMBRE_GRUPO_BARRIOS = "BARRIOS"

# GRUPOS -> CATASTRO
NOMBRE_GRUPO_CATASTRO = "CATASTRO"
NOMBRE_GRUPO_CATASTRO_2019 = "CATASTRO 2019"
NOMBRE_GRUPO_CATASTRO_2020 = "CATASTRO 2020"
NOMBRE_GRUPO_SENALIZACION = "SEÑALIZACION"

# GRUPOS -> PLANEAMIENTO
NOMBRE_GRUPO_PGM_2010 = "PGM 2010 actualizado"
NOMBRE_GRUPO_PEPRPA = "Plan Especial (PEPRPA)"
NOMBRE_GRUPO_PGOU_1999 = "PGOU 1999"
NOMBRE_GRUPO_PGOU_1985 = "PGOU 1985"
NOMBRE_GRUPO_PGOU_1961 = "PGOU 1961"
NOMBRE_GRUPO_PD_MURALLA = "Plan Director de la Muralla"
NOMBRE_GRUPO_ORDENES_SECTORIALES = "Ordenes Sectoriales"
NOMBRE_GRUPO_BIC = "BIC"

# GRUPOS -> INFRAESTRUCTURAS
NOMBRE_GRUPO_CONTENEDORES_BASURA = "CONTENEDORES BASURA" 

# GRUPOS -> REDES VIARIAS
NOMBRE_GRUPO_SENALIZACION_VERTICAL = "SEÑALIZACIÓN VERTICAL"
NOMBRE_GRUPO_CARRETERAS = "CARRETERAS"
NOMBRE_GRUPO_FERROCARRIL = "FERROCARRIL"
NOMBRE_GRUPO_PUNTOS_KILOMETRICOS = "PUNTOS KILOMÉTRICOS"
NOMBRE_GRUPO_CARRIL_BICI = "CARRIL BICI"
NOMBRE_GRUPO_VIAS_PECUARIAS = "VIAS PECUARIAS"
NOMBRE_GRUPO_RED_DE_CALLES = "RED DE CALLES"
NOMBRE_GRUPO_CALLES_PEATONALES = "CALLES PEATONALES"
NOMBRE_GRUPO_PINTURA_TRAFICO = "PINTURA TRAFICO"
NOMBRE_GRUPO_ANCHURA_ACERADOS = "ANCHURA ACERADOS"
NOMBRE_GRUPO_GLORIETAS_ISLETAS = "GLORIETAS ISLETAS"
NOMBRE_GRUPO_SENTIDO_CIRCULACION = "SENTIDO CIRCULACION"

# GRUPOS -> MOVILIDAD
NOMBRE_GRUPO_BUS_URBANO = "BUS URBANO"
NOMBRE_GRUPO_APARCAMIENTOS = "APARCAMIENTOS"
NOMBRE_GRUPO_VADOS = "VADOS"
NOMBRE_GRUPO_ZONA_AZUL = "ZONA AZUL"
NOMBRE_GRUPO_PARKING_MOTOS = "PARKING MOTOS"
NOMBRE_GRUPO_MOVILIDAD_REDUCIDA = "MOVILIDAD REDUCIDA"
NOMBRE_GRUPO_PUNTOS_RECARGA = "PUNTOS RECARGA"
NOMBRE_GRUPO_CARGA_DESCARGA = "CARGA Y DESCARGA"
NOMBRE_GRUPO_PASOS_PEATONES = "PASOS DE PEATONES"

# GRUPOS -> PATRIMONIO
NOMBRE_GRUPO_UNESCO_CIUDAD_VIEJA = "UNESCO_CIUDAD_VIEJA"
NOMBRE_GRUPO_INVENTARIO = "INVENTARIO"
NOMBRE_GRUPO_CAMINOS_PUBLICOS = "CAMINOS PÚBLICOS"
NOMBRE_GRUPO_RIBERA_MARCO = "INVENTARIO RIBERA DEL MARCO"
NOMBRE_GRUPO_LIBRO_YERBAS = "LIBRO DE YERBAS"

# GRUPOS -> ARCHIVO HISTORICO
NOMBRE_GRUPO_EXPEDIENTES_OBRA_HISTORICOS = "EXPEDIENTES DE OBRA HISTÓRICOS"
NOMBRE_GRUPO_PADRONES_HISTORICOS = "PADRONES HISTÓRICOS"
NOMBRE_GRUPO_HERALDICAS = "HERÁLDICA"
NOMBRE_GRUPO_FOTOS_HISTORICAS = "FOTOS HISTÓRICAS"
NOMBRE_GRUPO_AUDIOGUIAS = "AUDIOGUÍAS"

# GRUPOS -> SERVICIOS -> CENTROS ADMINISTRATIVOS
NOMBRE_GRUPO_ADMINISTRACION = "Administración"
NOMBRE_GRUPO_BUZONES = "Buzones"
NOMBRE_GRUPO_CEMENTERIOS = "Cementerios"
NOMBRE_GRUPO_CENTROS_EDUCATIVOS = "Centros educativos"
NOMBRE_GRUPO_CENTROS_TECNOLOGICOS = "Centros tecnológicos"
NOMBRE_GRUPO_CORREOS = "Correos"
NOMBRE_GRUPO_CUERPOS_DE_SEGURIDAD = "Cuerpos de seguridad"
NOMBRE_GRUPO_ITV = "ITV"
NOMBRE_GRUPO_TANATORIOS = "Tanatorios" 
# GRUPOS -> SERVICIOS -> CENTROS SANITARIOS
NOMBRE_GRUPO_CENTROS_SALUD = "Centros de salud"
NOMBRE_GRUPO_DESFIBRILADORES = "Desfibriladores"
NOMBRE_GRUPO_FARMACIAS = "Farmacias"
NOMBRE_GRUPO_HOSPITALES = "Hospitales"
NOMBRE_GRUPO_OTROS_CENTROS_SANITARIOS = "Otros centros sanitarios"
NOMBRE_GRUPO_RESIDENCIAS_MAYORES = "Residencias de mayores"
# GRUPOS -> SERVICIOS -> SERVICIOS TURISTICOS
NOMBRE_GRUPO_ALOJAMIENTOS = "Alojamientos"
NOMBRE_GRUPO_AUDIOGUIAS = "Audioguías"
NOMBRE_GRUPO_CENTROS_CULTURALES = "Centros culturales"
NOMBRE_GRUPO_CENTROS_EXPOSICIONES = "Centros de exposiciones y congresos"
NOMBRE_GRUPO_CENTROS_RELIGIOSOS = "Centros religiosos"
NOMBRE_GRUPO_ESCULTURAS = "Esculturas"
NOMBRE_GRUPO_MONUMENTOS = "Monumentos"
NOMBRE_GRUPO_MUSEOS = "Museos"
NOMBRE_GRUPO_OFICINAS_TURISMO = "Oficinas de turismo"
NOMBRE_GRUPO_VIA_PLATA = "Via de la Plata"
# GRUPOS -> SERVICIOS -> OCIO Y ENTRETENIMIENTO
NOMBRE_GRUPO_ARCHIVOS_BIBLIOTECAS = "Archivos y Bibliotecas"
NOMBRE_GRUPO_AAVV = "Asociaciones de Vecinos"
NOMBRE_GRUPO_CENTROS_CIVICOS = "Centros Cívicos"
NOMBRE_GRUPO_CINES_TEATROS = "Cines y Teatros"
NOMBRE_GRUPO_ESTANCOS = "Estancos"
NOMBRE_GRUPO_LOTERIAS = "Loterías"
NOMBRE_GRUPO_SALONES_JUEGOS = "Salones de Juego"
# GRUPOS -> SERVICIOS -> MOBILIARIO URBANO
NOMBRE_GRUPO_BANCOS_ASIENTO = "Bancos Asiento"
NOMBRE_GRUPO_FUENTES_PUBLICAS = "Fuentes Públicas"
NOMBRE_GRUPO_PAPELERAS = "Papeleras"

# GRUPOS -> SERVICIOS
NOMBRE_GRUPO_BEACONS = "Beacons"

# GRUPOS -> PARCELARIOS
NOMBRE_GRUPO_POLIGONO_GANADERO = "Polígono Ganadero"
NOMBRE_GRUPO_FERIAL = "Ferial"

# GRUPOS -> MEDIOAMBIENTE
NOMBRE_GRUPO_ARBOLADO = "Arbolado"
NOMBRE_GRUPO_PARQUES_JARDINES = "Parques y jardines"

# GRUPOS -> TEMATICOS
NOMBRE_GRUPO_FOTOVOLTAICAS = "FOTOVOLTAICAS"
NOMBRE_GRUPO_GEOLOGICO_MINERO = "Mapa Geológico Minero"
NOMBRE_GRUPO_MAPA_PENDIENTES = "Mapa de Pendientes"
NOMBRE_GRUPO_RELIEVE = "Relieve"

# Se define aqui el path de carga al archivo fuente de los estilos, con esto carga todas las capas.
# ESTE ES UN CASO PARTICULAR DE CARGAR TODAS LAS IMAGENES QUE SE ENCUENTRAN EN UN DIRECTORIO A PARTIR DE SU ARCHIVO <<QLR>>

ruta = os.path.dirname(__file__)

# RUTA -> CARTOGRAFIA Y ORTOFOTOS
PATH_ORTOFOTOS = os.path.join(ruta, "qlr", "_ortofotos.qlr")
PATH_ORTOFOTOS_HISTORICAS = os.path.join(ruta, "qlr", "_ortofotos_historicas.qlr")
PATH_PNOA_ANUAL = os.path.join(ruta, "qlr", "_PNOA_anual.qlr")
PATH_MAPAS_BASE = os.path.join(ruta, "qlr", "_mapas_base.qlr")
# RUTA -> CARTOGRAFIA Y ORTOFOTOS -> URBANA VECTORIAL
PATH_URBANA_ACTUALIZADA = os.path.join(ruta, "qlr", "_trama_urbana_actualizada.qlr")
PATH_URBANA_2012 = os.path.join(ruta, "qlr", "_trama_urbana_2012.qlr")
PATH_URBANA_2012_3D = os.path.join(ruta, "qlr", "_trama_urbana_2012_3D.qlr")
PATH_URBANA_2003 = os.path.join(ruta, "qlr", "_cartografia_urbana_2003_e500")
PATH_URBANA_1996 = os.path.join(ruta, "qlr", "_cartografia_urbana_1996_e500")
# RUTA -> CARTOGRAFIA Y ORTOFOTOS -> URBANA ESCANEADA
PATH_CARTOGRAFIA_ESCANEADA_1900 = os.path.join(ruta, "qlr", "_Caceres_1900.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1900_AGUAS = os.path.join(ruta, "qlr", "_Caceres_1900_aguas.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1922 = os.path.join(ruta, "qlr", "_Caceres_1922_proy_alcantarillado.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1931 = os.path.join(ruta, "qlr", "_Caceres_1931.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1942 = os.path.join(ruta, "qlr", "_Caceres_1942.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1947 = os.path.join(ruta, "qlr", "_Caceres_1947.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1961_E2000 = os.path.join(ruta, "qlr", "_Caceres_1961_e2000.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1971 = os.path.join(ruta, "qlr", "_Caceres_1971.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1975 = os.path.join(ruta, "qlr", "_Caceres_1975.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1981 = os.path.join(ruta, "qlr", "_Caceres_1981.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1984 = os.path.join(ruta, "qlr", "_Caceres_1984.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1993_E2000 = os.path.join(ruta, "qlr", "_Caceres_1993_e2000.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1993_E2000T = os.path.join(ruta, "qlr", "_Caceres_1993_e2000_transparencia.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1993_E5000 = os.path.join(ruta, "qlr", "_Caceres_1993_e5000.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1993_E5000T = os.path.join(ruta, "qlr", "_Caceres_1993_e5000_transparencia.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANIMETRIA_HISTORICA = os.path.join(ruta, "qlr", "_planimetria_historica.qlr")
# RUTA -> CARTOGRAFIA Y ORTOFOTOS -> PLANOS ESCANEADOS
PATH_CARTOGRAFIA_ESCANEADA_PLANO_BAIER_1813 = os.path.join(ruta, "qlr", "_plano_baier_1813.qlr")
PATH_CARTOGRAFIA_ESCANEADA_1845 = os.path.join(ruta, "qlr", "_Caceres_1845.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_COELLO_1853 = os.path.join(ruta, "qlr", "_plano_coello_1853.qlr")
PATH_CARTOGRAFIA_ESCANEADA_TUBERIAS_1895 = os.path.join(ruta, "qlr", "_alineacion_tuberias_1895.qlr")
PATH_CARTOGRAFIA_ESCANEADA_AGUAS_POTABLES_1895 = os.path.join(ruta, "qlr", "_plano_aguas_potables_1895.qlr")
PATH_CARTOGRAFIA_ESCANEADA_ALUMBRADO_1895 = os.path.join(ruta, "qlr", "_plano_alumbrado_1895.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_ENSANCHE_1922 = os.path.join(ruta, "qlr", "_plano_ensanche_1922.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_REFORMA_1922 = os.path.join(ruta, "qlr", "_plano_reforma_1922.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_MANANTIALES_1922 = os.path.join(ruta, "qlr", "_plano_manantiales_elmarco_1922.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_ZONA_REGABLE_1922 = os.path.join(ruta, "qlr", "_plano_zona_regable_1922.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PROYECTO_ALCANTARILLADO_1922 = os.path.join(ruta, "qlr", "_proyecto_alcantarillado_1922.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PROYECTO_PARQUE_1922 = os.path.join(ruta, "qlr", "_proyecto_parque_1922.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_DISTRIBUCION_1930 = os.path.join(ruta, "qlr", "_plano_distribucion_1930.qlr")
PATH_CARTOGRAFIA_ESCANEADA_PLANO_INSTALACIONES_1930 = os.path.join(ruta, "qlr", "_plano_instalaciones_1930.qlr")
PATH_CARTOGRAFIA_ESCANEADA_RED_SUPERIOR_1930 = os.path.join(ruta, "qlr", "_plano_instalaciones_1930.qlr")
PATH_CARTOGRAFIA_ESCANEADA_CAPTACION_AGUA_1930 = os.path.join(ruta, "qlr", "_captacion_agua_1930.qlr")
PATH_CARTOGRAFIA_ESCANEADA_RIEGO_HUERTAS_1930 = os.path.join(ruta, "qlr", "_riego_huertas_1930.qlr")
# RUTA -> CARTOGRAFIA Y ORTOFOTOS -> TM VECTORIAL
PATH_TM_2008_E10000 = os.path.join(ruta, "qlr", "_cartografia_TM_2008_e10000.qlr")
# RUTA -> CARTOGRAFIA Y ORTOFOTOS -> TM ESCANEADA
PATH_MINUTAS_1EDICIONES_E25000 = os.path.join(ruta, "qlr", "_minutas_1ras_ediciones_e25000.qlr")
PATH_MINUTAS_1EDICIONES_E50000 = os.path.join(ruta, "qlr", "_minutas_1ras_ediciones_e50000.qlr")
PATH_MINUTAS_CATASTRONES = os.path.join(ruta, "qlr", "_minutas_MTN50_catastrones.qlr")
PATH_MTN_RASTER_HD = os.path.join(ruta, "qlr", "_MTN_RASTER_alta_definicion.qlr")
PATH_PLANIMETRIA_HIST_CNIG = os.path.join(ruta, "qlr", "_planimetria_historica_CNIG.qlr")
PATH_PLANIMETRIA_HIST_IDECC = os.path.join(ruta, "qlr", "_planimetria_historica_IDE_Caceres.qlr")

# RUTA -> CALLEJERO Y TOPONIMIA
PATH_CALLEJERO = os.path.join(ruta, "qlr", "_callejero.qlr")
PATH_BARRIOS = os.path.join(ruta, "qlr", "_barrios.qlr")

# RUTA -> PLANEAMIENTO
PATH_CATASTRO = os.path.join(ruta, "qlr", "_catastro.qlr")
PATH_PGM_2010 = os.path.join(ruta, "qlr", "_pgm_2010_actualizado.qlr")
PATH_PE_PEPRPA = os.path.join(ruta, "qlr", "_plan_especial.qlr")
PATH_PGOU_1999 = os.path.join(ruta, "qlr", "_pgou_1999.qlr")
PATH_PGOU_1985 = os.path.join(ruta, "qlr", "_pgou_1985.qlr")
PATH_PGOU_1961 = os.path.join(ruta, "qlr", "_pgou_1961.qlr")
PATH_PD_MURALLA = os.path.join(ruta, "qlr", "_plan_director_de_la_muralla.qlr")
PATH_BIC = os.path.join(ruta, "qlr", "_bic.qlr")

#RUTA -> INFRAESTRUCTURAS
PATH_CONTENEDORES_BASURA = os.path.join(ruta, "qlr", "_contenedores.qlr")

# RUTA -> REDES VIARIAS
PATH_CARRETERAS = os.path.join(ruta, "qlr", "_carreteras.qlr")
PATH_FERROCARRIL = os.path.join(ruta, "qlr", "_ferrocarril.qlr")
PATH_PUNTOS_KILOMETRICOS = os.path.join(ruta, "qlr", "_puntos_kilometricos.qlr")
PATH_CARRIL_BICI = os.path.join(ruta, "qlr", "_red_carriles_bici.qlr")
PATH_VIAS_PECUARIAS = os.path.join(ruta, "qlr", "_vias_pecuarias.qlr")
PATH_RED_DE_CALLES = os.path.join(ruta, "qlr", "_red_de_calles.qlr")
PATH_CALLES_PEATONALES = os.path.join(ruta, "qlr", "_calles_peatonales.qlr")
PATH_PINTURA_TRAFICO = os.path.join(ruta, "qlr", "_pintura_trafico.qlr")
PATH_ANCHURA_ACERADOS = os.path.join(ruta, "qlr", "_anchura_acerados.qlr")
PATH_GLORIETAS_ISLETAS = os.path.join(ruta, "qlr", "_glorietas.qlr")
PATH_SENTIDO_CIRCULACION = os.path.join(ruta, "qlr", "_sentido_circulacion.qlr")

# RUTA -> MOVILIDAD
PATH_BUS_URBANO = os.path.join(ruta, "qlr", "_bus_urbano.qlr")
PATH_APARCAMIENTOS = os.path.join(ruta, "qlr", "_aparcamientos.qlr")
PATH_ZONA_AZUL = os.path.join(ruta, "qlr", "_zona_azul.qlr")
PATH_PARKING_MOTOS = os.path.join(ruta, "qlr", "_parking_motos.qlr")
PATH_MOVILIDAD_REDUCIDA = os.path.join(ruta, "qlr", "_PMR.qlr")
PATH_PUNTOS_RECARGA = os.path.join(ruta, "qlr", "_puntos_recarga.qlr")
PATH_CARGA_DESCARGA = os.path.join(ruta, "qlr", "_carga_y_descarga.qlr")
PATH_PASOS_PEATONES = os.path.join(ruta, "qlr", "_pasos_peatones.qlr")

# RUTA -> PATRIMONIO
PATH_UNESCO_CIUDAD_VIEJA = os.path.join(ruta, "qlr", "_unesco_ciudad_vieja.qlr")
PATH_INVENTARIO = os.path.join(ruta, "qlr", "_inventario_actual.qlr")
PATH_CAMINOS_PUBLICOS = os.path.join(ruta, "qlr", "_catalogo_caminos_publicos.qlr")
PATH_RIBERA_MARCO = os.path.join(ruta, "qlr", "_inventario_ribera_del_marco.qlr")
PATH_LIBRO_YERBAS = os.path.join(ruta, "qlr", "_libro_yerbas.qlr")

# RUTA -> ARCHIVO HISTORICO
PATH_EXPEDIENTES_OBRA_HISTORICOS = os.path.join(ruta, "qlr", "_expedientes_obra_historicos.qlr")
PATH_PADRONES_HISTORICOS = os.path.join(ruta, "qlr", "_padrones_historicos.qlr")
PATH_HERALDICA = os.path.join(ruta, "qlr", "_escudos.qlr")
PATH_FOTOS_HISTORICAS = os.path.join(ruta, "qlr", "_fotos_historicas.qlr")
PATH_AUDIOGUIAS = os.path.join(ruta, "qlr", "_audioguias.qlr")

# RUTA -> SERVICIOS -> CENTROS ADMINISTRATIVOS
PATH_ADMINISTRACION = os.path.join(ruta, "qlr", "_administracion.qlr")
PATH_BUZONES = os.path.join(ruta, "qlr", "_buzones.qlr")
PATH_CEMENTERIOS = os.path.join(ruta, "qlr", "_cementerios.qlr")
PATH_CENTROS_EDUCATIVOS = os.path.join(ruta, "qlr", "_centros_educativos.qlr")
PATH_CENTROS_TECNOLOGICOS = os.path.join(ruta, "qlr", "_centros_tecnologicos.qlr")
PATH_CORREOS = os.path.join(ruta, "qlr", "_correos.qlr")
PATH_CUERPOS_DE_SEGURIDAD = os.path.join(ruta, "qlr", "_cuerpos_de_seguridad.qlr")
PATH_ITV = os.path.join(ruta, "qlr", "_itv.qlr")
PATH_TANATORIOS = os.path.join(ruta, "qlr", "_tanatorios.qlr")
# RUTA -> SERVICIOS -> CENTROS SANITARIOS
PATH_CENTROS_SALUD = os.path.join(ruta, "qlr", "_centros_salud.qlr")
PATH_DESFIBRILADORES = os.path.join(ruta, "qlr", "_desfibriladores.qlr")
PATH_FARMACIAS = os.path.join(ruta, "qlr", "_farmacias.qlr")
PATH_HOSPITALES = os.path.join(ruta, "qlr", "_hospitales.qlr")
PATH_OTROS_CENTROS_SANITARIOS = os.path.join(ruta, "qlr", "_otros_centros_sanitarios.qlr")
PATH_RESIDENCIAS_MAYORES = os.path.join(ruta, "qlr", "_residencias_mayores.qlr")
# RUTA -> SERVICIOS -> SERVICIOS TURISTICOS
PATH_ALOJAMIENTOS = os.path.join(ruta, "qlr", "_alojamientos.qlr")
PATH_AUDIOGUIAS = os.path.join(ruta, "qlr", "_audioguias.qlr")
PATH_CENTROS_CULTURALES = os.path.join(ruta, "qlr", "_centros_culturales.qlr")
PATH_CENTROS_RELIGIOSOS = os.path.join(ruta, "qlr", "_centros_religiosos.qlr")
PATH_ESCULTURAS = os.path.join(ruta, "qlr", "_esculturas.qlr")
PATH_MONUMENTOS = os.path.join(ruta, "qlr", "_monumentos.qlr")
PATH_MUSEOS = os.path.join(ruta, "qlr", "_museos.qlr")
PATH_OFICINAS_TURISMO = os.path.join(ruta, "qlr", "_oficinas_turismo.qlr")
PATH_VIA_PLATA = os.path.join(ruta, "qlr", "_via_plata.qlr")
# RUTA -> SERVICIOS -> OCIO Y ENTRETENIMIENTO
PATH_ARCHIVOS_BIBLIOTECAS= os.path.join(ruta, "qlr", "_archivos_bibliotecas.qlr")
PATH_AAVV = os.path.join(ruta, "qlr", "_asociaciones_vecinos.qlr")
PATH_CENTROS_CIVICOS= os.path.join(ruta, "qlr", "_centros_civicos.qlr")
PATH_CINES_TEATROS = os.path.join(ruta, "qlr", "_cines_teatros.qlr")
PATH_ESTANCOS = os.path.join(ruta, "qlr", "_estancos.qlr")
PATH_LOTERIAS = os.path.join(ruta, "qlr", "_loterias.qlr")
PATH_SALONES_JUEGO = os.path.join(ruta, "qlr", "_salones_juego.qlr")
# RUTA -> SERVICIOS -> MOBILIARIO URBANO
PATH_BANCOS_ASIENTO = os.path.join(ruta, "qlr", "_banco_asiento.qlr")
PATH_FUENTES_PUBLICAS = os.path.join(ruta, "qlr", "_fuentes_publicas.qlr")
PATH_PAPELERAS = os.path.join(ruta, "qlr", "_papeleras.qlr")

# RUTA -> SERVICIOS
PATH_BEACONS = os.path.join(ruta, "qlr", "_beacons.qlr")

# RUTA -> PARCELARIOS
PATH_POLIGONO_GANADERO = os.path.join(ruta, "qlr", "_parcelario_polig_ganadero.qlr")
PATH_FERIAL = os.path.join(ruta, "qlr", "_ferial.qlr")

# RUTA -> MEDIOAMBIENTE
PATH_ARBOLADO = os.path.join(ruta, "qlr", "_arbolado.qlr")
PATH_PARQUES_JARDINES = os.path.join(ruta, "qlr", "_parques_jardines.qlr")

# RUTA -> TEMATICOS
PATH_GEOLOGICO_MINERO = os.path.join(ruta, "qlr", "_mapa_geologico_minero.qlr")
PATH_MAPA_PENDIENTES = os.path.join(ruta, "qlr", "_mapa_de_pendientes.qlr")
PATH_RELIEVE = os.path.join(ruta, "qlr", "_relieve.qlr")

# ******************************** ASIGNACIÓN PARA DESPLEGABLE VENTANA EMERGENTE CARTOGRAFIA

# listado de capas de urbana vectorial

urbana_vectorial={}
urbana_vectorial[NOMBRE_GRUPO_URBANA_ACTUALIZADA]={"path":PATH_URBANA_ACTUALIZADA}
urbana_vectorial[NOMBRE_GRUPO_URBANA_2012]={"path":PATH_URBANA_2012}
urbana_vectorial[NOMBRE_GRUPO_URBANA_2012_3D]={"path":PATH_URBANA_2012_3D}
urbana_vectorial[NOMBRE_GRUPO_URBANA_2003]={"path":PATH_URBANA_2003}
urbana_vectorial[NOMBRE_GRUPO_URBANA_1996]={"path":PATH_URBANA_1996}

# listado de capas de urbana vectorial

urbana_escaneada={}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1900]={"path":PATH_CARTOGRAFIA_ESCANEADA_1900}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1900_AGUAS]={"path":PATH_CARTOGRAFIA_ESCANEADA_1900_AGUAS}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_1922}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1931]={"path":PATH_CARTOGRAFIA_ESCANEADA_1931}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1942]={"path":PATH_CARTOGRAFIA_ESCANEADA_1942}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1947]={"path":PATH_CARTOGRAFIA_ESCANEADA_1947}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1961_E2000]={"path":PATH_CARTOGRAFIA_ESCANEADA_1961_E2000}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1971]={"path":PATH_CARTOGRAFIA_ESCANEADA_1971}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1975]={"path":PATH_CARTOGRAFIA_ESCANEADA_1975}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1981]={"path":PATH_CARTOGRAFIA_ESCANEADA_1981}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1984]={"path":PATH_CARTOGRAFIA_ESCANEADA_1984}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E2000]={"path":PATH_CARTOGRAFIA_ESCANEADA_1993_E2000}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E2000T]={"path":PATH_CARTOGRAFIA_ESCANEADA_1993_E2000T}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E5000]={"path":PATH_CARTOGRAFIA_ESCANEADA_1993_E5000}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1993_E5000T]={"path":PATH_CARTOGRAFIA_ESCANEADA_1993_E5000T}
urbana_escaneada[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANIMETRIA_HISTORICA]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANIMETRIA_HISTORICA}

# listado de capas de planos escaneados

Planos_escaneados={}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_BAIER_1813]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_BAIER_1813}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_1845]={"path":PATH_CARTOGRAFIA_ESCANEADA_1845}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_COELLO_1853]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_COELLO_1853}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_TUBERIAS_1895]={"path":PATH_CARTOGRAFIA_ESCANEADA_TUBERIAS_1895}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_AGUAS_POTABLES_1895]={"path":PATH_CARTOGRAFIA_ESCANEADA_AGUAS_POTABLES_1895}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_ALUMBRADO_1895]={"path":PATH_CARTOGRAFIA_ESCANEADA_ALUMBRADO_1895}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_ENSANCHE_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_ENSANCHE_1922}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_REFORMA_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_REFORMA_1922}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_MANANTIALES_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_MANANTIALES_1922}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_ZONA_REGABLE_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_ZONA_REGABLE_1922}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PROYECTO_ALCANTARILLADO_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_PROYECTO_ALCANTARILLADO_1922}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PROYECTO_PARQUE_1922]={"path":PATH_CARTOGRAFIA_ESCANEADA_PROYECTO_PARQUE_1922}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_DISTRIBUCION_1930]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_DISTRIBUCION_1930}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_PLANO_INSTALACIONES_1930]={"path":PATH_CARTOGRAFIA_ESCANEADA_PLANO_INSTALACIONES_1930}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_RED_SUPERIOR_1930]={"path":PATH_CARTOGRAFIA_ESCANEADA_RED_SUPERIOR_1930}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_CAPTACION_AGUA_1930]={"path":PATH_CARTOGRAFIA_ESCANEADA_CAPTACION_AGUA_1930}
Planos_escaneados[NOMBRE_GRUPO_CARTOGRAFIA_ESCANEADA_RIEGO_HUERTAS_1930]={"path":PATH_CARTOGRAFIA_ESCANEADA_RIEGO_HUERTAS_1930}

# listado de capas de TM vectorial

TM_vectorial={}
TM_vectorial[NOMBRE_GRUPO_TM_2008_E10000]={"path":PATH_TM_2008_E10000}

# listado de capas de TM escanedada

TM_escaneada={}
TM_escaneada[NOMBRE_GRUPO_MINUTAS_1EDICIONES_E25000]={"path":PATH_MINUTAS_1EDICIONES_E25000}
TM_escaneada[NOMBRE_GRUPO_MINUTAS_1EDICIONES_E50000]={"path":PATH_MINUTAS_1EDICIONES_E50000}
TM_escaneada[NOMBRE_GRUPO_MINUTAS_CATASTRONES]={"path":PATH_MINUTAS_CATASTRONES}
TM_escaneada[NOMBRE_GRUPO_MTN_RASTER_HD]={"path":PATH_MTN_RASTER_HD}
TM_escaneada[NOMBRE_GRUPO_PLANIMETRIA_HIST_IDECC]={"path":PATH_PLANIMETRIA_HIST_IDECC}
TM_escaneada[NOMBRE_GRUPO_PLANIMETRIA_HIST_CNIG]={"path":PATH_PLANIMETRIA_HIST_CNIG}

# ******************************** ASIGNACIÓN PARA DESPLEGABLE VENTANA EMERGENTE CARTOGRAFIA

# listado de capas de centros administrativos

centrosadministrativos={}
centrosadministrativos[NOMBRE_GRUPO_ADMINISTRACION]={"path":PATH_ADMINISTRACION}
centrosadministrativos[NOMBRE_GRUPO_BUZONES]={"path":PATH_BUZONES}
centrosadministrativos[NOMBRE_GRUPO_CEMENTERIOS]={"path":PATH_CEMENTERIOS}
centrosadministrativos[NOMBRE_GRUPO_CENTROS_EDUCATIVOS]={"path":PATH_CENTROS_EDUCATIVOS}
centrosadministrativos[NOMBRE_GRUPO_CENTROS_TECNOLOGICOS]={"path":PATH_CENTROS_TECNOLOGICOS}
centrosadministrativos[NOMBRE_GRUPO_CORREOS]={"path":PATH_CORREOS}
centrosadministrativos[NOMBRE_GRUPO_CUERPOS_DE_SEGURIDAD]={"path":PATH_CUERPOS_DE_SEGURIDAD}
centrosadministrativos[NOMBRE_GRUPO_ITV]={"path":PATH_ITV}
centrosadministrativos[NOMBRE_GRUPO_TANATORIOS]={"path":PATH_TANATORIOS}

# listado de capas de centros sanitarios

centrossanitarios={}
centrossanitarios[NOMBRE_GRUPO_CENTROS_SALUD]={"path":PATH_CENTROS_SALUD}
centrossanitarios[NOMBRE_GRUPO_DESFIBRILADORES]={"path":PATH_DESFIBRILADORES}
centrossanitarios[NOMBRE_GRUPO_FARMACIAS]={"path":PATH_FARMACIAS}
centrossanitarios[NOMBRE_GRUPO_HOSPITALES]={"path":PATH_HOSPITALES}
centrossanitarios[NOMBRE_GRUPO_OTROS_CENTROS_SANITARIOS]={"path":PATH_OTROS_CENTROS_SANITARIOS}
centrossanitarios[NOMBRE_GRUPO_RESIDENCIAS_MAYORES]={"path":PATH_RESIDENCIAS_MAYORES}

# listado de capas de servicios turisticos

serviciosturisticos={}
serviciosturisticos[NOMBRE_GRUPO_ALOJAMIENTOS]={"path":PATH_ALOJAMIENTOS}
serviciosturisticos[NOMBRE_GRUPO_MONUMENTOS]={"path":PATH_MONUMENTOS}
serviciosturisticos[NOMBRE_GRUPO_ESCULTURAS]={"path":PATH_ESCULTURAS}
serviciosturisticos[NOMBRE_GRUPO_MUSEOS]={"path":PATH_MUSEOS}
serviciosturisticos[NOMBRE_GRUPO_CENTROS_RELIGIOSOS]={"path":PATH_CENTROS_RELIGIOSOS}
serviciosturisticos[NOMBRE_GRUPO_CENTROS_CULTURALES]={"path":PATH_CENTROS_CULTURALES}
serviciosturisticos[NOMBRE_GRUPO_VIA_PLATA]={"path":PATH_VIA_PLATA}
serviciosturisticos[NOMBRE_GRUPO_OFICINAS_TURISMO]={"path":PATH_OFICINAS_TURISMO}
serviciosturisticos[NOMBRE_GRUPO_AUDIOGUIAS]={"path":PATH_AUDIOGUIAS}

# listado de capas de ocio y entretenimiento

ocio_entretenimiento={}
ocio_entretenimiento[NOMBRE_GRUPO_ARCHIVOS_BIBLIOTECAS]={"path":PATH_ARCHIVOS_BIBLIOTECAS}
ocio_entretenimiento[NOMBRE_GRUPO_AAVV]={"path":PATH_AAVV}
ocio_entretenimiento[NOMBRE_GRUPO_CENTROS_CIVICOS]={"path":PATH_CENTROS_CIVICOS}
ocio_entretenimiento[NOMBRE_GRUPO_CINES_TEATROS]={"path":PATH_CINES_TEATROS}
ocio_entretenimiento[NOMBRE_GRUPO_ESTANCOS]={"path":PATH_ESTANCOS}
ocio_entretenimiento[NOMBRE_GRUPO_LOTERIAS]={"path":PATH_LOTERIAS}
ocio_entretenimiento[NOMBRE_GRUPO_SALONES_JUEGOS]={"path":PATH_SALONES_JUEGO}

# listado de capas de mobiliario urbano

mobiliario_urbano={}
mobiliario_urbano[NOMBRE_GRUPO_BANCOS_ASIENTO]={"path":PATH_BANCOS_ASIENTO}
mobiliario_urbano[NOMBRE_GRUPO_FUENTES_PUBLICAS]={"path":PATH_FUENTES_PUBLICAS}
mobiliario_urbano[NOMBRE_GRUPO_PAPELERAS]={"path":PATH_PAPELERAS}