from Controllers.herustica import *
from Controllers.funciones import *
from Views.vistaGrafo import VistaGrafo
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QFont

class CargaRelaciones(QWidget):
    def __init__(self, nodos, vistaAnterior):
        super().__init__()
        self.setWindowTitle("Definir conexiones")
        self.setGeometry(800, 200, 260, 300)
        self.vistaAnterior = vistaAnterior
        self.nodos = nodos
        self.checkbox_dict = {}  # Diccionario para mapear ComboBoxes a CheckBoxes

        # Columnas y sus encabezados
        headers = ["Nombre","Conexiones"]

        layout = QVBoxLayout()
        self.tabla = QTableWidget()
        self.tabla.setRowCount(len(nodos))
        self.tabla.setColumnCount(len(headers))
        self.tabla.setHorizontalHeaderLabels(headers)

        for i, nodo in enumerate(nodos):
            self.tabla.setItem(i, 0, QTableWidgetItem(nodo.nombre))
            combo_box = CheckableComboBox()
            self.checkbox_dict[i] = combo_box #Agrego al dicccionario
            for opcion in nodos:
                if opcion.nombre != nodos[i].nombre:
                    item = QStandardItem(opcion.nombre)
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    item.setData(Qt.Unchecked, Qt.CheckStateRole)
                    combo_box.model().appendRow(item)
            self.tabla.setCellWidget(i, 1, combo_box)
            combo_box.currentIndexChanged.connect(lambda index, row=i: self.update_checklist(row))

        self.button = QPushButton("Continuar")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.verConexiones)

        self.atras = QPushButton("Atrás")
        self.atras.setFont(QFont("Arial", 10))
        self.atras.clicked.connect(self.volverAtras)

        layout.addWidget(self.tabla)
        layout.addWidget(self.button)
        layout.addWidget(self.atras) 
        self.setLayout(layout)

    def update_checklist(self, row):
        combo_box = self.checkbox_dict[row]  # Obtener ComboBox asociado a la fila
        checked_items = combo_box.checkedItems()  # Obtener elementos seleccionados en el ComboBox
        for i, nodo in enumerate(self.nodos):
            checkbox = self.checkbox_dict[i]
            checkbox.model().item(row).setCheckState(Qt.Checked if nodo.nombre in checked_items else Qt.Unchecked)
            
    def verConexiones(self):
        for row in range(self.tabla.rowCount()):
            nombre_nodo = self.tabla.item(row, 0).text()  # Obtener el nombre del nodo en la fila actual
            combo_box = self.tabla.cellWidget(row, 1)  # Obtener el ComboBox en la fila actual
            conexiones_marcadas = [combo_box.model().item(index).text() for index in range(combo_box.model().rowCount()) if combo_box.model().item(index).checkState() == Qt.Checked]
            for nodo in self.nodos:
                if nodo.nombre == nombre_nodo:
                   nodo.conexiones = [next((nodo for nodo in self.nodos if nodo.nombre == conexion), None) for conexion in conexiones_marcadas]
        
        self.hide()
        self.vistaGrafo = VistaGrafo(self.nodos,self)
        self.vistaGrafo.show()
    
    def volverAtras(self):
        self.close()
        self.vistaAnterior.show()
