from Models.nodo import Nodo
from Controllers.herustica import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QRadioButton, QPushButton, QButtonGroup
from PyQt5.QtGui import QIntValidator, QFont

class CargaRelaciones(QWidget):
    def __init__(self, nodos):
        super().__init__()
        self.setWindowTitle("Definir conexiones")
        self.setGeometry(800, 200, 550, 300)

        # Columnas y sus encabezados
        headers = ["Nombre","Heuristica", "Conexiones"]

        layout = QVBoxLayout()
        self.tabla = QTableWidget()
        self.tabla.setRowCount(len(nodos))
        self.tabla.setColumnCount(len(headers))
        self.tabla.setHorizontalHeaderLabels(headers)

        for i, nodo in enumerate(nodos):
            self.tabla.setItem(i, 0, QTableWidgetItem(nodo.nombre))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(nodo.heuristica)))

        layout.addWidget(self.tabla)
        self.setLayout(layout)
