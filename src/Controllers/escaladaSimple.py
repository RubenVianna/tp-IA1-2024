# def exploracion(nodo, nodosNoExplorados):
    
#     nodosNoExploradosLocal = nodosNoExplorados.copy()
#     nodo.conexiones.sort(key=lambda nodo: nodo.nombre)
#     nodoActual = nodo
#     conexionesNoExploradas = [nodo for nodo in nodoActual.conexiones if nodo in nodosNoExplorados]
    
#     print('Comienza el algoritmo, nodoActual:',nodoActual.nombre,'y sus conexiones son: ')
#     for nodi in nodoActual.conexiones:
#         print(nodi.nombre) 

#     print('Y los nodos no explorados aun son:')
#     for nodito in nodosNoExploradosLocal:
#         print(nodito.nombre)

#     print('Por lo tanto se itera unicamente sobre los nodos: ')
#     for nodin in conexionesNoExploradas:
#         print(nodin.nombre)


# # ----------------------------------------------------------- CICLO RECURSIVO ----------------------------------------------------------------------

#     for nodoCandidato in conexionesNoExploradas:
#         print('Evaluando la conexion: ',nodoCandidato.nombre)
#         if nodoCandidato.estadoF == 'F':
#             resultado = 'Nodo objetivo alcanzado' + nodoCandidato.nombre
#             return resultado
        
#         print('El nodo:',nodoCandidato.nombre,' no es final. Sigue...')
#         print('El ultimo nodo de las conexiones es:',nodoActual.conexiones[-1].nombre )
#         if nodoCandidato.heuristica < nodoActual.heuristica:
#             print('Evaluacion de heuristica verdadera - El nodo: ',nodoCandidato.nombre, 'mejora la heuristica del NodoActual')
#             nodosNoExploradosLocal.remove(nodoCandidato)
#             nodoActual = nodoCandidato
#             resultado = exploracion(nodoActual, nodosNoExploradosLocal)
#             break
#         elif nodoCandidato == conexionesNoExploradas[-1]:
#             print('Se llego al final de las conexiones para el nodo',nodoActual.nombre)
#             resultado = 'Encontrado un minimo local, nodo:' + nodoActual.nombre
#             return resultado
#         nodosNoExploradosLocal.remove(nodoCandidato)

    
#     return resultado
            
# def escaladaSimple(nodos):
#     nodosNoExplorados = nodos.copy()
#     nodosNoExplorados.sort(key = lambda nodo: nodo.nombre)
    
#     for nodo in nodosNoExplorados:
#         if nodo.estadoI == 'I':
#             nodoActual = nodo
#             nodosNoExplorados.remove(nodo)

#     return (exploracion(nodoActual, nodosNoExplorados))
#-------------------------------------------------------------------------------------------------

def existe_nodo(lista, nombre):
    for nodo in lista:
        if nodo.nombre == nombre:
            return True
    return False

def calcularEscaladaSimple(nodos):
    nodosAlf = sorted(nodos, key=lambda x: x.nombre) #ordenamos alfabeticamente los nodos
    escaladaSimple = []
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
                escaladaSimple.append(nodoActual)
                if not existe_nodo(nodosExplorados, nodoActual.nombre):
                    nodosExplorados.append(nodoActual)
                    if nodoActual.estadoI == 'I':
                        bandera = False
                if nodoActual.estadoF == 'F':
                    solucionActual = nodoActual
                    bandera = False
                else:
                    if nodoActual.conexiones != []:
                        for conexion in nodoActual.conexiones: #recorro las conexiones del nodo actual para ver que con que nodos tengo que comparar la heuristica
                            for nodoAux in nodosNoExplorados: #recorro el array de nodos no explorados
                                if nodoAux.nombre == conexion.nombre: #controlo si el nodo del array de nodos no explorados es alguno los nodos conectados al nodo actual
                                    if not existe_nodo(nodosExplorados, nodoAux.nombre):
                                        nodoAux.padre = nodoActual.nombre
                                        nodosExplorados.append(nodoAux)
                                        print(nodoActual.nombre, nodoAux.nombre, nodoAux.heuristica)
                                        if nodoAux.heuristica < solucionActual.heuristica:
                                            print('la heuristica actual es:', solucionActual.heuristica)
                                            solucionActual = nodoAux
                                            if solucionActual.estadoF == None:
                                                solucionActual.minLoc = "ML" 
                            break
                    else:
                        print("el nodo:",nodoActual.nombre, "no posee hijos")
                        solucionActual.minLoc = "ML"
                        break

    if solucionActual.minLoc == 'ML':
        print("la solucion es un Minimo Local:", solucionActual.nombre)
    else:
        print("la solucion es:", solucionActual.nombre)

    
    print("---------------------recorrido------------------------------")
    for i in escaladaSimple:
        print(i.heuristica, i.nombre)
    print("------------------------------------------------------------")

    for e in nodosExplorados:
        print(e.nombre)

    return escaladaSimple, nodosExplorados