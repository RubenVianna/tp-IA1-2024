from networkx.drawing.nx_agraph import graphviz_layout
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox

def graficarGrafo(nodos):
    G = nx.Graph()

    for nodo in nodos:
        G.add_node(nodo.nombre, heuristica=nodo.heuristica, minLoc=nodo.minLoc, estadoF=nodo.estadoF, estadoI=nodo.estadoI)

    i= 0
    while i < len(nodos):
        for nodo in nodos[i].nombre:
            G.add_node(nodo, weight=nodos[i].heuristica,pos=(nodos[i].coordenada_x,nodos[i].coordenada_y))
            for con in nodos[i].conexiones:
                G.add_edge(nodo, con.nombre)
        i= i+ 1
    
    colors = []
    for node in G.nodes():
        if G.nodes[node]['estadoI'] == 'I':
            colors.append('red')
        elif G.nodes[node]['estadoF'] == 'F':
            colors.append('green')
        else:
            colors.append('skyblue')
    # Mostrar el grafo

    return G, colors

#Funcion que nos crea el grafo ordenado usando graphviz
def graficaryMostrarArbol(nodosExplorados, titulo, mostrarResultados):
        
        G = nx.DiGraph()
        for nodo in nodosExplorados:
            G.add_node(nodo.nombre, heuristica=nodo.heuristica, minLoc=nodo.minLoc, estadoF=nodo.estadoF, estadoI=nodo.estadoI)
            if nodo.padre:
                G.add_edge(nodo.padre, nodo.nombre)
        
        if mostrarResultados:
            colors = []
            for node in G.nodes():
                if G.nodes[node]['minLoc'] == 'ML':
                    colors.append('yellow')
                elif G.nodes[node]['estadoI'] == 'I':
                    colors.append('red')
                elif G.nodes[node]['estadoF'] == 'F':
                    colors.append('green')
                else:
                    colors.append('skyblue')

        labels = {node: f'{node}\n({G.nodes[node]["heuristica"]})' for node in G.nodes()}

        return G, colors , labels

def graficarPasoAPaso(nodosExplorados, titulo):
    
    # Inicializar una lista vacía para almacenar los nodos acumulativos
    nodos_acumulativos = []

    # Inicializar un contador para rastrear cuántos nodos hemos enviado
    contador_nodos_enviados = 0

    # Definir cuántos nodos enviar en cada iteración
    nodos_por_iteracion = 1

    # Mientras haya nodos por enviar
    while contador_nodos_enviados < len(nodosExplorados):
        # Determinar cuántos nodos enviar en esta iteración
        nodos_a_enviar = min(nodos_por_iteracion, len(nodosExplorados) - contador_nodos_enviados)

        # Obtener los nodos para esta iteración
        nodos_enviados = nodosExplorados[contador_nodos_enviados:contador_nodos_enviados + nodos_a_enviar]

        # Agregar los nuevos nodos a la lista acumulativa
        nodos_acumulativos.extend(nodos_enviados)

        graficaryMostrarArbol(nodos_acumulativos, titulo, mostrarResultados=False)

        # Incrementar el contador de nodos enviados
        contador_nodos_enviados += nodos_a_enviar

    graficaryMostrarArbol(nodosExplorados, titulo, mostrarResultados=True)    

# def graficarPasoAPasoUser(nodosExplorados, titulo):
    
#     # Inicializar una lista vacía para almacenar los nodos acumulativos
#     nodos_acumulativos = []

#     # Inicializar un contador para rastrear cuántos nodos hemos enviado
#     contador_nodos_enviados = 0

#     # Definir cuántos nodos enviar en cada iteración
#     nodos_por_iteracion = 1

#     # Mientras haya nodos por enviar
#     while contador_nodos_enviados < len(nodosExplorados):
#         # Determinar cuántos nodos enviar en esta iteración
#         nodos_a_enviar = min(nodos_por_iteracion, len(nodosExplorados) - contador_nodos_enviados)

#         # Obtener los nodos para esta iteración
#         nodos_enviados = nodosExplorados[contador_nodos_enviados:contador_nodos_enviados + nodos_a_enviar]

#         # Agregar los nuevos nodos a la lista acumulativa
#         nodos_acumulativos.extend(nodos_enviados)

#         # Mostrar la ventana de confirmación
#         confirmacion = QMessageBox.question(None, 'Confirmación', 'Presione Ok para continuar al siguiente paso', QMessageBox.Ok | QMessageBox.Cancel)

#         # Si el usuario confirma, mostrar el siguiente paso
#         if confirmacion == QMessageBox.Ok:
#             graficaryMostrarArbol(nodos_acumulativos, titulo, mostrarResultados=False)
#             # Incrementar el contador de nodos enviados
#             contador_nodos_enviados += nodos_a_enviar
#         else:
#             break

#     # Si el usuario cancela la confirmación, mostrar el resultado final
#     if confirmacion == QMessageBox.Ok:
#         graficaryMostrarArbol(nodosExplorados, titulo, mostrarResultados=True)