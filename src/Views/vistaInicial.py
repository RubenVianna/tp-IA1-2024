import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal
from Controllers.logicaNodos import definirNodos
from Views.cargaCoordenadas import cargaCoordenadas
from Controllers.logicaNodos import definirNodos

class CargaNodos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingrese la cantidad de nodos")
        self.setFixedSize(400, 100)
        layout = QVBoxLayout()
        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)
        self.button = QPushButton("Aceptar")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.enviarValor)
        layout.addWidget(self.button)
        self.setLayout(layout)

        cantidadNodos = pyqtSignal(object)
    
    def enviarCantidadNodos(self):
        valor = self.input_text.text()  # Obtener el valor del campo de texto
        nodos = definirNodos(valor)
        self.cantidadNodos.emit(nodos)


class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trabajo Integrador - Inteligencia Artificial 1")
        self.setFixedSize(400, 200)
        layout = QVBoxLayout()
        self.button = QPushButton("Cargar Datos")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.cargarCantidadNodos)
        layout.addWidget(self.button)

        self.button2 = QPushButton("Generar Datos Aleatorios")
        self.button2.setFont(QFont("Arial", 10))  
       # self.button2.clicked.connect(self.abrir_segunda_vista)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def cargarCantidadNodos(self):
        self.hide()
        self.cargarNodos = CargaNodos()
        self.cargarNodos.show()
