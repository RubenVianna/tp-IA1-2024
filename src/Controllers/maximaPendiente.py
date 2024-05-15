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
                nodosExplorados.append(nodoActual)
                if nodoActual.estadoF == 'F':
                    solucionActual = nodoActual
                    bandera = False
                else:
                    if nodoActual.conexiones != []:
                        for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
                            nodosConectados = [] #defino un array para ir cargando la heuristica de los nodos que estan relacionados
                            for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados
                                if nodoAux.nombre == conexion: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
                                    if not existe_nodo(nodosExplorados, nodoAux.nombre):
                                        nodoAux.padre = nodoActual.nombre
                                        nodosConectados.append(nodoAux) #agrego el nodo al array de nodos conectados para evaluar despues si su heuristica es mejor que el de la solucion actual
                            # if nodosConectados == []:
                            #     print("el nodo:",nodoActual.nombre, "no posee hijos no explorados")
                            #     bandera = False
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
   


   
    # print("nodos no explorados:")
    # for r in nodosNoExplorados:
    #     print(r.nombre)
    


############################################################################################ version mas estable
    # for nodoActual in nodosNoExplorados:
    #     nodosExplorados.append(nodoActual)
    #     nodosNoExplorados.remove(nodoActual)
    #     if nodoActual.estadoF == 'F':
    #         solucionActual = nodoActual
    #         recorridoMaxPendiente.append(nodoActual) #cargo el nodo final al array de nodos recorridos
    #         print('la solucion es:',solucionActual.nombre)
    #         break #finalizo la ejecucion ya que se encontro el nodo final
    #     else:
    #         if nodoActual.conexiones != []:
    #             for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
    #                 nodosConectados = [] #defino un array para ir cargando la heuristica de los nodos que estan relacionados
    #                 for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados
    #                     if nodoAux.nombre == conexion: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
    #                         nodosConectados.append(nodoAux) #agrego el nodo al array de nodos conectados para evaluar despues si su heuristica es mejor que el de la solucion actual
    #                         nodosExplorados.append(nodoAux) #agrego el nodo al array de nodos explorados
    #                         nodosNoExplorados.remove(nodoAux) #elimino el nodo del array de NO explorados
    #                 if nodosConectados == []:
    #                     print("el nodo:",nodoActual.nombre, "no posee hijos no Explorados")
    #                     break
    #                 for nC in nodosConectados:
    #                     print(nodoActual.nombre, nC.nombre, nC.heuristica)
    #         else:
    #             print("el nodo:",nodoActual.nombre, "no posee hijos")
    #             break
    #             # if solucionActual.heuristica == nodoActual.heuristica:
    #             #     break                   
    #         # nodosExplorados.append(nodoAux)
    #         # nodosNoExplorados.remove(nodoAux

    # print("nodos explorados:")
    # for i in nodosExplorados:
    #     print(i.heuristica, i.nombre)

    # print("nodos no explorados:")
    # for r in nodosNoExplorados:
    #     print(r.nombre)



    ##############################################

    # for nodoActual in nodosNoExplorados:
    #     nodosExplorados.append(nodoActual)
    #     nodosNoExplorados.remove(nodoActual)
    #     if nodoActual.estadoF == 'F':
    #         solucionActual = nodoActual
    #         recorridoMaxPendiente.append(nodoActual) #cargo el nodo final al array de nodos recorridos
    #         break #finalizo la ejecucion ya que se encontro el nodo final
    #     else:
    #         if nodoActual.conexiones != []:
    #             for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
    #                 nodosConectados = [] #defino un array para ir cargando la heuristica de los nodos que estan relacionados
    #                 for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados
    #                     if nodoAux.nombre == conexion: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
    #                         nodosConectados.append(nodoAux) 
    #                         nodosExplorados.append(nodoAux)
    #                         nodosNoExplorados.remove(nodoAux)
    #                 if nodosConectados == []:
    #                     print("el nodo:",nodoActual.nombre, "no posee hijos no Explorados")
    #                 for nC in nodosConectados:
    #                     print(nodoActual.nombre, nC.nombre, nC.heuristica)
    #         else:
    #             print("el nodo:",nodoActual.nombre, "no posee hijos")
    #             # if solucionActual.heuristica == nodoActual.heuristica:
    #             #     break                   
    #         # nodosExplorados.append(nodoAux)
    #         # nodosNoExplorados.remove(nodoAux)



    # print('el nodo final es:',solucionActual.nombre)

    # print("nodos explorados:")
    # for i in nodosExplorados:
    #     print(i.heuristica, i.nombre)

    # print("nodos no explorados:")
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