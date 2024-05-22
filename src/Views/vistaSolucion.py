from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Controllers.graficos import *
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
import networkx as nx

class VistaSolucion(QWidget):

    def __init__(self, nodos):
        super().__init__()
        self.nodos = nodos
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visor de Árboles')

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # Título principal
        self.titleLabel = QLabel("Árboles Generados", self)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        mainLayout.addWidget(self.titleLabel)

        # Layout para contener los dos canvas
        canvasLayout = QHBoxLayout()
        mainLayout.addLayout(canvasLayout)

        # Canvas para mostrar el primer árbol
        self.canvas1 = ArbolCanvas(self, width=5, height=4, dpi=100)
        canvasLayout.addWidget(self.canvas1)

        # Canvas para mostrar el segundo árbol
        self.canvas2 = ArbolCanvas(self, width=5, height=4, dpi=100)
        canvasLayout.addWidget(self.canvas2)

        self.graficar_y_mostrar_arboles()

    def graficar_y_mostrar_arboles(self):
        recorridoMaximaPendiente, nodosExploradosMP = calcularMaximaPendiente(self.nodos)
        arbol1, colors1, labels1= graficaryMostrarArbol(nodosExploradosMP, "Arbol Maxima Pendiente", mostrarResultados=True)
        escaladaSimple , nodosExploradosES = calcularEscaladaSimple(self.nodos)
        arbol2, colors2, labels2= graficaryMostrarArbol(nodosExploradosES, "Arbol Escalada Simple", mostrarResultados=True)
        self.canvas1.plot(arbol1, colors1, labels1)
        self.canvas2.plot(arbol2, colors2, labels2)


class ArbolCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, G, colors, labels):
        self.axes.clear()
        pos = graphviz_layout(G, prog='dot')  # Usar 'dot' para un layout jerárquico

        plt.figure(figsize=(10, 7))

        nx.draw(G, pos, ax=self.axes, with_labels=True, node_color=colors, edge_color='gray')
        nx.draw_networkx_labels(G, pos, labels, font_size=10)
        self.draw()