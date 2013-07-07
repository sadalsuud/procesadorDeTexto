# -*- coding: utf-8 -*-


from PyQt4 import uic, QtGui#, QtCore


# instancia de la listaCD
# nombre del archivo


# Clase principal del editor, será un wrapper de la ventana a mostrar, en este
# caso MainWindow
class WordUFPS(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(WordUFPS, self).__init__(parent)
        # cargamos la interfaz gráfica desde el archivo textedito.ui  self.ui es
        # ahora por llamarlo de alguna forma, un puntero al objeto MainWindow.
        self.ui = uic.loadUi('../share/ui/texteditor.ui', self)
        #referencia al boton buscar
        self.boton = self.ui.findChild(QtGui.QPushButton, "pushButton")

        self.boton.clicked.connect(self.close)

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
""""
    # conectar señales y slots
    # elQueEnvia.señal.connect(funcion_slot)
        self.actionAbrir_archivo.triggered.connect(self.on_actionAbrir_archivo_triggered)
        self.actionGuardar_archivo.triggered.connect(self.on_actionGuardar_archivo_triggered)
        self.actionCerrar_archivo.triggered.connect(self.on_actionCerrar_archivo_triggered)
        self.actionSalir.triggered.connect(self.on_actionSalir_triggered)
        self.actionBuscar.triggered.connect(self.on_actionBuscar_triggered)
        self.actionReemplazar.triggered.connect(self.on_actionReemplazar_triggered)
        self.puschButton.clicked.connect(self.on_puchButton_clicked)

    # abrir archivo
    @QtCore.Slot()
    def on_actionAbrir_archivo_triggered(self):
        pass
    # guardar archivo

    @QtCore.Slot()
    def on_actionGuardar_archivo_triggered(self):
        pass

    # cerrar archivo
    @QtCore.Slot()
    def on_actionCerrar_archivo_triggered(self):
        pass

    # salir
    @QtCore.Slot()
    def on_actionSalir_triggered(self):
        pass

    # buscar
    @QtCore.Slot()
    def on_actionBuscartriggered(self):
        pass

    # Reemplazar
    @QtCore.Slot()
    def on_actionReemplazar_triggered(self):
        pass

    # boton buscar
    @QtCore.Slot()
    def on_puchButton_clicked(self):
        pass
"""

if __name__ == '__main__':
    app = QtGui.QApplication(["WordUFPSEditor"])
    ProEditor = WordUFPS()
    ProEditor.show()
    app.exec_()

