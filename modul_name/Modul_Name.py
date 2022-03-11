# -*- coding: utf-8 -*-

from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
# fxs 27.12.2020 QLineEdit neu in import
from qgis.PyQt.QtWidgets import QAction, QDialog, QPushButton, QDialogButtonBox, QLineEdit

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Modul_Name_dialog import Test_KlasseDialog
import os.path
import math
import sys
#import shapefile
import struct
import numpy
import matplotlib.pyplot as plot
from scipy.spatial import Delaunay, delaunay_plot_2d
#import vispy # di05012021

#import numpy as np  # di05012021
#from vispy import app  # di05012021
#from vispy import gloo  # di05012021

class Test_Klasse:
    """QGIS Plugin Implementation."""

    def read_shp(self, path):
        P = []

        with shapefile.Reader(path) as shape_file:
            print('Shapetype: ' + str(shape_file.shapeType))  # fxs neu 13.12.2021 
            if shape_file.shapeType == 5: # Polygon
                print('Polygon')
            elif shape_file.shapeType == 1: # Point
                print('Point')
                geom = shape_file.shapes()
                for feature in geom:
                    for coords in feature.points:
                        x, y = coords[0], coords[1]
                        print(x,y)
                        p =[x,y]
                        P.append(p)
                        
            elif shape_file.shapeType == 8: # Multipoint
                print('MultiPoint')
                
            elif shape_file.shapeType == 11: # fxs neu 13.12.2021
                zaehler = 0
                print('PointZ')
                geom = shape_file.shapes()
                for feature in geom:
                    for coords in feature.points:
                        x, y = coords[0], coords[1]
                        print(str(zaehler) + '.')
                        print(x,y)
                        zaehler = zaehler+1
        return P

    # Aus: ESRI Shapefile Technical Description
    # An ESRI White Paper—July 1998
    # Seite 4
    ShapeType = {
        0: 'Null Shape',
        1: 'Point',
        3: 'PolyLine',
        5: 'Polygon',
        8: 'MultiPoint',
        11: 'PointZ',
        13: 'PolyLineZ',
        15: 'PolygonZ',
        18: 'MultiPointZ',
        21: 'PointM',
        23: 'PolyLineM',
        25: 'PolygonM',
        28: 'MultiPointM',
        31: 'MultiPatch'
    }


    # liest aus einer Binaerdatei und gibt shapeType zurueck
    # vgl. whitepaper S. 4
    def lies_shapetype_an_Byte32(self, b_datei):
        # an Position 32 springen
        b_datei.seek(32)
        # Die folgenden 4 Bytes auslesen
        # In Integer umwandeln
        shapeType = struct.unpack('<i', b_datei.read(4))[0]
        # ShapeType finden und ausgeben
        return self.ShapeType[shapeType]

    # liest BoundingBox as (xmin,ymin,xmax,ymax)
    def getBBox(self, b_datei):
        b_datei.seek(36)
        bbox = struct.unpack('<4d', b_datei.read(32))
        return bbox

    #def toggleDarkMode(self):
        #self.dlg.Test_KlasseDialogBase.setColor("white")

    def ear_clip(self):
        #punkte = numpy.array([[0, 0], [10, 10], [10, 15], [3, 15], [1, 10], [0, 0]])
        punkte = []
        if self.dlg.lineEdit_1.text() and self.dlg.lineEdit_2.text():
            punkte.append([int(self.dlg.lineEdit_1.text()),int(self.dlg.lineEdit_2.text())])
        if self.dlg.lineEdit_3.text() and self.dlg.lineEdit_4.text():
            punkte.append([int(self.dlg.lineEdit_3.text()),int(self.dlg.lineEdit_4.text())])
        if self.dlg.lineEdit_5.text() and self.dlg.lineEdit_6.text():
            punkte.append([int(self.dlg.lineEdit_5.text()),int(self.dlg.lineEdit_6.text())])
        if self.dlg.lineEdit_7.text() and self.dlg.lineEdit_8.text():
            punkte.append([int(self.dlg.lineEdit_7.text()),int(self.dlg.lineEdit_8.text())])
        if self.dlg.lineEdit_9.text() and self.dlg.lineEdit_10.text():
            punkte.append([int(self.dlg.lineEdit_9.text()),int(self.dlg.lineEdit_10.text())])
        if self.dlg.lineEdit_11.text() and self.dlg.lineEdit_12.text():
            punkte.append([int(self.dlg.lineEdit_11.text()),int(self.dlg.lineEdit_12.text())])
        if self.dlg.lineEdit_13.text() and self.dlg.lineEdit_14.text():
            punkte.append([int(self.dlg.lineEdit_13.text()),int(self.dlg.lineEdit_14.text())])
        if self.dlg.lineEdit_15.text() and self.dlg.lineEdit_16.text():
            punkte.append([int(self.dlg.lineEdit_15.text()),int(self.dlg.lineEdit_16.text())])
        if self.dlg.lineEdit_17.text() and self.dlg.lineEdit_18.text():
            punkte.append([int(self.dlg.lineEdit_17.text()),int(self.dlg.lineEdit_18.text())])
        if self.dlg.lineEdit_19.text() and self.dlg.lineEdit_20.text():
            punkte.append([int(self.dlg.lineEdit_19.text()),int(self.dlg.lineEdit_20.text())])
        if self.dlg.lineEdit_21.text() and self.dlg.lineEdit_22.text():
            punkte.append([int(self.dlg.lineEdit_21.text()),int(self.dlg.lineEdit_22.text())])
        if self.dlg.lineEdit_23.text() and self.dlg.lineEdit_24.text():
            punkte.append([int(self.dlg.lineEdit_23.text()),int(self.dlg.lineEdit_24.text())])
        punkte = numpy.array(punkte)
        print('Polygon mit ' + str(len(punkte)) + ' Punkten')
        
        tri = Delaunay(punkte)
        tri.simplices 
        print('Erzeugte Dreiecksflächen: ' + str(len(punkte[tri.simplices])))
        #plot.plot(int(self.dlg.lineEdit_25.text()), int(self.dlg.lineEdit_26.text()), color="green", markersize = 12)
        _ = delaunay_plot_2d(tri)
        #hier
        plot.title('Earclip')
        plot.show()
        self.dlg.label_18.setText("Erzeugte Dreiecksflächen:")
        self.dlg.Ergebnis_3.setText(str(len(punkte[tri.simplices])))
        
        
        


    def berechne_route_nach_dijkstra(self, Netzwerk_Knoten_und_Kanten, start_und_zielpunkt, zielpunkt, punkt_geprueft=[], entfernungen={}, vorgaenger={}):
        """ Berechnung des kuezesten Pfades aus start_und_zielpunkt
        """    
        # Schauen, ob Start- und Zielpunkt überhaupt im Netzwerk enthalten sind 
        if start_und_zielpunkt not in Netzwerk_Knoten_und_Kanten:
            raise TypeError('Start- und/oder Zielpunkt nicht vorhanden')
        if zielpunkt not in Netzwerk_Knoten_und_Kanten:
            raise TypeError('Zielpunkt kann nicht gefunden werden')    
        # falls alle Punkte geprüft und Zielpunkt erreicht, dann kürzesten Pfad auslesen und die mit den
        #    Schlüsseln verbundenen Werte für die Weglänge zusammenzählen und ausgeben
        if start_und_zielpunkt == zielpunkt:
            # Kürzesten Pfad bestimmen und anzeigen
            weg_pfad=[]
            variable_fuer_vorgaenger=zielpunkt
            while variable_fuer_vorgaenger != None:
                
                variable_fuer_vorgaenger=vorgaenger.get(variable_fuer_vorgaenger,None)
            print(" Länge (in Einheiten): "+str(entfernungen[zielpunkt]) + " -> Kürzester Weg: "+str(weg_pfad))
        else :     
            # Zu Beginn alle Entfernungen auf 0 setzen
            if not punkt_geprueft: 
                entfernungen[start_und_zielpunkt]=0
            # Dann Nachbarpunkt besuchen und Entfernungen merken
            for nachbarpunkt in Netzwerk_Knoten_und_Kanten[start_und_zielpunkt] :
                if nachbarpunkt not in punkt_geprueft:
                    neue_entfernung = entfernungen[start_und_zielpunkt] + Netzwerk_Knoten_und_Kanten[start_und_zielpunkt][nachbarpunkt]
      
                    if neue_entfernung < entfernungen.get(nachbarpunkt,float('inf')):
                        entfernungen[nachbarpunkt] = neue_entfernung
                        vorgaenger[nachbarpunkt] = start_und_zielpunkt
        
            punkt_geprueft.append(start_und_zielpunkt)
            ungeprueft={}
            for k in Netzwerk_Knoten_und_Kanten:
                if k not in punkt_geprueft:
                    ungeprueft[k] = entfernungen.get(k,float('inf'))        
            nd=min(ungeprueft, key=ungeprueft.get)
            self.berechne_route_nach_dijkstra(Netzwerk_Knoten_und_Kanten,nd,zielpunkt,punkt_geprueft,entfernungen,vorgaenger)
        self.dlg.label_17.setText("Der kürzeste Weg ist:")
        self.dlg.Ergebnis_2.setText(str(weg_pfad)[1:len(str(weg_pfad))-1])
    
    def wurzel(self, x):
        return x * x

    def entfernung(self, p0, p1):
        return self.wurzel(p0[0] - p1[0]) + self.wurzel(p0[1] - p1[1])

    def minimaler_Abstand(self, P):
        n = len(P)
        return math.sqrt(self.minimalen_Abstand_berechnen(P, n))

    last_i = 0
    last_j = 0

    def minimalen_Abstand_berechnen(self, P, n):
        if n == 2:
            return self.entfernung(P[0], P[1])
        if n == 3:
            return min(self.entfernung(P[0], P[1]), self.entfernung(P[0], P[2]), self.entfernung(P[1], P[2]))

        mid = n // 2
        dl = self.minimalen_Abstand_berechnen(P[:mid], mid)
        dr = self.minimalen_Abstand_berechnen(P[mid:], n - mid)

        aktueller_MinAbstand = min(dl, dr)
        MinSoFar = math.sqrt(aktueller_MinAbstand) 

        mid_x = P[mid][0]
        strip = []
        strip_length = 0
        for i in range(n):
            p = P[i]
            if abs(p[0] - mid_x) < MinSoFar:
                strip.append(p)
                strip_length += 1

        strip.sort(key=lambda x: x[1]) # strip nach Koordinaten sortieren

        for i in range(strip_length):
            js = min(strip_length, i + 7) # 6 nächste Nachbarpunkte in Berechnung einbeziehen
            for j in range(i + 1, js):
                ds = self.entfernung(strip[i], strip[j])
                if ds < aktueller_MinAbstand:
                    self.last_i = i
                    self.last_j = j
                    aktueller_MinAbstand = ds

        return aktueller_MinAbstand

    def __init__(self, iface):

        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Test_Klasse_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.actions = []
        self.menu = self.tr(u'&PlugIn_Name')

        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Test_Klasse', message)

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
       
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Modul_Name/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'QGIS TestPlugIn v17122020'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&PlugIn_Name'),
                action)
            self.iface.removeToolBarIcon(action)
    
    def closestPair(self): 
        print("Anfang: Dichtestes Punktepaar")
        #P = [(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]
        P = []
        if self.dlg.lineEdit_1.text() and self.dlg.lineEdit_2.text():
            P.append((int(self.dlg.lineEdit_1.text()),int(self.dlg.lineEdit_2.text())))
        if self.dlg.lineEdit_3.text() and self.dlg.lineEdit_4.text():
            P.append((int(self.dlg.lineEdit_3.text()),int(self.dlg.lineEdit_4.text())))
        if self.dlg.lineEdit_5.text() and self.dlg.lineEdit_6.text():
            P.append((int(self.dlg.lineEdit_5.text()),int(self.dlg.lineEdit_6.text())))
        if self.dlg.lineEdit_7.text() and self.dlg.lineEdit_8.text():
            P.append((int(self.dlg.lineEdit_7.text()),int(self.dlg.lineEdit_8.text())))
        if self.dlg.lineEdit_9.text() and self.dlg.lineEdit_10.text():
            P.append((int(self.dlg.lineEdit_9.text()),int(self.dlg.lineEdit_10.text())))
        if self.dlg.lineEdit_11.text() and self.dlg.lineEdit_12.text():
            P.append((int(self.dlg.lineEdit_11.text()),int(self.dlg.lineEdit_12.text())))
        if self.dlg.lineEdit_13.text() and self.dlg.lineEdit_14.text():
            P.append((int(self.dlg.lineEdit_13.text()),int(self.dlg.lineEdit_14.text())))
        if self.dlg.lineEdit_15.text() and self.dlg.lineEdit_16.text():
            P.append((int(self.dlg.lineEdit_15.text()),int(self.dlg.lineEdit_16.text())))
        if self.dlg.lineEdit_17.text() and self.dlg.lineEdit_18.text():
            P.append((int(self.dlg.lineEdit_17.text()),int(self.dlg.lineEdit_18.text())))
        if self.dlg.lineEdit_19.text() and self.dlg.lineEdit_20.text():
            P.append((int(self.dlg.lineEdit_19.text()),int(self.dlg.lineEdit_20.text())))
        if self.dlg.lineEdit_21.text() and self.dlg.lineEdit_22.text():
            P.append((int(self.dlg.lineEdit_21.text()),int(self.dlg.lineEdit_22.text())))
        if self.dlg.lineEdit_23.text() and self.dlg.lineEdit_24.text():
            P.append((int(self.dlg.lineEdit_23.text()),int(self.dlg.lineEdit_24.text())))
        try:
            ergebnis = self.minimaler_Abstand(P)
            self.dlg.label_16.setText("Der kürzeste Abstand ist:")
            self.dlg.Ergebnis.setText(str(round(ergebnis, 2)))
            #print(os.path.expanduser('~'))
            output = open(os.path.expanduser('~') + "/output.txt", "w+")
            output.write(str(ergebnis))
            print("Ende: Dichtestes Punktepaar")
        except:
            print("Für diese Funktion sind mindestens zwei Punkte erforderlich!")

    def dijkstra(self):

        Netzwerk_Knoten_und_Kanten = {
            'P1': {'P2': 4, 'P6': 1},
            'P2': {'P1': 5, 'P6': 6, 'P3':11},
            'P3': {'P2': 11, 'P5': 11, 'P4': 4},
            'P4': {'P3': 9, 'P5': 19},
            'P5': {'P6': 5, 'P3': 12, 'P4': 17},
            'P6': {'P1': 7, 'P2': 2, 'P5': 2}
            }
        
        self.berechne_route_nach_dijkstra(Netzwerk_Knoten_und_Kanten, 'P5', 'P2')

    def CCW(self, p1, p2, p3):
        if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
            return True
        return False

