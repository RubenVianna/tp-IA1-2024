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

    # for nodo in nodosOrdenados:
    #     print("la heuristica de", nodo.nombre, "es", nodo.heuristica)

    solucionActual = nodosOrdenados[0] #definimos al primer nodo como solucion actual antes de comenzar a recorrer los demas nodos
    nodosNoExplorados = nodosOrdenados.copy() #se hace una copia para no alterar el orden de los nodos cargados
    #nodosExplorados.append(nodosNoExplorados.pop(0)) #se va a ir eliminando del array de no explorados y se va ir cargando el array de nodos explorados, para luego hacer el recorrido en el arbol

    for nodoActual in nodosNoExplorados:
        nodosExplorados.append(nodoActual)
        nodosNoExplorados.remove(nodoActual)
        if nodoActual.estadoF == 'F':
            solucionActual = nodoActual
            recorridoMaxPendiente.append(nodoActual) #cargo el nodo final al array de nodos recorridos
            break #finalizo la ejecucion ya que se encontro el nodo final
        else:
            for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
                print("nodo",nodoActual.nombre, "conexion", conexion)
                break
                for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados 
                     if nodoAux.nombre == conexion: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
                         if nodoAux.heuristica < solucionActual.heuristica: #Comparo si alguno de los nuevos nodos tiene mejor heuristica que la solución actual
                             solucionActual = nodoAux #si es el caso, defino a ese nuevo nodo como solucion actual
                if solucionActual.heuristica == nodoActual.heuristica:
                    break                   
            # nodosExplorados.append(nodoAux)
            # nodosNoExplorados.remove(nodoAux)



    # print('el nodo final es:',solucionActual.nombre)

    # for i in nodosExplorados:
    #     print(i.heuristica, i.nombre)

    # for r in nodosNoExplorados:
    #     print(r.nombre)

    # for re in recorridoMaxPendiente:
    #     print ("el recorrido es:", re.nombre)
         









    # def maxima_pendiente_con_historial(nodos, distancias, conexiones):    
    #         solucion_actual = nodosOrdenados[0]  # Comenzamos desde el primer nodo
    #         historial = [solucion_actual]  # Inicializamos el historial con el primer nodo
    #         while True:
    #             vecinos = [(nodo, distancias[nodo]) for nodo in conexiones[solucion_actual] if nodo not in historial]
    #             if not vecinos:
    #                 return historial  # Si el nodo actual no tiene vecinos no visitados, devolvemos el historial
    #             mejor_vecino = max(vecinos, key=lambda x: x[1])  # Encontrar el vecino con la mayor heurística
    #             if mejor_vecino[1] <= distancias[solucion_actual]:
    #                 return historial  # Si no hay mejora, devolvemos el historial actual
    #             solucion_actual = mejor_vecino[0]  # Actualizamos la solución actual con el mejor vecino
    #             historial.append(solucion_actual)  # Agregamos el nodo actual al historial