import sys
from Controllers.logicaNodos import definirNodos

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class cargaCoordenadas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabla de Objetos")
        self.setGeometry(100, 100, 400, 300)
        
        # Conectar la señal de la vista de origen a la ranura de esta vista
        cargarNodos.enviarDatos.connect(self.recibir_datos)

        layout = QVBoxLayout()
        self.tabla = QTableWidget()
        self.tabla.setRowCount(len(nodos))
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Nombre"])

        for i, nodo in enumerate(nodos):
            item = QTableWidgetItem(nodo.nombre)
            self.tabla.setItem(i, 0, item)

        layout.addWidget(self.tabla)
        self.setLayout(layout)

