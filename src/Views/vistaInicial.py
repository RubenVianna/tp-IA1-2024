from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import pyqtSignal
from Controllers.logicaNodos import generarAleatorios
from Views.cargaCoordenadas import CargaCoordenadas
from Views.vistaGrafo import VistaGrafo
from Controllers.logicaNodos import definirNodos

class CargaNodos(QWidget):
    cantidadNodos = pyqtSignal(object)  # Definir la señal a nivel de clase

    def __init__(self,opcion):
        super().__init__()
        self.opcion = str(opcion)
        enteros = QIntValidator(1,1000)

        self.setWindowTitle("Ingrese la cantidad de nodos")
        self.setFixedSize(400, 100)
        layout = QVBoxLayout()
        self.input_text = QLineEdit()
        self.input_text.setValidator(enteros)  # Aplicar el validador de enteros al QLineEdit
        layout.addWidget(self.input_text)

        self.button = QPushButton("Aceptar")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.enviarCantidadNodos)

        self.atras = QPushButton("Atrás")
        self.atras.setFont(QFont("Arial", 10))
        self.atras.clicked.connect(self.volverAtras)

        button_layout = QHBoxLayout()  # Crear un layout horizontal para los botones
        button_layout.addWidget(self.button)
        button_layout.addWidget(self.atras)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def enviarCantidadNodos(self):
        valor = self.input_text.text()  # Obtener el valor del campo de texto
        if valor.strip():
            valor = int(valor)
            if valor > 0 and valor < 28:
                if(self.opcion == 'carga'):
                    nodos = definirNodos(valor)
                    self.hide()
                    self.cargacoordenadas = CargaCoordenadas(nodos, self)
                    self.cargacoordenadas.show()
                else:
                    nodos = generarAleatorios(valor)
                    self.hide()
                    self.vistaGrafo = VistaGrafo(nodos,self)
                    self.vistaGrafo.show()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Atencion!")
                msg.setText("La cantidad de nodos debe ser entre 1 y 27")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Atencion!")
            msg.setText("El campo no puede estar vacio.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def volverAtras(self):
        self.close()
        self.inicio = Inicio()
        self.inicio.show()

class Inicio(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trabajo Integrador - Inteligencia Artificial 1")
        self.setFixedSize(400, 100)
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
            self.close()
            self.cargarNodos = CargaNodos(opcion)
            self.cargarNodos.show()
