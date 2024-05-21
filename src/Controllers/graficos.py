from networkx.drawing.nx_agraph import graphviz_layout
import networkx as nx
import matplotlib.pyplot as plt

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

    # Extraer las posiciones de los nodos
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=False, node_color='skyblue', edge_color='gray', node_size=600, font_size=10)
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Mostrar el grafo
    plt.show()

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
                # Verificar si el nodo tiene el atributo minLoc y si es 'ML'
                if G.nodes[node]['minLoc'] == 'ML':
                    # Si el atributo minLoc es 'ML', el color es verde
                    colors.append('yellow')
                elif G.nodes[node]['estadoI'] == 'I':
                    # Si el atributo minLoc no es 'ML', el color es skyblue
                    colors.append('red')
                elif G.nodes[node]['estadoF'] == 'F':
                    colors.append('green')
                else:
                    colors.append('skyblue')

        pos = graphviz_layout(G, prog='dot')  # Usar 'dot' para un layout jerárquico

        labels = {node: f'{node}\n({G.nodes[node]["heuristica"]})' for node in G.nodes()}
        plt.figure(figsize=(10, 7))
        if mostrarResultados:
            nx.draw(G, pos, with_labels=False, node_color=colors, node_size=500, edge_color='gray')
        else:
            nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=500, edge_color='gray')
        nx.draw_networkx_labels(G, pos, labels, font_size=10)
        plt.title(titulo)
        plt.show()

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