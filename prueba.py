import sys
import networkx as nx
import matplotlib.pyplot as plt
from Controllers.maximaPendiente import calcularMaximaPendiente
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coordenada_x = None
        self.coordenada_y = None
        self.heuristica = None
        self.estadoI = None
        self.estadoF = None
        self.minLoc = None
        self.padre = None
        self.conexiones = []

def existe_nodo(lista, nombre):
    return any(nodo.nombre == nombre for nodo in lista)

def calcularMaximaPendiente(nodos):
    nodosAlf = sorted(nodos, key=lambda x: x.nombre)  # Ordenamos alfabeticamente los nodos
    recorridoMaxPendiente = []
    nodosExplorados = []
    nodosOrdenados = []

    # Se ordena el array de nodos recibido para comenzar a recorrer por el nodo Inicial
    for nodo in nodosAlf:
        if nodo.estadoI == 'I':
            nodoInicial = nodo
            nodosOrdenados.insert(0, nodoInicial)
        else:
            nodosOrdenados.append(nodo)

    for nodo in nodosOrdenados:
        print("la heuristica de", nodo.nombre, "es", nodo.heuristica)

    solucionActual = nodosOrdenados[0]  # Definimos al primer nodo como solucion actual antes de comenzar a recorrer los demas nodos
    nodosNoExplorados = nodosOrdenados.copy()  # Se hace una copia para no alterar el orden de los nodos cargados

    bandera = True
    while bandera:
        for nodoActual in nodosOrdenados:
            if solucionActual == nodoActual:
                print("------------------------------------------------------------")
                print("Analizando nodo:", nodoActual.nombre, "con padre:", nodoActual.padre)
                recorridoMaxPendiente.append(nodoActual)
                if not existe_nodo(nodosExplorados, nodoActual.nombre):
                    nodosExplorados.append(nodoActual)
                if nodoActual.estadoF == 'F':
                    solucionActual = nodoActual
                    bandera = False
                else:
                    if nodoActual.conexiones:
                        for conexion in nodoActual.conexiones:  # Recorro las conexiones del nodo actual para ver con que nodos tengo que comparar la heuristica
                            nodosConectados = []  # Defino un array para ir cargando la heuristica de los nodos que estan relacionados
                            for nodoAux in nodosNoExplorados:  # Recorro el array de nodos no explorados
                                if nodoAux.nombre == conexion.nombre:  # Controlo si el nodo del array de nodos no explorados es alguno de los nodos conectados al nodo actual
                                    if not existe_nodo(nodosExplorados, nodoAux.nombre):
                                        nodoAux.padre = nodoActual.nombre
                                        nodosExplorados.append(nodoAux)
                                        nodosConectados.append(nodoAux)  # Agrego el nodo al array de nodos conectados para evaluar despues si su heuristica es mejor que el de la solucion actual
                            for nC in nodosConectados:
                                print(nodoActual.nombre, nC.nombre, nC.heuristica)
                                if nC.heuristica < solucionActual.heuristica:
                                    solucionActual = nC
                                    if solucionActual.estadoF is None:
                                        solucionActual.minLoc = "ML"
                                        bandera = False
                    else:
                        print("el nodo:", nodoActual.nombre, "no posee hijos")
                        solucionActual.minLoc = "ML"
                        break

    if solucionActual.minLoc == 'ML':
        print("la solucion es un Minimo Local:", solucionActual.nombre)
    else:
        print("la solucion es:", solucionActual.nombre)

    print("---------------------recorrido------------------------------")
    for i in recorridoMaxPendiente:
        print(i.heuristica, i.nombre)
    print("------------------------------------------------------------")

    for e in nodosExplorados:
        print(e.nombre)

    return recorridoMaxPendiente, nodosExplorados

def crear_y_mostrar_arbol(nodosExplorados):
    G = nx.DiGraph()

    for nodo in nodosExplorados:
        G.add_node(nodo.nombre, heuristica=nodo.heuristica)
        if nodo.padre:
            G.add_edge(nodo.padre, nodo.nombre)

    pos = nx.spring_layout(G)  # Usar 'spring_layout' para un layout jerárquico
    labels = {node: f'{node}\n({G.nodes[node]["heuristica"]})' for node in G.nodes()}
    fig, ax = plt.subplots(figsize=(10, 7))
    nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=500, edge_color='gray', ax=ax)
    nx.draw_networkx_labels(G, pos, labels, font_size=10)
    ax.set_title("Árbol de Máxima Pendiente")
    return fig

