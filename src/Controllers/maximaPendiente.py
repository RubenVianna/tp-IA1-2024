def existe_nodo(lista, nombre):
    for nodo in lista:
        if nodo.nombre == nombre:
            return True
    return False

def calcularMaximaPendiente(nodos):
    nodosAlf = sorted(nodos, key=lambda x: x.nombre) #ordenamos alfabeticamente los nodos
    recorridoMaxPendiente = []
    nodosExplorados = []
    nodosOrdenados = []

    # se ordena el array de nodos recibido para comenzar a recorrer por el nodo Inicial
    for nodo in nodosAlf:
        if nodo.estadoI == 'I':
           nodoInicial = nodo
           nodosOrdenados.insert(0,nodoInicial)
        else:
            nodosOrdenados.append(nodo)

    for nodo in nodosOrdenados:
        print("la heuristica de", nodo.nombre, "es", nodo.heuristica)

    solucionActual = nodosOrdenados[0] #definimos al primer nodo como solucion actual antes de comenzar a recorrer los demas nodos
    nodosNoExplorados = nodosOrdenados.copy() #se hace una copia para no alterar el orden de los nodos cargados


    bandera = True
    
    while bandera == True:
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
                    if nodoActual.conexiones != []:
                        for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
                            nodosConectados = [] #defino un array para ir cargando la heuristica de los nodos que estan relacionados
                            for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados
                                if nodoAux.nombre == conexion.nombre: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
                                    if not existe_nodo(nodosExplorados, nodoAux.nombre):
                                        nodoAux.padre = nodoActual.nombre
                                        nodosExplorados.append(nodoAux)
                                        nodosConectados.append(nodoAux) #agrego el nodo al array de nodos conectados para evaluar despues si su heuristica es mejor que el de la solucion actual
                            for nC in nodosConectados:
                                print(nodoActual.nombre, nC.nombre, nC.heuristica)
                                if nC.heuristica < solucionActual.heuristica:
                                    solucionActual = nC
                                    if solucionActual.estadoF == None:
                                        solucionActual.minLoc = "ML"
                                        bandera = False  
                    else:
                        print("el nodo:",nodoActual.nombre, "no posee hijos")
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



#-----------------------------------------------Version con conexiones solo con nombre --------------------------------------------


    # bandera = True
    
    # while bandera == True:
    #     for nodoActual in nodosOrdenados:
    #         if solucionActual == nodoActual:
    #             print("------------------------------------------------------------")
    #             print("Analizando nodo:", nodoActual.nombre, "con padre:", nodoActual.padre)
    #             recorridoMaxPendiente.append(nodoActual)
    #             if not existe_nodo(nodosExplorados, nodoActual.nombre):
    #                 nodosExplorados.append(nodoActual)
    #             if nodoActual.estadoF == 'F':
    #                 solucionActual = nodoActual
    #                 bandera = False
    #             else:
    #                 if nodoActual.conexiones != []:
    #                     for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
    #                         nodosConectados = [] #defino un array para ir cargando la heuristica de los nodos que estan relacionados
    #                         for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados
    #                             if nodoAux.nombre == conexion: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
    #                                 if not existe_nodo(nodosExplorados, nodoAux.nombre):
    #                                     nodoAux.padre = nodoActual.nombre
    #                                     nodosExplorados.append(nodoAux)
    #                                     nodosConectados.append(nodoAux) #agrego el nodo al array de nodos conectados para evaluar despues si su heuristica es mejor que el de la solucion actual
    #                         for nC in nodosConectados:
    #                             print(nodoActual.nombre, nC.nombre, nC.heuristica)
    #                             if nC.heuristica < solucionActual.heuristica:
    #                                 solucionActual = nC
    #                                 if solucionActual.estadoF == None:
    #                                     solucionActual.minLoc = "ML"
    #                                     bandera = False  
    #                 else:
    #                     print("el nodo:",nodoActual.nombre, "no posee hijos")
    #                     solucionActual.minLoc = "ML"
    #                     break

    # if solucionActual.minLoc == 'ML':
    #     print("la solucion es un Minimo Local:", solucionActual.nombre)
    # else:
    #     print("la solucion es:", solucionActual.nombre)

    
    # print("---------------------recorrido------------------------------")
    # for i in recorridoMaxPendiente:
    #     print(i.heuristica, i.nombre)
    # print("------------------------------------------------------------")

    # for e in nodosExplorados:
    #     print(e.nombre)