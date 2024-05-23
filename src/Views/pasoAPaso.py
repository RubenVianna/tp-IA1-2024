from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
from Controllers.graficos import graficaryMostrarArbol
from matplotlib.figure import Figure
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

class GraficacionPasoAPaso(QWidget):

    def __init__(self, nodos, vistaAnterior):
        super().__init__()
        self.nodos = nodos
        self.vistaAnterior = vistaAnterior
        self.contador_es = 0
        self.contador_mp = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visor de Árboles')
        self.setGeometry(100, 100, 1000, 800)

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

        self.button_siguiente_es = QPushButton("Siguiente Escalada Simple")
        self.button_siguiente_es.setFont(QFont("Arial", 10))
        self.button_siguiente_es.clicked.connect(self.siguientePasoES)
        mainLayout.addWidget(self.button_siguiente_es)

        self.button_siguiente_mp = QPushButton("Siguiente Máxima Pendiente")
        self.button_siguiente_mp.setFont(QFont("Arial", 10))
        self.button_siguiente_mp.clicked.connect(self.siguientePasoMP)
        mainLayout.addWidget(self.button_siguiente_mp)

        self.atras = QPushButton("Atrás")
        self.atras.setFont(QFont("Arial", 10))
        self.atras.clicked.connect(self.volverAtras)
        mainLayout.addWidget(self.atras)

        self.colorReferences = QLabel(self)
        self.colorReferences.setText("Referencias de colores:\nRojo = Inicio\nVerde = Final\nAmarillo = Mínimo Local")
        self.colorReferences.setStyleSheet("font-size: 14px; font-weight: bold;")
        mainLayout.addWidget(self.colorReferences)

        self.graficar_y_mostrar_arboles()

    def siguientePasoES(self):
        if self.contador_es < len(self.nodosExploradosES):
            self.contador_es += 1
            self.graficar_y_mostrar_arbol_escalada_simple()

    def siguientePasoMP(self):
        if self.contador_mp < len(self.nodosExploradosMP):
            self.contador_mp += 1
            self.graficar_y_mostrar_arbol_maxima_pendiente()

    def graficar_y_mostrar_arboles(self):
        self.escaladaSimple , self.nodosNoExploradosES, self.nodosExploradosES = calcularEscaladaSimple(self.nodos)
        self.recorridoMaximaPendiente, self.nodosExploradosMP = calcularMaximaPendiente(self.nodos)

        self.contador_es = 0
        self.contador_mp = 0

        self.graficar_y_mostrar_arbol_escalada_simple()
        self.graficar_y_mostrar_arbol_maxima_pendiente()

    def graficar_y_mostrar_arbol_escalada_simple(self):
        if self.contador_es > 0:
            nodos_mostrar = self.nodosExploradosES[:self.contador_es]
        else:
            nodos_mostrar = []

        final_iteration = (self.contador_es == len(self.nodosExploradosES))
        arbol, colors, labels = graficaryMostrarArbol(nodos_mostrar, "Arbol Escalada Simple", mostrarResultados=final_iteration)
        self.canvas1.plot(arbol, colors, labels)

    def graficar_y_mostrar_arbol_maxima_pendiente(self):
        if self.contador_mp > 0:
            nodos_mostrar = self.nodosExploradosMP[:self.contador_mp]
        else:
            nodos_mostrar = []

        final_iteration = (self.contador_mp == len(self.nodosExploradosMP))
        arbol, colors, labels = graficaryMostrarArbol(nodos_mostrar, "Arbol Maxima Pendiente", mostrarResultados=final_iteration)
        self.canvas2.plot(arbol, colors, labels)

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
        if len(colors)==0:
            self.colors='skyblue'
        else:
            self.colors = colors
        self.axes.clear()
        pos = graphviz_layout(G, prog='dot')
        nx.draw(G, pos, ax=self.axes, with_labels=False, node_color=self.colors, node_size=600, edge_color='gray')
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold', ax=self.axes)
        self.draw()

