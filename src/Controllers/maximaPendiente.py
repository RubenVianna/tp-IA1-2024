def existe_nodo(listaNodos, nombre):
    return any(nodo.nombre == nombre for nodo in listaNodos)


def calcularMaximaPendiente(nodos, nodoActual=None, solucionActual=None, recorridoMaxPendiente=None, nodosExplorados=None):
    if recorridoMaxPendiente is None:
        recorridoMaxPendiente = []
    if nodosExplorados is None:
        nodosExplorados = []
    
    # Ordenamos alfabéticamente los nodos al inicio de la primera llamada
    if nodoActual is None and solucionActual is None:
        nodosAlf = sorted(nodos, key=lambda x: x.nombre) # ordenamos alfabéticamente los nodos
        nodosOrdenados = []

        # Se ordena el array de nodos recibido para comenzar a recorrer por el nodo Inicial
        for nodo in nodosAlf:
            if nodo.estadoI == 'I':
                nodoInicial = nodo
                nodosOrdenados.insert(0, nodoInicial)
            else:
                nodosOrdenados.append(nodo)
        
        # Imprimimos la heurística de cada nodo
        for nodo in nodosOrdenados:
            print("La heurística de", nodo.nombre, "es", nodo.heuristica)
        
        # Definimos al primer nodo como solución actual antes de comenzar a recorrer los demás nodos
        solucionActual = nodosOrdenados[0]
        nodoActual = solucionActual
    
    # Agregamos el nodo actual al recorrido máximo pendiente y nodos explorados
    recorridoMaxPendiente.append(nodoActual)
    if not existe_nodo(nodosExplorados, nodoActual.nombre):
        nodosExplorados.append(nodoActual)

    print("------------------------------------------------------------")
    print("Analizando nodo:", nodoActual.nombre, "con padre:", nodoActual.padre)

    if nodoActual.estadoF == 'F':
        print("La solución es:", nodoActual.nombre)
        return recorridoMaxPendiente, nodosExplorados
    else:
        if nodoActual.conexiones != []:
            nodosConectados = []
            for conexion in nodoActual.conexiones:
                for nodoAux in nodos:
                    if nodoAux.nombre == conexion.nombre:
                        print(nodoActual.nombre, nodoAux.nombre, nodoAux.heuristica)
                        if nodoAux.estadoF == 'F':
                            nodoAux.padre = nodoActual.nombre
                            nodosExplorados.append(nodoAux)
                            nodosConectados.append(nodoAux)
                            recorridoMaxPendiente.append(nodoAux)
                            print("La solución es:", nodoAux.nombre)
                            return recorridoMaxPendiente, nodosExplorados
                        if not existe_nodo(nodosExplorados, nodoAux.nombre):
                            nodoAux.padre = nodoActual.nombre
                            nodosExplorados.append(nodoAux)
                            nodosConectados.append(nodoAux)
            for nC in nodosConectados:
                if nC.heuristica < solucionActual.heuristica:
                    solucionActual = nC
        
        if nodoActual == solucionActual:
            print("El nodo:", nodoActual.nombre, "no posee hijos o no hay mejor opción")
            solucionActual.minLoc = "ML"
            print("La solución es un Mínimo Local:", solucionActual.nombre)
            return recorridoMaxPendiente, nodosExplorados
        else:
            return calcularMaximaPendiente(nodos, nodoActual, solucionActual, recorridoMaxPendiente, nodosExplorados)