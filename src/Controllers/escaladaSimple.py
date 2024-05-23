import time

def exploracion(nodo, nodosNoExplorados, caminoSolucion, nodosRecorridos): # FUNCION RECURSIVA
    
    nodosNoExploradosLocal = nodosNoExplorados.copy() # Copia local para evitar problemas con la recursividad.
    caminoSolucionLocal = caminoSolucion.copy()
    nodosRecorridosLocal = nodosRecorridos.copy()


    nodo.conexiones.sort(key=lambda nodo: nodo.nombre)
    nodoActual = nodo
    conexionesNoExploradas = [nodo for nodo in nodoActual.conexiones if nodo in nodosNoExplorados] 
    # Lista de las conexiones de cada nodo solo si estas ya no fueron exploradas.
    caminoSolucionLocal.append(nodoActual)

# ----------------------------------------------------------- CICLO RECURSIVO ----------------------------------------------------------------------
    
    if nodoActual.estadoF == 'F':
        caminoSolucionLocal.append(nodoActual)
        nodosRecorridosLocal.append(nodoActual)

        return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal

    for nodoCandidato in conexionesNoExploradas:
        if nodoCandidato.estadoF == 'F':
            caminoSolucionLocal.append(nodoCandidato)
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodoCandidato.padre = nodoActual.nombre
            nodosRecorridosLocal.append(nodoCandidato)

            return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal
        
        if nodoCandidato.heuristica < nodoActual.heuristica:
            nodoCandidato.padre = nodoActual.nombre
            nodosRecorridosLocal.append(nodoCandidato)
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodoActual = nodoCandidato

            return exploracion(nodoActual, nodosNoExploradosLocal, caminoSolucionLocal, nodosRecorridosLocal)
        
        elif nodoCandidato == conexionesNoExploradas[-1]:
            nodosNoExploradosLocal.remove(nodoCandidato)
            nodoActual.minLoc = 'ML'
            nodoCandidato.padre = nodoActual.nombre
            nodosRecorridosLocal.append(nodoCandidato)
            break   
        
        nodoCandidato.padre = nodoActual.nombre
        nodosRecorridosLocal.append(nodoCandidato)
        nodosNoExploradosLocal.remove(nodoCandidato)
    
    return caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal #Return de la funcion exploracion
                   
def calcularEscaladaSimple(nodos):
    print('                           Inicio del algoritmo Escalada Simple                           ')
    print('')

    tiempoInicial = time.time()
    
    nodosNoExplorados = nodos.copy()
    cantidadNodos = len(nodos)
    nodosNoExplorados.sort(key = lambda nodo: nodo.nombre)
    caminoSolucion = []

    for nodo in nodosNoExplorados:
        if nodo.estadoI == 'I':
            nodoActual = nodo
            nodosNoExplorados.remove(nodo)
    nodosRecorridos = [nodoActual]
    caminoSolucion, nodosNoExplorados, nodosRecorridos = exploracion(nodoActual, nodosNoExplorados, [], nodosRecorridos)
    tiempoFinal = time.time()
    tiempoTotal = tiempoFinal - tiempoInicial

    if caminoSolucion[-1].estadoF == 'F':
        nodoObjetivoAlcanzado = 'SI'
        minimoLocalAlcanzado = 'NO'
    else:
        nodoObjetivoAlcanzado = 'NO'
        minimoLocalAlcanzado = 'SI'

    print('Cantidad de nodos en el espacio de busqueda: ',cantidadNodos)
    print('Cantidad de nodos explorados:                ',len(nodosRecorridos))
    print('Cantidad de nodos no explorados:             ',len(nodosNoExplorados))
    print('Nodo objetivo alcanzado:                     ',nodoObjetivoAlcanzado)
    if nodoObjetivoAlcanzado == 'SI':
        print('Nombre del nodo objetivo:                    ',caminoSolucion[-1].nombre)
    print('Minimo local alcanzado:                      ',minimoLocalAlcanzado)
    if minimoLocalAlcanzado == 'SI':
        print('Nombre del minimo local:                     ',caminoSolucion[-1].nombre)
    print('Cantidad de iteraciones:                     ',len(caminoSolucion))
    print('Camino solucion:                             ', end = ' ')
    for nodo in caminoSolucion:
        print(nodo.nombre, end = ' ')
    print() # Salto de linea. 
    print('Tiempo total de ejecucion:                   ', tiempoTotal)

    print('')
    print('                           Fin del algoritmo Escalada Simple                           ')

    return caminoSolucion, nodosNoExplorados, nodosRecorridos
