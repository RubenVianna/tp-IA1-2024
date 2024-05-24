def exploracion(nodo, nodosNoExplorados, caminoSolucion, nodosRecorridos): # FUNCION RECURSIVA
    
    nodosNoExploradosLocal = nodosNoExplorados.copy() # Copia local para evitar problemas con la recursividad.
    caminoSolucionLocal = caminoSolucion.copy()
    nodosRecorridosLocal = nodosRecorridos.copy()


    nodo.conexiones.sort(key=lambda nodo: nodo.nombre)
    nodoActual = nodo
    conexionesNoExploradas = [nodo for nodo in nodoActual.conexiones if nodo in nodosNoExplorados] 
    # Lista de las conexiones de cada nodo solo si estas ya no fueron exploradas.
    caminoSolucionLocal.append(nodoActual)

    
    if nodoActual.estadoF == 'F':
        return  caminoSolucionLocal, nodosNoExploradosLocal, nodosRecorridosLocal
        
# ----------------------------------------------------------- CICLO RECURSIVO ----------------------------------------------------------------------

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
    titulo = 'Inicio del algoritmo Escalada Simple'
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

    print(f"{'Cantidad de nodos en el espacio de busqueda:':50} {cantidadNodos}")
    print('--------------------------------------------------------------------')
    print(f"{'Cantidad de nodos explorados:':50} {len(nodosRecorridos)}")
    print('--------------------------------------------------------------------')
    print(f"{'Cantidad de nodos no explorados:':50} {len(nodosNoExplorados)}")
    print('--------------------------------------------------------------------')
    print(f"{'Nodo objetivo alcanzado:':50} {nodoObjetivoAlcanzado}")
    print('--------------------------------------------------------------------')
    print(f"{'Nombre del nodo objetivo:':50} {nodoObjetivo}")
    print('--------------------------------------------------------------------')
    print(f"{'Minimo local alcanzado:':50} {minimoLocalAlcanzado}")
    print('--------------------------------------------------------------------')

    if minimoLocalAlcanzado == 'SI':
        print(f"{'Nombre del minimo local:':50} {caminoSolucion[-1].nombre}")
        print('--------------------------------------------------------------------')

    print(f"{'Cantidad de iteraciones:':50} {len(caminoSolucion)}")
    print('--------------------------------------------------------------------')

    camino_texto = ' -> '.join(nodo.nombre for nodo in caminoSolucion)
    print(f"{'Camino solucion:':50} {camino_texto}")
    print('--------------------------------------------------------------------')

    print(f"\n{'Fin del algoritmo Escalada Simple'.center(80)}")


    return nodosRecorridos
