def exploracion(nodo, nodosNoExplorados, caminoSolucion, nodosRecorridos): # FUNCION RECURSIVA
    
    nodosNoExploradosLocal = nodosNoExplorados.copy() # Copia local para evitar problemas con la recursividad.
    caminoSolucionLocal = caminoSolucion.copy()
    nodosRecorridosLocal = nodosRecorridos.copy()


    nodo.conexiones.sort(key=lambda nodo: nodo.nombre)
    nodoActual = nodo
    conexionesNoExploradas = [nodo for nodo in nodoActual.conexiones if nodo in nodosNoExplorados] 
    # Lista de las conexiones de cada nodo solo si estas ya no fueron exploradas.
    
    caminoSolucionLocal.append(nodoActual)
    print('[---------------------------- FUNCION RECURSIVA ----------------------------] ')

    print('nodoActual:',nodoActual.nombre,'y sus conexiones son: ', end = ' ')
    for nodi in nodoActual.conexiones:
        print(nodi.nombre, end = ', ')
    print() # Salto de linea. 

    print('Y los nodos no explorados aun son: ', end = ' ')
    for nodito in nodosNoExploradosLocal:
        print(nodito.nombre, end = ',')
    print() # Salto de linea. 

    print('Por lo tanto se itera unicamente sobre los nodos: ', end = ' ')
    for nodin in conexionesNoExploradas:
        print(nodin.nombre, end = ', ')

    print('El camino solucion hasta ahora es: ', end = ' ')
    for nodin in caminoSolucionLocal:
        print(nodo.nombre, end = ', ')

# ----------------------------------------------------------- CICLO RECURSIVO ----------------------------------------------------------------------
    
    if nodoActual.estadoF == 'F':
        print('Nodo objetivo alcanzado: ' + nodoActual.nombre)
        caminoSolucionLocal.append(nodoActual)
        nodosRecorridosLocal.append(nodoActual)

        return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal

    for nodoCandidato in conexionesNoExploradas:
        print('Evaluando la conexion: ',nodoCandidato.nombre)
        if nodoCandidato.estadoF == 'F':
            print('Nodo objetivo alcanzado: ' + nodoCandidato.nombre)
            caminoSolucionLocal.append(nodoCandidato)
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodoCandidato.padre = nodoActual.nombre
            nodosRecorridosLocal.append(nodoCandidato)

            return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal
        
        print('El nodo:',nodoCandidato.nombre,' no es final. Sigue...')
        print('El ultimo nodo de las conexiones es: ', nodoActual.conexiones[-1].nombre)
        
        nodoCandidato.padre = nodoActual.nombre
        nodosRecorridosLocal.append(nodoCandidato)
        if nodoCandidato.heuristica < nodoActual.heuristica:
            print('Evaluacion de heuristica verdadera - El nodo: ',nodoCandidato.nombre, 'mejora la heuristica del nodo ', nodoActual.nombre)
            nodoActual = nodoCandidato
            nodosNoExploradosLocal.remove(nodoCandidato)

            return exploracion(nodoActual, nodosNoExploradosLocal, caminoSolucionLocal, nodosRecorridosLocal)
        
        elif nodoCandidato == conexionesNoExploradas[-1]:
            print('Se llego al final de las conexiones para el nodo ',nodoActual.nombre)
            print('Encontrado un minimo local, nodo:' + nodoActual.nombre)
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodoActual.minLoc = 'ML'
            nodoCandidato.padre = nodoActual.nombre
            nodosRecorridosLocal.append(nodoCandidato)
            'Encontrado un minimo local, nodo:' + nodoActual.nombre
            break   
        
        nodosNoExploradosLocal.remove(nodoCandidato)
    
    return caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal #Return de la funcion exploracion
                   
def calcularEscaladaSimple(nodos):
    nodosNoExplorados = nodos.copy()
    nodosNoExplorados.sort(key = lambda nodo: nodo.nombre)
    caminoSolucion = []

    for nodo in nodosNoExplorados:
        if nodo.estadoI == 'I':
            nodoActual = nodo
            nodosNoExplorados.remove(nodo)
    nodosRecorridos = [nodoActual]
    print('------------------------ Inicio de la funcion escaladaSimple -------------------------')

    caminoSolucion, nodosNoExplorados, nodosRecorridos = exploracion(nodoActual, nodosNoExplorados, [], nodosRecorridos)

    print('------------------------ Fin de la funcion escaladaSimple -------------------------')
    
    return caminoSolucion, nodosNoExplorados, nodosRecorridos
