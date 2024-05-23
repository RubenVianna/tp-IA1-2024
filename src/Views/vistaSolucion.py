from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from networkx.drawing.nx_agraph import graphviz_layout
from Controllers.graficos import *
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
from Views.comparacionSoluciones import ComparacionSoluciones
import networkx as nx

class VistaSolucion(QWidget):

    def __init__(self, nodos, vistaAnterior):
        super().__init__()
        self.nodos = nodos
        self.vistaAnterior = vistaAnterior
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visor de Árboles')

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # Título principal
        self.titleLabel = QLabel("Árboles Generados", self)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        mainLayout.addWidget(self.titleLabel)

        # Layout para los dos árboles
        treesLayout = QHBoxLayout()
        mainLayout.addLayout(treesLayout)

        # Layout para el primer árbol con título
        tree1Layout = QVBoxLayout()
        self.tree1Title = QLabel("Solución con Escalada Simple", self)
        self.tree1Title.setStyleSheet("font-size: 16px; font-weight: bold;")
        tree1Layout.addWidget(self.tree1Title)
        self.canvas1 = ArbolCanvas(self, width=5, height=4, dpi=100)
        tree1Layout.addWidget(self.canvas1)
        treesLayout.addLayout(tree1Layout)

        # Layout para el segundo árbol con título
        tree2Layout = QVBoxLayout()
        self.tree2Title = QLabel("Solución con Máxima Pendiente", self)
        self.tree2Title.setStyleSheet("font-size: 16px; font-weight: bold;")
        tree2Layout.addWidget(self.tree2Title)
        self.canvas2 = ArbolCanvas(self, width=5, height=4, dpi=100)
        tree2Layout.addWidget(self.canvas2)
        treesLayout.addLayout(tree2Layout)

        self.graficar_y_mostrar_arboles()

        self.button = QPushButton("Ver Comparación")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.verConexiones)
        mainLayout.addWidget(self.button)
        self.atras = QPushButton("Atrás")
        self.atras.setFont(QFont("Arial", 10))
        self.atras.clicked.connect(self.volverAtras)
        mainLayout.addWidget(self.atras)
        # Cuadro de texto para las referencias de colores (no editable)
        self.colorReferences = QLabel(self)
        self.colorReferences.setText("Refencias de colores:\nRojo = Inicio\nVerde = Final\nAmarillo = Mínimo Local")
        self.colorReferences.setStyleSheet("font-size: 14px; font-weight: bold;")
        mainLayout.addWidget(self.colorReferences)
    
    def verConexiones(self):
        self.comparativa = ComparacionSoluciones(self.nodos)
        self.comparativa.show()

    def graficar_y_mostrar_arboles(self):
        escaladaSimple , nodosNoExploradosES, nodosExploradosES = calcularEscaladaSimple(self.nodos)
        arbol1, colors1, labels1= graficaryMostrarArbol(nodosExploradosES, "Arbol Escalada Simple", mostrarResultados=True)
        recorridoMaximaPendiente, nodosExploradosMP = calcularMaximaPendiente(self.nodos)
        arbol2, colors2, labels2= graficaryMostrarArbol(nodosExploradosMP, "Arbol Maxima Pendiente", mostrarResultados=True)
        self.canvas1.plot(arbol1, colors1, labels1)
        self.canvas2.plot(arbol2, colors2, labels2)
    
    def volverAtras(self):
        self.close()
        self.vistaAnterior.show()


class ArbolCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, G, colors, labels):
        self.axes.clear()
        pos = graphviz_layout(G, prog='dot')  # Usar 'dot' para un layout jerárquico
        nx.draw(G, pos,ax=self.axes, with_labels=False, node_color=colors, node_size=600, edge_color='gray')
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold', ax=self.axes)