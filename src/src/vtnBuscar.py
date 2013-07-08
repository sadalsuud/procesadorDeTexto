# -*- coding: utf-8 -*-

import sys
from PyQt4 import uic, QtGui, QtCore


QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class VtnBuscar(QtGui.QDialog):

    # recibe por parametro en el contructor el texto que contiene el archivo 
    def __init__(self, l=None):
        super(VtnBuscar, self).__init__(parent=None)
        self.ui = uic.loadUi('../share/ui/vtnbuscar.ui', self)
        self.l = l 
        self.coincidencias = 0
         # se hace referencia a los componentes de la ventana
        self.busqueda = self.ui.findChild(QtGui.QLineEdit, "linEdBuscar")
        self.btnBuscar = self.ui.findChild(QtGui.QPushButton, "btnBuscar")

        # cuando el usuario presion el boton buscar
        self.btnBuscar.clicked.connect(self.buscar)
        

    @QtCore.Slot()
    def buscar(self):
        seq = []
        # self.busqueda es un objeto QLineEdit y el texto se saca con .text()
        for c in self.busqueda.text():
            seq.append(str(c))
        # recorra toda el texto del archivo
        i = 0
        for posicion in range(len(self.l)-1):
            # si coincide la primera letra de la busqueda y el texyo del archivo... 
            pos = posicion
            #print "posicion ->", posicion
            while i < len(seq) and self.l.get(pos) == seq[i]:  # si coinciden en el 1er simbolo del texto del archivo y el patron de búsqueda
                #print self.l.get(pos)
                i += 1
                pos += 1
                #print "i ->", i
                #print "pos ->", pos                    
                #print "fin de un ciclo de while" 
                if i == len(seq):
                    self.coincidencias += 1 # por cada palabra que encuentr
            i = 0 
            #print "fin de un ciclo for"  
        #print "se encontraron ", self.coincidencias, "coincidencias"
        
    def getCoincidencias(self):
        return self.coincidencias

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    buscar = VtnBuscar()
    buscar.ui.show()
    app.exec_()
