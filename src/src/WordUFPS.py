# -*- coding: utf-8 -*-


from PyQt4 import uic, QtGui, QtCore
import vtnBuscar
import VtnReemplazar

QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


# Clase principal del editor, será un wrapper de la ventana a mostrar, en este
# caso MainWindow
class WordUFPS(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(WordUFPS, self).__init__(parent)
        # cargamos la interfaz gráfica desde el archivo textedito.ui  self.ui es
        # ahora por llamarlo de alguna forma, un puntero al objeto MainWindow.
        self.ui = uic.loadUi('../share/ui/texteditor.ui', self)

        #referencia a los componentes de la ventana
        self.textEdit = self.ui.findChild(QtGui.QTextEdit)
        self.boton = self.ui.findChild(QtGui.QPushButton, "pushButton")
        self.optBuscar = self.ui.findChild(QtGui.QAction, "actionBuscar")
        self.optReemplazar = self.ui.findChild(QtGui.QAction, "actionReemplazar")
        self.optSalir = self.ui.findChild(QtGui.QAction, "actionSalir")
        self.optAbrir = self.ui.findChild(QtGui.QAction, "actionAbrir_archivo")
        self.optGuardar = self.ui.findChild(QtGui.QAction, "actionGuardar_archivo")
        
        # conectando signals y slots
        self.boton.clicked.connect(self.buscar)
        self.optBuscar.triggered.connect(self.buscar)
        self.optReemplazar.triggered.connect(self.reemplazar)
        self.optSalir.triggered.connect(self.close)
        self.optAbrir.triggered.connect(self.abrir)
        self.optGuardar.triggered.connect(self.guardar)

    # decoradores
    @QtCore.Slot()
    def buscar(self):
        buscar = vtnBuscar.VtnBuscar()
        buscar.ui.exec_()
        
    @QtCore.Slot()
    def reemplazar(self):
        # variable = nombreDelArchivo.NombreDeLaClase
        reemplazar = VtnReemplazar.VtnReemplazar()
        reemplazar.ui.exec_()
    
    @QtCore.Slot()
    def abrir(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)
        fname.close() 
        
    @QtCore.Slot()
    def guardar(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar archivo', '.')
        fname = open(filename, 'w')
        fname.write(self.textEdit.toPlainText())
        fname.close() 



if __name__ == '__main__':
    app = QtGui.QApplication(["WordUFPSEditor"])
    ProEditor = WordUFPS()
    ProEditor.show()
    app.exec_()