class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grafo Inicial")

        # Crear el grafo inicial
        self.G = nx.Graph()
        self.G.add_node("A", pos=(0, 1))
        self.G.add_node("B", pos=(1, 1))
        self.G.add_node("C", pos=(1, 0))
        self.G.add_node("D", pos=(0, 0))
        self.G.add_edge("A", "B")
        self.G.add_edge("B", "C")
        self.G.add_edge("C", "D")
        self.G.add_edge("D", "A")
        self.G.add_edge("A", "C")

        self.pos = nx.get_node_attributes(self.G, 'pos')

        # Dibujar el grafo inicial
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        nx.draw(self.G, self.pos, with_labels=True, node_size=700, node_color="skyblue", edge_color="gray", font_size=14, ax=self.ax)
        self.ax.set_title("Grafo Inicial")

        # Crear un canvas de matplotlib para PyQt5
        self.canvas = FigureCanvas(self.fig)

        # Crear un botón
        self.button = QPushButton("Calcular Máxima Pendiente")
        self.button.clicked.connect(self.on_button_clicked)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.button)

        # Crear un contenedor
        self.container = QWidget()
        self.container.setLayout(self.layout)

        # Establecer el contenedor como el widget central
        self.setCentralWidget(self.container)

    def on_button_clicked(self):
         #ejemplo de como usar la funcion para distancia en linea recta
        nodo1 = Nodo('A')
        nodo1.coordenada_x=1
        nodo1.coordenada_y=2
        nodo2 = Nodo('B')
        nodo2.coordenada_x=8
        nodo2.coordenada_y=6
        nodo3 = Nodo('C')
        nodo3.coordenada_x=8
        nodo3.coordenada_y=1
        nodo4 = Nodo('D')
        nodo4.coordenada_x=10
        nodo4.coordenada_y=2
        nodo5 = Nodo('E')
        nodo5.coordenada_x=4
        nodo5.coordenada_y=6
        nodo6 = Nodo('F')
        nodo6.coordenada_x=15
        nodo6.coordenada_y=8

        cantNodos = 6

        #definimos al nodo 5 como nodo final
        nodo5.estadoF = 'F'

        nodo1.estadoI = 'I'

        #logica
        nodos= []

        nodos+=[nodo6,nodo1,nodo5,nodo3,nodo4,nodo2]

        # calculo de heuristica
        i= 0
        while i < cantNodos:
            heuristica = (nodos[i],nodo5)
            nodos[i].heuristica = heuristica
            i= i+ 1


        #relaciones nodo A (B,C)
        nodo1.conexiones.append(nodo2)
        nodo1.conexiones.append(nodo3)

        #relaciones nodo B (A,D)
        nodo2.conexiones.append(nodo1)
        nodo2.conexiones.append(nodo4)

        #relaciones nodo C (A,D,E)
        nodo3.conexiones.append(nodo1)
        nodo3.conexiones.append(nodo4)
        nodo3.conexiones.append(nodo5)

        #relaciones nodo D (B,E)
        nodo4.conexiones.append(nodo2)
        nodo4.conexiones.append(nodo5)

        #relaciones nodo E (C,D,F)
        nodo5.conexiones.append(nodo3)
        nodo5.conexiones.append(nodo4)
        nodo5.conexiones.append(nodo6)

        #relaciones nodo F (E)
        nodo6.conexiones.append(nodo5)

        recorridoMaxPendiente, nodosExplorados = calcularMaximaPendiente(nodos)
        fig = crear_y_mostrar_arbol(nodosExplorados)

        # Mostrar la nueva ventana con el árbol generado
        self.tree_window = TreeWindow(fig)
        self.tree_window.show()

class TreeWindow(QDialog):
    def __init__(self, fig, parent=None):
        super(TreeWindow, self).__init__(parent)
        self.setWindowTitle("Árbol de Máxima Pendiente")
        
        # Crear un canvas de matplotlib para PyQt5
        self.canvas = FigureCanvas(fig)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)

        # Crear un contenedor
        self.container = QWidget()
        self.container.setLayout(self.layout)

        # Establecer el contenedor como el widget central
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = GraphWindow()
    window.show()

    sys.exit(app.exec_())
