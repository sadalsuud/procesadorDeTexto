# -*- coding: utf-8 -*-

import sys
from PyQt4 import uic, QtGui, QtCore


QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class VtnBuscar(QtGui.QDialog):

    def __init__(self):
        super(VtnBuscar, self).__init__(parent=None)
        self.ui = uic.loadUi('../share/ui/vtnbuscar.ui', self)

        # se hace referencia a los componentes de la ventana
        self.busqueda = self.ui.findChild(QtGui.QLineEdit, "linEdBuscar")
        self.btnBuscar = self.ui.findChild(QtGui.QPushButton, "btnBuscar")

        # cuando el usuario presion el boton buscar
        self.btnBuscar.clicked.connect(self.buscar)

    @QtCore.Slot()
    def buscar(self):
        print "buscando"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    buscar = VtnBuscar()
    buscar.ui.show()
    app.exec_()
