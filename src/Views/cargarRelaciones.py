from Controllers.herustica import *
from Controllers.funciones import *
from Views.vistaGrafo import VistaGrafo
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

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
            nombre = QTableWidgetItem(nodo.nombre)
            nombre.setFlags(nombre.flags() & ~Qt.ItemIsEditable)  
            self.tabla.setItem(i, 0, nombre)
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

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button)
        button_layout.addWidget(self.atras)

        layout.addWidget(self.tabla)
        layout.addLayout(button_layout)  # Agregar el layout de botones al layout principal
        self.setLayout(layout)
      
    def verConexiones(self):
            # Limpiar todas las conexiones existentes
        for nodo in self.nodos:
            nodo.conexiones.clear()
            
        for row in range(self.tabla.rowCount()):
            nombre_nodo = self.tabla.item(row, 0).text()  # Obtener el nombre del nodo en la fila actual
            combo_box = self.tabla.cellWidget(row, 1)  # Obtener el ComboBox en la fila actual
            conexiones_marcadas = [combo_box.model().item(index).text() for index in range(combo_box.model().rowCount()) if combo_box.model().item(index).checkState() == Qt.Checked]
            nodo_actual = next((nodo for nodo in self.nodos if nodo.nombre == nombre_nodo), None)
            if nodo_actual:
                for nombre_conexion in conexiones_marcadas:
                    nodo_conexion = next((nodo for nodo in self.nodos if nodo.nombre == nombre_conexion), None)
                    if nodo_conexion:
                        # Agregar la conexión del check
                        if nodo_conexion not in nodo_actual.conexiones:
                            nodo_actual.conexiones.append(nodo_conexion)
                        # Aseguramos que la conexión sea bidireccional
                        if nodo_actual not in nodo_conexion.conexiones:
                            nodo_conexion.conexiones.append(nodo_actual)
        self.hide()
        self.vistaGrafo = VistaGrafo(self.nodos, self)
        self.vistaGrafo.show()
    
    def volverAtras(self):
        self.close()
        self.vistaAnterior.show()
