import string
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
