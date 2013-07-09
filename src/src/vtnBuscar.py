# -*- coding: utf-8 -*-

import sys
import ListaCD
from PyQt4 import uic, QtGui, QtCore


QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class VtnBuscar(QtGui.QDialog):

    # recibe por parametro en el contructor el texto que contiene el archivo 
    def __init__(self, uiPri, l=None):
        super(VtnBuscar, self).__init__(parent=None)
        self.ui = uic.loadUi('../share/ui/vtnbuscar.ui', self)
        self.uiWordUfps =  uiPri        # referencia a la ventana principal
        self.l = l 
        self.coincidencias = 0
         # se hace referencia a los componentes de la ventana
        self.rta = self.ui.findChild(QtGui.QLabel,"qLbRta")
        self.busqueda = self.ui.findChild(QtGui.QLineEdit, "linEdBuscar")
        self.btnBuscar = self.ui.findChild(QtGui.QPushButton, "btnBuscar")
    
        # cuando el usuario presion el boton buscar
        self.btnBuscar.clicked.connect(self.buscar)
        

    @QtCore.Slot()
    def buscar(self):
        copia_lista = ListaCD.ListaCD(self.l)
        self.coincidencias = 0      # reinicia el conteo con cada nueva busqueda
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
                # si se alcanzo el final del tamaño de la busqueda
                if i == len(seq):
                    self.coincidencias += 1     # por cada palabra que encuentr
                    # pos - 1 porque aun no sé xD
                    #print pos
                    self.pintarCoincidencia(len(seq), pos -1, copia_lista)
            i = 0 
            #print "fin de un ciclo for" 
        self.getCoincidencias()
        #print "se encontraron ", self.coincidencias, "coincidencias"
    
    # para obtener el numero de coincidencias
    def getCoincidencias(self):
        self.rta.setText(str(self.coincidencias) + " coincidencias")
        #return self.coincidencias
        
    def pintarCoincidencia(self, tam, pos, copia_lista):
        #~ print "tamaño de la busqueda", tam
        #~ print "posicion del ultimo caracter en la lista", pos
        
        # si la busqueda es un solo caracter 
        if tam == 1:
            # pinte el caracter 
            val = "<font color = '#E32828'>" + copia_lista.get(pos) + "</font>"
            copia_lista.set(pos, val)
        else:
            # inicie la pintada desde el primer caracter de la busqueda
            ini = "<font color ='#E32828'>" + copia_lista.get((pos - tam) + 1)
            # termine la pintada en el ultimo caracter de la busqueda
            fin = copia_lista.get(pos) + "</font>"
        
            #~ print "inicio de la palabra", ini
            #~ print "fin de la palaba", fin
            copia_lista.set((pos - tam) + 1, ini)
            copia_lista.set(pos, fin)
           
        html = ""
        # sacar el texto coloreado de la lisa para mostrarlo la interfaz
        for elem in copia_lista:
            html = html + elem
        self.uiWordUfps.textEdit.setHtml(html)
        #~ print html
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    buscar = VtnBuscar()
    buscar.ui.show()
    app.exec_()
