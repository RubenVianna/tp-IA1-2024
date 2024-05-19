def existe_nodo(listaNodos, nombre):
    return any(nodo.nombre == nombre for nodo in listaNodos)

# def calcularMaximaPendiente(nodos):
#     nodosAlf = sorted(nodos, key=lambda x: x.nombre) #ordenamos alfabeticamente los nodos
#     recorridoMaxPendiente = []
#     nodosExplorados = []
#     nodosOrdenados = []

#     # se ordena el array de nodos recibido para comenzar a recorrer por el nodo Inicial
#     for nodo in nodosAlf:
#         if nodo.estadoI == 'I':
#            nodoInicial = nodo
#            nodosOrdenados.insert(0,nodoInicial)
#         else:
#             nodosOrdenados.append(nodo)

#     for nodo in nodosOrdenados:
#         print("la heuristica de", nodo.nombre, "es", nodo.heuristica)

#     solucionActual = nodosOrdenados[0] #definimos al primer nodo como solucion actual antes de comenzar a recorrer los demas nodos
#     #nodosNoExplorados = nodosOrdenados.copy() #se hace una copia para no alterar el orden de los nodos cargados
    
#     bandera = True

#     while bandera == True:
#         for nodoActual in nodosOrdenados:
#             if solucionActual == nodoActual:
#                 print("------------------------------------------------------------")
#                 print("Analizando nodo:", nodoActual.nombre, "con padre:", nodoActual.padre)
#                 recorridoMaxPendiente.append(nodoActual)
#                 if not existe_nodo(nodosExplorados, nodoActual.nombre):
#                     nodosExplorados.append(nodoActual)
#                     if nodoActual.estadoI == 'I':
#                         bandera = False
#                 if nodoActual.estadoF == 'F':
#                     solucionActual = nodoActual
#                     bandera = False
#                 else:
#                     if nodoActual.conexiones != []:
#                         for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
#                             nodosConectados = [] #defino un array para ir cargando la heuristica de los nodos que estan relacionados
#                             for nodoAux in nodosOrdenados: #recorro el array de nodos no explorados
#                                 if nodoAux.nombre == conexion.nombre: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
#                                     if not existe_nodo(nodosExplorados, nodoAux.nombre):
#                                         nodoAux.padre = nodoActual.nombre
#                                         nodosExplorados.append(nodoAux)
#                                         nodosConectados.append(nodoAux) #agrego el nodo al array de nodos conectados para evaluar despues si su heuristica es mejor que el de la solucion actual
#                             for nC in nodosConectados:
#                                 print(nodoActual.nombre, nC.nombre, nC.heuristica)
#                                 if nC.heuristica < solucionActual.heuristica:
#                                     solucionActual = nC
#                                     if solucionActual.estadoF == None:
#                                         solucionActual.minLoc = "ML"
#                                         bandera = False  
#                     else:
#                         print("el nodo:",nodoActual.nombre, "no posee hijos")
#                         solucionActual.minLoc = "ML"
#                         break

#     if solucionActual.minLoc == 'ML':
#         print("la solucion es un Minimo Local:", solucionActual.nombre)
#     else:
#         print("la solucion es:", solucionActual.nombre)

    
#     print("---------------------recorrido------------------------------")
#     for i in recorridoMaxPendiente:
#         print(i.heuristica, i.nombre)
#     print("------------------------------------------------------------")

#     for e in nodosExplorados:
#         print(e.nombre)

#     return recorridoMaxPendiente, nodosExplorados


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
                        if not existe_nodo(nodosExplorados, nodoAux.nombre):
                            nodoAux.padre = nodoActual.nombre
                            nodosExplorados.append(nodoAux)
                            nodosConectados.append(nodoAux)
            
            for nC in nodosConectados:
                print(nodoActual.nombre, nC.nombre, nC.heuristica)
                if nC.heuristica < solucionActual.heuristica:
                    solucionActual = nC
        
        if nodoActual == solucionActual:
            print("El nodo:", nodoActual.nombre, "no posee hijos o no hay mejor opción")
            solucionActual.minLoc = "ML"
            print("La solución es un Mínimo Local:", solucionActual.nombre)
            return recorridoMaxPendiente, nodosExplorados
        else:
            return calcularMaximaPendiente(nodos, solucionActual, solucionActual, recorridoMaxPendiente, nodosExplorados)