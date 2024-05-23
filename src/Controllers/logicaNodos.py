import string
import random
from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Models.nodo import Nodo

def definirNodos(cantNodos):
    cantNodos = int(cantNodos)
    nodos = []
    nombres = string.ascii_uppercase  # Obtener las letras del alfabeto en mayúsuclas
    for i in range(cantNodos):
        nombre = nombres[i % len(nombres)]  # Usar módulo para ciclar a través del alfabeto
        nodo = Nodo(nombre)
        nodos.append(nodo)

    return nodos

def generarAleatorios(cantNodos):
    cantNodos = int(cantNodos)
    nodos = definirNodos(cantNodos)

    ini = random.randint(1,cantNodos-1)
    fin = random.randint(1,cantNodos-1)
    nodos[ini].estadoI = 'I'
    nodos[fin].estadoF = 'F'

    heuristica = random.randint(1,2)

    for nodo in nodos:
        nodo.coordenada_x = random.randint(-10,20)
        nodo.coordenada_y = random.randint(-10,20)

    for nodo in nodos:
        if heuristica == 1:
            nodo.heuristica =distanciaManhattan(nodo, nodos[fin])
        else:
            nodo.heuristica = distanciaLineaRecta(nodo,nodos[fin])
    
    # Generar conexiones bidireccionales aleatorias entre los nodos
    for nodo in nodos:
        posibles_conexiones = [n for n in nodos if n != nodo and n not in nodo.conexiones]  # Evitar autoconexiones y duplicadas
        num_conexiones = min(random.randint(1,3), len(posibles_conexiones))  # Asegurarse de no exceder los posibles
        conexiones = random.sample(posibles_conexiones, num_conexiones)
        for conexion in conexiones:
            if conexion not in nodo.conexiones:
                nodo.conexiones.append(conexion)
            if nodo not in conexion.conexiones:
                conexion.conexiones.append(nodo)

    return nodos


