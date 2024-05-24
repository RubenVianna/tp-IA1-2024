from Controllers.graficos import graficarGrafo
from Views.vistaSolucion import VistaSolucion
from Views.pasoAPaso import GraficacionPasoAPaso
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx

class VistaGrafo(QWidget):
    def __init__(self, nodos, vistaAnterior):
        super().__init__()
        self.nodos = nodos
        self.vistaAnterior = vistaAnterior
        self.heuristics = {}  # Diccionario para guardar los QLineEdit
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grafo Generado')

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # Título principal
        self.titleLabel = QLabel("Grafo Generado", self)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        mainLayout.addWidget(self.titleLabel)

        # Layout para el contenido principal (grafo y heurísticas)
        contentLayout = QHBoxLayout()
        mainLayout.addLayout(contentLayout)

        # Layout para el grafo
        graphLayout = QVBoxLayout()
        self.canvas = GrafoCanvas(self, width=5, height=4, dpi=100)
        graphLayout.addWidget(self.canvas)
        contentLayout.addLayout(graphLayout)


        # Layout para las heurísticas
        heuristicsLayout = QVBoxLayout()


        # Cuadro de texto para las referencias de colores (no editable)
        references = QLabel(self)
        references.setText("Refencias de colores:\n\nRojo = Inicio\nVerde = Final\nAmarillo = Mínimo Local\n")
        references.setStyleSheet("font-size: 12px; font-weight: bold;")
        heuristicsLayout.addWidget(references)
        
        # Título de heurísticas
        heuristicsTitle = QLabel("Heurísticas", self)
        heuristicsTitle.setStyleSheet("font-size: 16px; font-weight: bold;")
        heuristicsLayout.addWidget(heuristicsTitle)

        formLayout = QFormLayout()
        for nodo in self.nodos:
            heuristicInput = QLineEdit(self)
            heuristicInput.setText(str(nodo.heuristica))
            heuristicInput.setReadOnly(True)  # Hacer el campo no editable
            self.heuristics[nodo.nombre] = heuristicInput
            formLayout.addRow(f"Heurística de {nodo.nombre}:", heuristicInput)
        heuristicsLayout.addLayout(formLayout)

        # Botones
        buttonLayout = QHBoxLayout()
        self.stepButton = QPushButton('Generar Paso a Paso', self)
        self.solutionButton = QPushButton('Ver Solución', self)
        self.atras = QPushButton("Atrás")
        buttonLayout.addWidget(self.stepButton)
        buttonLayout.addWidget(self.solutionButton)
        buttonLayout.addWidget(self.atras)
        heuristicsLayout.addLayout(buttonLayout)
        contentLayout.addLayout(heuristicsLayout)

        self.atras.clicked.connect(self.volverAtras)
        self.stepButton.clicked.connect(self.verPasoAPaso)
        self.solutionButton.clicked.connect(self.verSolucion)

        self.mostrar_grafo()

    def mostrar_grafo(self):
        G, colors = graficarGrafo(self.nodos)
        self.canvas.plot(G, colors)
    
    def verPasoAPaso(self):
        self.hide()
        self.vistaGrafo = GraficacionPasoAPaso(self.nodos,self)
        self.vistaGrafo.show()

    def verSolucion(self):
        # Lógica para ver la solución completa del grafo
        self.hide()
        self.vistaGrafo = VistaSolucion(self.nodos,self)
        self.vistaGrafo.show()

    def volverAtras(self):
        self.close()
        self.vistaAnterior.show()


class GrafoCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, G, colors):
        self.axes.clear()
        # Extraer las posiciones de los nodos
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, ax=self.axes, with_labels=True, node_color=colors, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_size=10)
        self.draw()


