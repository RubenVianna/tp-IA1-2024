from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Controllers.graficos import graficaryMostrarArbol
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
from Views.comparacionSoluciones import ComparacionSoluciones
import networkx as nx
import copy

class VistaSolucion(QWidget):

    def __init__(self, nodos, vistaAnterior):
        super().__init__()
        self.nodosES = copy.deepcopy(nodos)
        self.nodosMP = copy.deepcopy(nodos)
        self.vistaAnterior = vistaAnterior
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visor de Árboles')
        self.setFixedSize(900, 600)  # Establece el tamaño fijo de la ventana

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # Título principal
        self.titleLabel = QLabel("Árboles Generados", self)
        self.titleLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
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

        self.graficarArboles()

        # Cuadro de texto para las referencias de colores (no editable)
        self.colorReferences = QLabel(self)
        self.colorReferences.setText("Refencias de colores:\nRojo = Inicio\nVerde = Final\nAmarillo = Mínimo Local")
        self.colorReferences.setStyleSheet("font-size: 14px; font-weight: bold;")
        mainLayout.addWidget(self.colorReferences)

      # Layout para los botones
        buttonsLayout = QHBoxLayout()
        mainLayout.addLayout(buttonsLayout)

        self.button = QPushButton("Ver Comparación")
        self.button.setFont(QFont("Arial", 10))
        self.button.clicked.connect(self.verConexiones)
        buttonsLayout.addWidget(self.button)

        self.atras = QPushButton("Atrás")
        self.atras.setFont(QFont("Arial", 10))
        self.atras.clicked.connect(self.volverAtras)
        buttonsLayout.addWidget(self.atras)
    
    def verConexiones(self):
        self.comparativa = ComparacionSoluciones(self.nodosES, self.nodosMP)
        self.comparativa.show()

    def graficarArboles(self):
        self.nodosExploradosES = calcularEscaladaSimple(self.nodosES)
        self.nodosExploradosES = copy.deepcopy(self.nodosExploradosES)
        self.arbol1, self.colors1, self.labels1= graficaryMostrarArbol(self.nodosExploradosES, "Arbol Escalada Simple", mostrarResultados=True)
        self.arbol1 = copy.deepcopy(self.arbol1)
        self.colors1 = copy.deepcopy(self.colors1)
        self.labels1 = copy.deepcopy(self.labels1)

        for col in self.colors1:
            print('primera iteracion de ES: ', col)
        print('----------------------')


        self.canvas1.plot(self.arbol1, self.colors1, self.labels1)

        self.nodosExploradosMP = calcularMaximaPendiente(self.nodosMP)
        self.nodosExploradosMP = copy.deepcopy(self.nodosExploradosMP)
        self.arbol2, self.colors2, self.labels2= graficaryMostrarArbol(self.nodosExploradosMP, "Arbol Maxima Pendiente", mostrarResultados=True)
        self.arbol2 = copy.deepcopy(self.arbol2)
        self.colors2 = copy.deepcopy(self.colors2)
        self.labels2 = copy.deepcopy(self.labels2)

        for col in self.colors2:
            print('primera iteracion de MP: ', col)
        print('----------------------')

        for col in self.colors2:
            print('segunda iteracion de ES: ', col)
        print('----------------------')

        self.canvas2.plot(self.arbol2, self.colors2, self.labels2)
    
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
        pos = self.generarArbol(G)
        nx.draw(G, pos,ax=self.axes, with_labels=False, node_color=colors, node_size=600, edge_color='gray')
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold', ax=self.axes)

    def generarArbol(self,G):
        pos = {}
        levels = {}  # Diccionario para almacenar los nodos por nivel
                # Agrupar nodos por nivel
        for node in G.nodes():
            level = G.nodes[node]["padre"]  # Obtener el nivel del nodo
            if level not in levels:
                levels[level] = []
            levels[level].append(node)

        # Calcular las posiciones de los nodos
        x_step = 1.0  # Distancia horizontal entre niveles
        y_step = -1.0  # Distancia vertical entre nodos en el mismo nivel
        y_offset = 0  # Desplazamiento vertical inicial
        for level, nodes in levels.items():
            x_offset = -((len(nodes) - 1) * x_step) / 2  # Calcula el desplazamiento horizontal inicial para centrar los nodos
            for node in nodes:
                pos[node] = (x_offset, y_offset)
                x_offset += x_step
            y_offset += y_step

        return pos