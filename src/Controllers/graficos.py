import networkx as nx

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
        if G.nodes[node]['estadoF'] == 'F':
            colors.append('green')
        elif G.nodes[node]['estadoI'] == 'I':
            colors.append('red')
        else:
            colors.append('skyblue')
    # Mostrar el grafo

    return G, colors

def graficaryMostrarArbol(nodosExplorados, titulo, mostrarResultados):
        
        G = nx.DiGraph()
        colors = []
        for nodo in nodosExplorados:
            G.add_node(nodo.nombre, heuristica=nodo.heuristica, minLoc=nodo.minLoc, estadoF=nodo.estadoF, estadoI=nodo.estadoI)
            if nodo.padre:
                G.add_edge(nodo.padre, nodo.nombre)
        
        if mostrarResultados:
            for node in G.nodes():
                if G.nodes[node]['estadoF'] == 'F':
                    colors.append('green')
                elif G.nodes[node]['minLoc'] == 'ML':
                    colors.append('yellow')
                elif G.nodes[node]['estadoI'] == 'I':
                    colors.append('red')
                else:
                    colors.append('skyblue')

        labels = {node: f'{node}\n({G.nodes[node]["heuristica"]})' for node in G.nodes()}

        return G, colors , labels