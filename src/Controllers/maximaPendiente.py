
def exploracion(nodo, nodosNoExplorados, caminoSolucion, nodosRecorridos): # FUNCION RECURSIVA
    
    nodosNoExploradosLocal = nodosNoExplorados.copy() # Copia local para evitar problemas con la recursividad.
    caminoSolucionLocal = caminoSolucion.copy()
    nodosRecorridosLocal = nodosRecorridos.copy()

    nodo.conexiones.sort(key=lambda nodo: nodo.nombre)
    nodoActual = nodo
    conexionesNoExploradas = [nodo for nodo in nodoActual.conexiones if nodo in nodosNoExplorados] 
    caminoSolucionLocal.append(nodoActual)
    heuristicaMejorada = 0
   # print('Inicio de la exploracion, evaluando el nodo:',nodoActual.nombre)
    
    if nodoActual.estadoF == 'F':
       # print('El nodo',nodoActual.nombre,' no es final...')
        return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal
    
   # print('Las conexiones no exploradas del nodo',nodoActual.nombre,'son:', end = ' ')
    # for nodo in conexionesNoExploradas:
    #     print(nodo.nombre, end = ' ')

    for nodo in conexionesNoExploradas:
        nodo.padre = nodoActual.nombre


# ----------------------------------------------------------- CICLO RECURSIVO ----------------------------------------------------------------------

    for nodoCandidato in conexionesNoExploradas:
       # print('Evaluando la conexion:',nodoCandidato.nombre)
        if nodoCandidato.estadoF == 'F':
            caminoSolucionLocal.append(nodoCandidato)
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodosRecorridosLocal.append(nodoCandidato)


            return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal
        
        if nodoCandidato.heuristica < nodoActual.heuristica:
           # print('El nodo candidato',nodoCandidato.nombre,'mejora la heuristica del nodo actual.')
          #  print('La heuristica:',nodoCandidato.heuristica,'del nodo',nodoCandidato.nombre,'es mejor que la heuristica',nodoActual.heuristica,'del nodo actual',nodoActual.nombre)
            nodosRecorridosLocal.append(nodoCandidato)
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodoActual = nodoCandidato
         #   print('El nodo actual ahora es:',nodoActual.nombre)
            heuristicaMejorada = 1

        else:
            nodosRecorridosLocal.append(nodoCandidato)
            nodosNoExploradosLocal.remove(nodoCandidato)
        
        if nodoCandidato == conexionesNoExploradas[-1] and heuristicaMejorada == 1:
           # print('Se ha llegado al final de las conexiones sin encontrarse el nodo objetivo aun.')
            return exploracion(nodoActual, nodosNoExploradosLocal, caminoSolucionLocal, nodosRecorridosLocal)
        
    # print()
    # print('Fin del algoritmo de exploracion')
    # print()
    return caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal #Return de la funcion exploracion
                   
def calcularMaximaPendiente(nodos):
    titulo = 'Inicio del algoritmo Máxima Pendiente'
    print(f"{titulo.center(80)}\n")
    print('')
    
    nodosNoExplorados = nodos.copy()
    cantidadNodos = len(nodos)
    nodosNoExplorados.sort(key = lambda nodo: nodo.nombre)
    caminoSolucion = []

    for nodo in nodos:
        if nodo.estadoF == 'F':
            nodoObjetivo= nodo.nombre

    for nodo in nodosNoExplorados:
        if nodo.estadoI == 'I':
            nodoActual = nodo
            nodosNoExplorados.remove(nodo)
    nodosRecorridos = [nodoActual]
    caminoSolucion, nodosNoExplorados, nodosRecorridos = exploracion(nodoActual, nodosNoExplorados, [], nodosRecorridos)

    if caminoSolucion[-1].estadoF == 'F':
        nodoObjetivoAlcanzado = 'SI'
        minimoLocalAlcanzado = 'NO'
    else:
        nodoObjetivoAlcanzado = 'NO'
        minimoLocalAlcanzado = 'SI'
        caminoSolucion[-1].minLoc = 'ML'

    print('Cantidad de nodos en el espacio de busqueda:    ',cantidadNodos)
    print('--------------------------------------------------------------------')
    print('Cantidad de nodos explorados:                ',len(nodosRecorridos))
    print('--------------------------------------------------------------------')
    print('Cantidad de nodos no explorados:             ',len(nodosNoExplorados))
    print('--------------------------------------------------------------------')
    print('Nodo objetivo alcanzado:                     ',nodoObjetivoAlcanzado)
    print('--------------------------------------------------------------------')
    print('Nombre del nodo objetivo:                    ',nodoObjetivo)
    print('--------------------------------------------------------------------')
    print('Minimo local alcanzado:                      ',minimoLocalAlcanzado)
    print('--------------------------------------------------------------------')
    if minimoLocalAlcanzado == 'SI':
        print('Nombre del minimo local:                     ',caminoSolucion[-1].nombre)
        print('--------------------------------------------------------------------')
    print('Cantidad de iteraciones:                     ',len(caminoSolucion))
    print('--------------------------------------------------------------------')

    camino_texto = ' -> '.join(nodo.nombre for nodo in caminoSolucion)
    print(f"{'Camino solucion:':45} {camino_texto}")
    print('--------------------------------------------------------------------')

    print('')
    print('                           Fin del algoritmo Maxima Pendiente                           ')

    return nodosRecorridos