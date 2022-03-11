# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Test_Klasse
                                 A QGIS plugin
 Beschreibung PlugIn
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-17
        copyright            : (C) 2020 by fxs
        email                : schuetz@hm.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Test_Klasse class from file Test_Klasse.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Modul_Name import Test_Klasse
    return Test_Klasse(iface)