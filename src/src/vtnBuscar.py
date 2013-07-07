# -*- coding: utf-8 -*-

import sys
from PyQt4 import uic, QtGui

class VtnBuscar(QtGui.QWidget):

    def __init__(self):
        super(VtnBuscar, self).__init__(parent)
         self.ui = uic.loadUi('../share/ui/vtnbuscar.ui', self)

