from Models.nodo import Nodo
from Views.cargarRelaciones import CargaRelaciones
from Controllers.herustica import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QRadioButton, QPushButton, QButtonGroup
from PyQt5 import Qt
from PyQt5.QtGui import QIntValidator, QFont

class CargaCoordenadas(QWidget):

    def __init__(self, nodos):
        super().__init__()
        self.setWindowTitle("Listado de Nodos")
        self.setGeometry(800, 200, 550, 300)
        
        # Columnas y sus encabezados
        headers = ["Nombre", "Coordenada X", "Coordenada Y", "Estado Inicial", "Estado Final"]

        layout = QVBoxLayout()
        self.tabla = QTableWidget()
        self.tabla.setRowCount(len(nodos))
        self.tabla.setColumnCount(len(headers))
        self.tabla.setHorizontalHeaderLabels(headers)

        self.buttonGroupInitial = QButtonGroup(self)
        self.buttonGroupFinal = QButtonGroup(self)

        enteros = QIntValidator(-10, 20)

        for i, nodo in enumerate(nodos):
            self.tabla.setItem(i, 0, QTableWidgetItem(nodo.nombre))
            self.input_x = QLineEdit()
            self.input_x.setValidator(enteros)
            self.input_x.setText("")
            self.tabla.setCellWidget(i, 1,  self.input_x)
            self.input_y = QLineEdit()
            self.input_y.setValidator(enteros)
            self.input_y.setText("")
            self.tabla.setCellWidget(i, 2,  self.input_y)
            radio_initial = QRadioButton()
            self.buttonGroupInitial.addButton(radio_initial, i)
            if nodo.estadoI:
                radio_initial.setChecked(True)
            self.tabla.setCellWidget(i, 3, radio_initial)
            radio_final = QRadioButton()
            self.buttonGroupFinal.addButton(radio_final, i)
            if nodo.estadoF:
                radio_final.setChecked(True)
            self.tabla.setCellWidget(i, 4, radio_final)

        self.button = QPushButton("Calcular con Distancia Linea Recta")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.calcularDLR)

        self.button2 = QPushButton("Calcular con Distancia de Manhattan")
        self.button2.setFont(QFont("Arial", 10))
        self.button2.clicked.connect(self.calcularManhattan)

        layout.addWidget(self.tabla)
        layout.addWidget(self.button)  
        layout.addWidget(self.button2)
        self.setLayout(layout)
    
    def calcularDLR(self):
        nodos = []
        nodoFinal = None
        for row in range(self.tabla.rowCount()):
            nombre = self.tabla.item(row, 0).text()
            coordenada_x = self.tabla.cellWidget(row, 1).text()
            coordenada_y = self.tabla.cellWidget(row, 2).text()

            radio_initial = self.tabla.cellWidget(row, 3)
            radio_final = self.tabla.cellWidget(row, 4)
            estadoI = 'I' if radio_initial.isChecked() else None
            estadoF = 'F' if radio_final.isChecked() else None

            nodo = Nodo(nombre)
            nodo.coordenada_x = int(coordenada_x) if coordenada_x else None
            nodo.coordenada_y = int(coordenada_y) if coordenada_y else None
            nodo.estadoI = estadoI
            nodo.estadoF = estadoF
            nodos.append(nodo)

        for n in nodos:
            if n.estadoF == 'F':
                nodoFinal = n
    
        i= 0
        while i < len(nodos):
            if coordenada_x and coordenada_y:
                heuristica = distanciaLineaRecta(nodos[i],nodoFinal)
                nodos[i].heuristica = heuristica
            i= i+ 1

        self.hide()
        self.cargaRelaciones = CargaRelaciones(nodos)
        self.cargaRelaciones.show()

        
    def calcularManhattan(self):
        nodos = []
        nodoFinal = None
        for row in range(self.tabla.rowCount()):
            nombre = self.tabla.item(row, 0).text()
            coordenada_x = self.tabla.cellWidget(row, 1).text()
            coordenada_y = self.tabla.cellWidget(row, 2).text()

            radio_initial = self.tabla.cellWidget(row, 3)
            radio_final = self.tabla.cellWidget(row, 4)
            estadoI = 'I' if radio_initial.isChecked() else None
            estadoF = 'F' if radio_final.isChecked() else None

            nodo = Nodo(nombre)
            nodo.coordenada_x = int(coordenada_x) if coordenada_x else None
            nodo.coordenada_y = int(coordenada_y) if coordenada_y else None
            nodo.estadoI = estadoI
            nodo.estadoF = estadoF
            nodos.append(nodo)

        for n in nodos:
            if n.estadoF == 'F':
                nodoFinal = n

        i= 0
        while i < len(nodos):
            if coordenada_x and coordenada_y:
                heuristica = distanciaManhattan(nodos[i],nodoFinal)
                nodos[i].heuristica = heuristica
            i= i+ 1

        self.abrir_cargar_relaciones_signal.emit(nodos)