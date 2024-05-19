import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import pyqtSignal
from Controllers.logicaNodos import definirNodos
from Views.cargaCoordenadas import CargaCoordenadas
from Controllers.logicaNodos import definirNodos

class CargaNodos(QWidget):
    cantidadNodos = pyqtSignal(object)  # Definir la señal a nivel de clase

    def __init__(self):
        super().__init__()

        enteros = QIntValidator(1,20)

        self.setWindowTitle("Ingrese la cantidad de nodos")
        self.setFixedSize(400, 100)
        layout = QVBoxLayout()
        self.input_text = QLineEdit()
        self.input_text.setValidator(enteros)  # Aplicar el validador de enteros al QLineEdit
        layout.addWidget(self.input_text)
        self.button = QPushButton("Aceptar")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.enviarCantidadNodos)
        layout.addWidget(self.button)
        self.setLayout(layout)

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
        self.cargarNodos.cantidadNodos.connect(self.mostrarCargaCoordenadas)  # Conectar la señal
        self.cargarNodos.show()

    def mostrarCargaCoordenadas(self, nodos):
        self.cargarNodos.close()
        self.ventanaCoordenadas = CargaCoordenadas(nodos)
        self.ventanaCoordenadas.show()