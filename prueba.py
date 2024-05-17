import sys
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGridLayout, QLabel, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class NetworkGraph(QWidget):
    def __init__(self):
        super().__init__()

        # Crear un grafo con NetworkX (aquí puedes construir tu propio grafo)
        G = nx.complete_graph(4)

        # Crear una escena de gráficos de PyQt5
        self.scene = QGraphicsScene(self)
        
        # Dibujar el grafo en la escena de PyQt5
        fig, ax = plt.subplots()
        nx.draw(G, ax=ax, with_labels=True, node_color='yellow', edge_color='gray', node_size=500, font_size=12)
        
        # Crear un lienzo de Matplotlib
        self.canvas = FigureCanvas(fig)

        # Agregar el lienzo a la escena
        self.scene.addWidget(self.canvas)

        # Crear una vista de gráficos de PyQt5
        self.view = QGraphicsView(self.scene)

        # Crear un cuadro de diálogo que dice "Hola Mundo"
        b= 'Una prueba de concatenacion'
        s="['A','B','C']" + b

        self.label = QLabel(s)

        # Configurar el diseño
        layout = QGridLayout()
        layout.addWidget(self.view, 0, 1)  # Agregar la vista del gráfico en la columna 0, fila 0
        layout.addWidget(self.label, 0, 0)  # Agregar el cuadro de diálogo en la columna 1, fila 0
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NetworkGraph()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle('NetworkX Graph with Dialog in PyQt5')
    window.show()
    sys.exit(app.exec_())

