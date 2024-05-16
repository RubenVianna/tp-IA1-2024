from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Controllers.maximaPendiente import calcularMaximaPendiente
from Models.nodo import Nodo
import networkx as nx
import matplotlib.pyplot as plt

#ejemplo de como usar la funcion para distancia en linea recta
nodo1 = Nodo('A')
nodo1.coordenada_x=1
nodo1.coordenada_y=2
nodo2 = Nodo('B')
nodo2.coordenada_x=4
nodo2.coordenada_y=6
nodo3 = Nodo('C')
nodo3.coordenada_x=8
nodo3.coordenada_y=1
nodo4 = Nodo('D')
nodo4.coordenada_x=10
nodo4.coordenada_y=2
nodo5 = Nodo('E')
nodo5.coordenada_x=12
nodo5.coordenada_y=10
nodo6 = Nodo('F')
nodo6.coordenada_x=15
nodo6.coordenada_y=8

cantNodos = 6

#definimos al nodo 5 como nodo final
nodo5.estadoF = 'F'
nodo1.estadoI = 'I'

#logica

#relaciones nodo A (B,C)
nodo1.conexiones.append(nodo2.nombre)
nodo1.conexiones.append(nodo3.nombre)

#relaciones nodo B (A,D)
nodo2.conexiones.append(nodo1.nombre)
nodo2.conexiones.append(nodo4.nombre)

#relaciones nodo C (A,D,E)
nodo3.conexiones.append(nodo1.nombre)
nodo3.conexiones.append(nodo4.nombre)
nodo3.conexiones.append(nodo5.nombre)

#relaciones nodo D (B,E)
nodo4.conexiones.append(nodo2.nombre)
nodo4.conexiones.append(nodo5.nombre)

#relaciones nodo E (C,D,F)
nodo5.conexiones.append(nodo3.nombre)
nodo5.conexiones.append(nodo4.nombre)
nodo5.conexiones.append(nodo6.nombre)

#relaciones nodo F (E)
nodo6.conexiones.append(nodo5.nombre)

nodos= []

nodos+=[nodo6,nodo1,nodo5,nodo3,nodo4,nodo2]

# calculo de heuristica
i= 0
while i < cantNodos:
    heuristica = distanciaManhattan(nodos[i],nodo5)
    nodos[i].heuristica = heuristica
    i= i+ 1

#calcularMaximaPendiente(nodos)

# Crear un grafo vacío
G = nx.Graph()

# # Agregar nodos
# G.add_node(nodo6.nombre)
# G.add_node(nodo1.nombre)
# G.add_node(nodo5.nombre)

# Agregar aristas (edges)
i= 0
aristas = None
while i < cantNodos:
    for nodo in nodos[i].nombre:
        for con in nodos[i].conexiones:
            G.add_edge(nodo, con)
    i= i+ 1



# G.add_edge()
# G.add_edge(nodo2.coordenada_x, 3)
# G.add_edge(2, 3)

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=200, font_size=10)

# Mostrar el grafo
plt.show()