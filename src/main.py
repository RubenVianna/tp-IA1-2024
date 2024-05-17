from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
from networkx.drawing.nx_agraph import graphviz_layout
from Models.nodo import Nodo
import networkx as nx
import matplotlib.pyplot as plt

#Funcion que nos crea el grafo ordenado usando graphviz
def crear_y_mostrar_arbol(nodosExplorados):
    G = nx.DiGraph()

    for nodo in nodosExplorados:
        G.add_node(nodo.nombre, heuristica=nodo.heuristica)
        if nodo.padre:
            G.add_edge(nodo.padre, nodo.nombre)

    pos = graphviz_layout(G, prog='dot')  # Usar 'dot' para un layout jerárquico
    labels = {node: f'{node}\n({G.nodes[node]["heuristica"]})' for node in G.nodes()}
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=500, edge_color='gray')
    nx.draw_networkx_labels(G, pos, labels, font_size=10)
    plt.title("Árbol de Máxima Pendiente")
    plt.show()

#ejemplo de como usar la funcion para distancia en linea recta
nodo1 = Nodo('A')
nodo1.coordenada_x=5
nodo1.coordenada_y=4
nodo2 = Nodo('B')
nodo2.coordenada_x=5
nodo2.coordenada_y=4
nodo3 = Nodo('C')
nodo3.coordenada_x=5
nodo3.coordenada_y=14
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
    heuristica = distanciaManhattan(nodos[i],nodo5)
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




recorridoMaximaPendiente, nodosExploradosMP = calcularMaximaPendiente(nodos)
escaladaSimple , nodosExploradosES = calcularEscaladaSimple(nodos)

crear_y_mostrar_arbol(nodosExploradosMP)
crear_y_mostrar_arbol(nodosExploradosES)

for s in recorridoMaximaPendiente:
    print("Paso: ",s.nombre, "Heuristica: ", s.heuristica)

for e in escaladaSimple:
    print("Paso: ",s.nombre, "Heuristica: ", s.heuristica)

# # Crear un grafo vacío
# G = nx.Graph()

# # # Agregar nodos
# # G.add_node(nodo6.nombre)
# # G.add_node(nodo1.nombre)
# # G.add_node(nodo5.nombre)

# # Agregar aristas (edges)
# i= 0
# aristas = None
# while i < cantNodos:
#     for nodo in nodos[i].nombre:
#         G.add_node(nodo, weight=nodos[i].heuristica)
#         for con in nodos[i].conexiones:
#             G.add_edge(nodo, con.nombre)
#     i= i+ 1

# labels = {node: f'{node}\n({G.nodes[node]["weight"]})' for node in G.nodes()}

# # G.add_edge()
# # G.add_edge(nodo2.coordenada_x, 3)
# # G.add_edge(2, 3)

# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=False, node_color='skyblue', edge_color='gray', node_size=600, font_size=10)
# nx.draw_networkx_labels(G, pos, labels, font_size=10)

# # Mostrar el grafo
# plt.show()

#------------------ ARBOL-------------------------------------