# Main Function:
    def GiftWrapping(self, S):
        n = len(S)
        P = [None] * n
        l = numpy.where(S[:,0] == numpy.min(S[:,0]))
        pointOnHull = S[l[0][0]]
        i = 0
        while True:
            P[i] = pointOnHull
            endpoint = S[0]
            for j in range(1,n):
                if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not self.CCW(S[j],P[i],endpoint):
                    endpoint = S[j]
            i = i + 1
            pointOnHull = endpoint
            if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
                break

        for i in range(n):
            if P[-1] is None:
                del P[-1]
        return numpy.array(P)

    def readShapeFile(self, dateiname):
      
        with open(dateiname, 'rb') as b_datei:
            shapeType = self.lies_shapetype_an_Byte32(b_datei)
            BBox = self.getBBox(b_datei)
            print ("shapeType = ", shapeType, BBox)
            print("Programm erfolgreich beendet  - Python Version: ", sys.version)
        self.dlg.label_19.setText("Umgebende Eckpunkte:")
        self.dlg.Ergebnis_4.setText(str(round(BBox[0],1)) + ",   " + str(round(BBox[1],1)))
        self.dlg.Ergebnis_5.setText(str(round(BBox[2],1)) + ",   " + str(round(BBox[3],1)))
    
    def CSVLesen(self):
        i=0
        file = open(os.path.abspath(os.path.dirname(__file__)) + "/Punkte.csv", "r")
        for line in file:
            i += 1
            line = line.strip()
            line_list = line.split(";")
            if(i==1):
                self.dlg.lineEdit_1.setText(str(line_list[0]))
                self.dlg.lineEdit_2.setText(str(line_list[1]))
            elif(i==2):
                self.dlg.lineEdit_3.setText(str(line_list[0]))
                self.dlg.lineEdit_4.setText(str(line_list[1]))
            elif(i==3):
                self.dlg.lineEdit_5.setText(str(line_list[0]))
                self.dlg.lineEdit_6.setText(str(line_list[1]))
            elif(i==4):
                self.dlg.lineEdit_7.setText(str(line_list[0]))
                self.dlg.lineEdit_8.setText(str(line_list[1]))
            elif(i==5):
                self.dlg.lineEdit_9.setText(str(line_list[0]))
                self.dlg.lineEdit_10.setText(str(line_list[1]))
            elif(i==6):
                self.dlg.lineEdit_11.setText(str(line_list[0]))
                self.dlg.lineEdit_12.setText(str(line_list[1]))
            elif(i==7):
                self.dlg.lineEdit_13.setText(str(line_list[0]))
                self.dlg.lineEdit_14.setText(str(line_list[1]))
            elif(i==8):
                self.dlg.lineEdit_15.setText(str(line_list[0]))
                self.dlg.lineEdit_16.setText(str(line_list[1]))
            elif(i==9):
                self.dlg.lineEdit_17.setText(str(line_list[0]))
                self.dlg.lineEdit_18.setText(str(line_list[1]))
            elif(i==10):
                self.dlg.lineEdit_19.setText(str(line_list[0]))
                self.dlg.lineEdit_20.setText(str(line_list[1]))
            elif(i==11):
                self.dlg.lineEdit_21.setText(str(line_list[0]))
                self.dlg.lineEdit_22.setText(str(line_list[1]))
            elif(i==12):
                self.dlg.lineEdit_23.setText(str(line_list[0]))
                self.dlg.lineEdit_24.setText(str(line_list[1]))  
        file.close()

    def konvexeHuelle(self):
        N = int(self.dlg.lineEdit_27.text())
        punkte = []
        if self.dlg.lineEdit_1.text() and self.dlg.lineEdit_2.text():
            punkte.append([int(self.dlg.lineEdit_1.text()),int(self.dlg.lineEdit_2.text())])
        if self.dlg.lineEdit_3.text() and self.dlg.lineEdit_4.text():
            punkte.append([int(self.dlg.lineEdit_3.text()),int(self.dlg.lineEdit_4.text())])
        if self.dlg.lineEdit_5.text() and self.dlg.lineEdit_6.text():
            punkte.append([int(self.dlg.lineEdit_5.text()),int(self.dlg.lineEdit_6.text())])
        if self.dlg.lineEdit_7.text() and self.dlg.lineEdit_8.text():
            punkte.append([int(self.dlg.lineEdit_7.text()),int(self.dlg.lineEdit_8.text())])
        if self.dlg.lineEdit_9.text() and self.dlg.lineEdit_10.text():
            punkte.append([int(self.dlg.lineEdit_9.text()),int(self.dlg.lineEdit_10.text())])
        if self.dlg.lineEdit_11.text() and self.dlg.lineEdit_12.text():
            punkte.append([int(self.dlg.lineEdit_11.text()),int(self.dlg.lineEdit_12.text())])
        if self.dlg.lineEdit_13.text() and self.dlg.lineEdit_14.text():
            punkte.append([int(self.dlg.lineEdit_13.text()),int(self.dlg.lineEdit_14.text())])
        if self.dlg.lineEdit_15.text() and self.dlg.lineEdit_16.text():
            punkte.append([int(self.dlg.lineEdit_15.text()),int(self.dlg.lineEdit_16.text())])
        if self.dlg.lineEdit_17.text() and self.dlg.lineEdit_18.text():
            punkte.append([int(self.dlg.lineEdit_17.text()),int(self.dlg.lineEdit_18.text())])
        if self.dlg.lineEdit_19.text() and self.dlg.lineEdit_20.text():
            punkte.append([int(self.dlg.lineEdit_19.text()),int(self.dlg.lineEdit_20.text())])
        if self.dlg.lineEdit_21.text() and self.dlg.lineEdit_22.text():
            punkte.append([int(self.dlg.lineEdit_21.text()),int(self.dlg.lineEdit_22.text())])
        if self.dlg.lineEdit_23.text() and self.dlg.lineEdit_24.text():
            punkte.append([int(self.dlg.lineEdit_23.text()),int(self.dlg.lineEdit_24.text())])
        if(len(punkte)>0):
            P = numpy.array(punkte)
        else:
            P = numpy.array([(numpy.random.randint(10,290),numpy.random.randint(10,290)) for i in range(N)])
        print(P) 
        L = self.GiftWrapping(P)
        convexXCoords= []
        convexYCoords= []
            
        fig = plot.figure()
        ax = fig.add_subplot(111)  
        plot.plot(P[:,0],P[:,1],"r^")
        # Punkte auf Huelle: gruen + square marker
        plot.plot(L[:,0],L[:,1],"gs", markersize=7)
        plot.plot(L[:,0],L[:,1], 'b-')  # b = blau
        plot.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-')
        # Koordinaten anzeigen
        for xy in zip(L[:,0],L[:,1]):                                                           
            ax.annotate('%s, %s' %xy, xy=xy, textcoords='data', ha='center', va='bottom', fontstyle='normal')     
        plot.axis('on')
        plot.title('Berechnung einer konvexen Hülle')
        plot.show()
        

    def point_in_polygon(self,x,y,poly):
        n=len(poly)
        inside = False
        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x >= max(p1x,p2x):
                        if p1y != p2y:
                            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside

    def PunktPolygonTest(self):
        punkte = []
        if self.dlg.lineEdit_1.text() and self.dlg.lineEdit_2.text():
            punkte.append([int(self.dlg.lineEdit_1.text()),int(self.dlg.lineEdit_2.text())])
        if self.dlg.lineEdit_3.text() and self.dlg.lineEdit_4.text():
            punkte.append([int(self.dlg.lineEdit_3.text()),int(self.dlg.lineEdit_4.text())])
        if self.dlg.lineEdit_5.text() and self.dlg.lineEdit_6.text():
            punkte.append([int(self.dlg.lineEdit_5.text()),int(self.dlg.lineEdit_6.text())])
        if self.dlg.lineEdit_7.text() and self.dlg.lineEdit_8.text():
            punkte.append([int(self.dlg.lineEdit_7.text()),int(self.dlg.lineEdit_8.text())])
        if self.dlg.lineEdit_9.text() and self.dlg.lineEdit_10.text():
            punkte.append([int(self.dlg.lineEdit_9.text()),int(self.dlg.lineEdit_10.text())])
        if self.dlg.lineEdit_11.text() and self.dlg.lineEdit_12.text():
            punkte.append([int(self.dlg.lineEdit_11.text()),int(self.dlg.lineEdit_12.text())])
        if self.dlg.lineEdit_13.text() and self.dlg.lineEdit_14.text():
            punkte.append([int(self.dlg.lineEdit_13.text()),int(self.dlg.lineEdit_14.text())])
        if self.dlg.lineEdit_15.text() and self.dlg.lineEdit_16.text():
            punkte.append([int(self.dlg.lineEdit_15.text()),int(self.dlg.lineEdit_16.text())])
        if self.dlg.lineEdit_17.text() and self.dlg.lineEdit_18.text():
            punkte.append([int(self.dlg.lineEdit_17.text()),int(self.dlg.lineEdit_18.text())])
        if self.dlg.lineEdit_19.text() and self.dlg.lineEdit_20.text():
            punkte.append([int(self.dlg.lineEdit_19.text()),int(self.dlg.lineEdit_20.text())])
        if self.dlg.lineEdit_21.text() and self.dlg.lineEdit_22.text():
            punkte.append([int(self.dlg.lineEdit_21.text()),int(self.dlg.lineEdit_22.text())])
        if self.dlg.lineEdit_23.text() and self.dlg.lineEdit_24.text():
            punkte.append([int(self.dlg.lineEdit_23.text()),int(self.dlg.lineEdit_24.text())])
        punkte = numpy.array(punkte)
        print('Polygon mit ' + str(len(punkte)) + ' Punkten')
        #polygon = [(0,10),(10,10),(10,0),(0,0)]
        point_x = int(self.dlg.lineEdit_25.text())
        point_y = int(self.dlg.lineEdit_26.text())
        print (self.point_in_polygon(point_x,point_y,punkte))
        if(self.point_in_polygon(point_x,point_y,punkte)==True):
            self.dlg.Ergebnis_7.setText("Ja,  der Punkt liegt im Polygon")
        else:
            self.dlg.Ergebnis_7.setText("Nein,  der Punkt liegt nicht im Polygon")

    def close(self):
        self.dlg.close()

    def test(self):
        print(self.dlg.darkModeToggle.isChecked())

    def run(self):
        if self.first_start == True:
            self.first_start = False
            self.dlg = Test_KlasseDialog()

        # show the dialog
        self.dlg.show()
        print("Neuer Durchlauf")
        # jetzt wird on_klick aufgerufen
        self.dlg.pushButton.clicked.connect(self.closestPair)
        self.dlg.pushButton_2.clicked.connect(self.dijkstra)
        self.dlg.pushButton_3.clicked.connect(self.ear_clip)
        self.dlg.pushButton_4.clicked.connect(lambda: self.readShapeFile(os.path.abspath(os.path.dirname(__file__)) + "/bayern_shape/bayern_ex.shp"))
        self.dlg.pushButton_5.clicked.connect(self.CSVLesen)
        self.dlg.pushButton_6.clicked.connect(self.konvexeHuelle)
        self.dlg.pushButton_7.clicked.connect(self.PunktPolygonTest)
        self.dlg.darkModeToggle.toggled.connect(self.test)
        self.dlg.button_box.accepted.connect(self.close)
        self.dlg.button_box.rejected.connect(self.close)

        result = self.dlg.exec_()
        
        if result:
            print("OK gedrückt")
            
            