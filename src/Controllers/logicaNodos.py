import string
import random
from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Models.nodo import Nodo

def definirNodos(cantNodos):
    cantNodos = int(cantNodos)
    nodos = []
    nombres = string.ascii_uppercase  # Obtener las letras del alfabeto en mayúsuclas
    i=0
    asignadoÑ = False
    while i < cantNodos:
        if i == 14 and not asignadoÑ:
            nombre = 'Ñ'
            asignadoÑ = True
        elif asignadoÑ:
            nombre = nombres[i-1 % len(nombres)]
        else:
            nombre = nombres[i % len(nombres)]
        i =i+1  # Usar módulo para ciclar a través del alfabeto

        nodo = Nodo(nombre)
        nodos.append(nodo)

    return nodos

def generarAleatorios(cantNodos):
    cantNodos = int(cantNodos)
    if cantNodos > 1:
        nodos = definirNodos(cantNodos)

        ini = random.randint(1,cantNodos-1)
        fin = random.randint(1,cantNodos-1)
        nodos[ini].estadoI = 'I'
        nodos[fin].estadoF = 'F'

        heuristica = random.randint(1,2)

        for nodo in nodos:
            nodo.coordenada_x = random.randint(-20,20)
            nodo.coordenada_y = random.randint(-20,20)

        for nodo in nodos:
            if heuristica == 1:
                nodo.heuristica =distanciaManhattan(nodo, nodos[fin])
            else:
                nodo.heuristica = distanciaLineaRecta(nodo,nodos[fin])
        
        # Generar conexiones bidireccionales aleatorias entre los nodos
        for nodo in nodos:
            posibles_conexiones = [n for n in nodos if n != nodo and n not in nodo.conexiones]  # Evitar autoconexiones y duplicadas
            num_conexiones = min(random.randint(1, 3), len(posibles_conexiones))  # Asegurarse de no exceder los posibles
            conexiones = random.sample(posibles_conexiones, num_conexiones)
            for conexion in conexiones:
                if conexion not in nodo.conexiones:
                    nodo.conexiones.append(conexion)
                    if nodo not in conexion.conexiones:  # Asegurar que la conexión inversa esté presente
                        conexion.conexiones.append(nodo)
                if nodo not in conexion.conexiones:
                    conexion.conexiones.append(nodo)
                    if conexion not in nodo.conexiones:  # Asegurar que la conexión inversa esté presente
                        nodo.conexiones.append(conexion)
    else:
        nodos = []
        nodo= Nodo('A')
        nodo.estadoI = 'I'
        nodo.estadoF = 'F'
        nodo.coordenada_x = random.randint(-20,20)
        nodo.coordenada_y = random.randint(-20,20)
        nodo.heuristica = 0
        nodos.append(nodo)

    return nodos


