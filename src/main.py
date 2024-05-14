from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Models.nodo import Nodo

#ejemplo de como usar la funcion para distancia en linea recta
nodo1 = Nodo('A')
nodo1.coordenada_x=1
nodo1.coordenada_y=2
nodo2 = Nodo('B')
nodo2.coordenada_x=4
nodo2.coordenada_y=6
nodo3 = Nodo('C')
nodo3.coordenada_x=8
nodo3.coordenada_y=1

#logica 
nodo2.conexiones.append(nodo1.nombre)
nodo2.conexiones.append(nodo3.nombre)

print(nodo2.conexiones)

heuristica = distanciaManhattan(nodo1,nodo2)


print("El nodo 1 es:" , nodo1.nombre , "con coordenadas:" , nodo1.coordenada_x , "y", nodo1.coordenada_y, "su heuristica es:", heuristica)
print("El nodo 2 es:", nodo2.nombre)