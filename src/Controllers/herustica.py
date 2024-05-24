import math

# Función para calcular la distancia en linea recta usando el teorema de pitagoras (distancia euclidiana) entre el nodo actual y el objetivo
def distanciaLineaRecta(nodoAct: int, nodoFin: int):
    heuristica = math.sqrt((nodoFin.coordenada_x - nodoAct.coordenada_x) ** 2 + (nodoFin.coordenada_y - nodoAct.coordenada_y) ** 2)
    
    return math.trunc(heuristica) 
# Función para calcular la distancia en linea recta entre 2 puntos usando la suma de la diferencia de las coordenadas entre el nodo actual y el objetivo
def distanciaManhattan(nodoAct: int, nodoFin: int):
    herustica = abs(nodoFin.coordenada_x - nodoAct.coordenada_x) + abs(nodoFin.coordenada_y - nodoAct.coordenada_y)
    
    return math.trunc(herustica)
