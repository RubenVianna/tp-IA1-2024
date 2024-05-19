from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
from networkx.drawing.nx_agraph import graphviz_layout
from Models.nodo import Nodo
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
def crear_y_mostrar_arbol(nodosExplorados, titulo, mostrarResultados):
        
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
        plt.title('Seteando titulo')
        plt.show()

def graficarPasoAPaso(nodosExploradosES, titulo):
    
    # Inicializar una lista vacía para almacenar los nodos acumulativos
    nodos_acumulativos = []

    # Inicializar un contador para rastrear cuántos nodos hemos enviado
    contador_nodos_enviados = 0

    # Definir cuántos nodos enviar en cada iteración
    nodos_por_iteracion = 1

    # Mientras haya nodos por enviar
    while contador_nodos_enviados < len(nodosExploradosES):
        # Determinar cuántos nodos enviar en esta iteración
        nodos_a_enviar = min(nodos_por_iteracion, len(nodosExploradosES) - contador_nodos_enviados)

        # Obtener los nodos para esta iteración
        nodos_enviados = nodosExploradosES[contador_nodos_enviados:contador_nodos_enviados + nodos_a_enviar]

        # Agregar los nuevos nodos a la lista acumulativa
        nodos_acumulativos.extend(nodos_enviados)

        crear_y_mostrar_arbol(nodos_acumulativos, 'Arbol Maxima Pendiente', mostrarResultados=False)

        # Incrementar el contador de nodos enviados
        contador_nodos_enviados += nodos_a_enviar

    crear_y_mostrar_arbol(nodosExploradosES, 'Arbol Maxima Pendiente', mostrarResultados=True)    

#ejemplo de como usar la funcion para distancia en linea recta
nodo1 = Nodo('A')
nodo1.coordenada_x=1
nodo1.coordenada_y=1
nodo2 = Nodo('B')
nodo2.coordenada_x=2
nodo2.coordenada_y=2
nodo3 = Nodo('C')
nodo3.coordenada_x=3
nodo3.coordenada_y=3
nodo4 = Nodo('D')
nodo4.coordenada_x=4
nodo4.coordenada_y=4
nodo5 = Nodo('E')
nodo5.coordenada_x=5
nodo5.coordenada_y=5
nodo6 = Nodo('F')
nodo6.coordenada_x=6
nodo6.coordenada_y=6
nodo7 = Nodo('G')
nodo7.coordenada_x=7
nodo7.coordenada_y=7

cantNodos = 7

#definimos al nodo 5 como nodo final
nodo7.estadoF = 'F'
nodo1.estadoI = 'I'

#logica
nodos= []

nodos+=[nodo6,nodo1,nodo5,nodo3,nodo4,nodo2,nodo7]

# calculo de heuristica
i= 0
while i < cantNodos:
    heuristica = distanciaManhattan(nodos[i],nodo7)
    nodos[i].heuristica = heuristica
    i= i+ 1


#relaciones nodo A (B,C)
nodo1.conexiones.append(nodo2)
nodo1.conexiones.append(nodo3)

#relaciones nodo B (A,C,D)
nodo2.conexiones.append(nodo1)
nodo2.conexiones.append(nodo4)
nodo2.conexiones.append(nodo3)

#relaciones nodo C (A,B,D,E,G)
nodo3.conexiones.append(nodo1)
nodo3.conexiones.append(nodo4)
nodo3.conexiones.append(nodo5)
nodo3.conexiones.append(nodo2)
nodo3.conexiones.append(nodo7)

#relaciones nodo D (B,E)
nodo4.conexiones.append(nodo2)
nodo4.conexiones.append(nodo5)

#relaciones nodo E (C,D,F)
nodo5.conexiones.append(nodo3)
nodo5.conexiones.append(nodo4)
nodo5.conexiones.append(nodo6)

#relaciones nodo F (E)
nodo6.conexiones.append(nodo5)

#graficarGrafo(nodos)

recorridoMaximaPendiente, nodosExploradosMP = calcularMaximaPendiente(nodos)

# print("-------------------------------------------")

#escaladaSimple , nodosExploradosES = calcularEscaladaSimple(nodos)

print('Maxima pendiente')
for s in recorridoMaximaPendiente:
    print("Paso: ",s.nombre, "Heuristica: ", s.heuristica, 'con padre:', s.padre, "es un minimo local:", s.minLoc)

# print('Escalada Simple')
# for e in escaladaSimple:
#     print("Paso: ",e.nombre, "Heuristica: ", e.heuristica, 'con padre:', e.padre, "es un minimo local:", e.minLoc)

# crear_y_mostrar_arbol(nodosExploradosES, 'Arbol Maxima Pendiente', mostrarResultados=True)

#graficarPasoAPaso(nodosExploradosES,'Arbol Escalada Simple')

graficarPasoAPaso(nodosExploradosMP,'Arbol Escalada Simple')

#------------------ ARBOL-------------------------------------
