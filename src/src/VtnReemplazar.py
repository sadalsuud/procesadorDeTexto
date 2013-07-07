#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import uic, QtGui, QtCore


QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class VtnReemplazar(QtGui.QDialog):
    
    def __init__(self):
        super(VtnReemplazar, self).__init__(parent=None)
        self.ui = uic.loadUi('../share/ui/vtnReemplazar.ui', self)
        
        # referencia a los componentes de la ventana
        #self.linEdiBuscar = self.ui.findChild(QtGui.QLineEdit, "lineEdit")
        #self.linEdiReemplazar = self.ui.findChild(QtGui.QLineEdit, "lineEdit_2")
        self.btnReemplazar = self.ui.findChild(QtGui.QPushButton, "qpBtnReemplazar")
        
        # conectar signals y slots
        self.btnReemplazar.clicked.connect(self.reemplazar)

    @QtCore.Slot()
    def reemplazar(self):
        print "reeemplzando"
    
    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    reemplazar = VtnReemplazar()
    reemplazar.ui.show()
    app.exec_()
