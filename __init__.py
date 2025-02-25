# -*- coding: utf-8 -*-



# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SigCaceres class from file SigCaceres.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sig_caceres import SigCaceres
    return SigCaceres(iface)