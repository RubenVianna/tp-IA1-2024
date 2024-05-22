from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import pyqtSignal
from Controllers.logicaNodos import *
from Views.cargaCoordenadas import CargaCoordenadas
from Views.vistaGrafo import VistaGrafo
from Controllers.logicaNodos import definirNodos

class CargaNodos(QWidget):
    cantidadNodos = pyqtSignal(object)  # Definir la señal a nivel de clase

    def __init__(self,opcion):
        super().__init__()
        self.opcion = str(opcion)
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
        if(self.opcion == 'carga'):
            nodos = definirNodos(valor)
            self.hide()
            self.cargacoordenadas = CargaCoordenadas(nodos)
            self.cargacoordenadas.show()
        else:
            nodos = generarAleatorios(valor)
            #self.hide()
            self.vistaGrafo = VistaGrafo(nodos)
            self.vistaGrafo.show()
    

class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trabajo Integrador - Inteligencia Artificial 1")
        self.setFixedSize(400, 200)
        layout = QVBoxLayout()
        self.button = QPushButton("Cargar Datos")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(lambda: self.avanzarVista('carga'))
        layout.addWidget(self.button)

        self.button2 = QPushButton("Generar Datos Aleatorios")
        self.button2.setFont(QFont("Arial", 10))  
        self.button2.clicked.connect(lambda: self.avanzarVista('aleatorio'))
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def avanzarVista(self,opcion):
            self.hide()
            self.cargarNodos = CargaNodos(opcion)
            self.cargarNodos.show()
