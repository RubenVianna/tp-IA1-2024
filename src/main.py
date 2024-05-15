from Controllers.herustica import distanciaLineaRecta
from Controllers.herustica import distanciaManhattan
from Controllers.maximaPendiente import calcularMaximaPendiente
from Models.nodo import Nodo

#ejemplo de como usar la funcion para distancia en linea recta
nodo1 = Nodo('A')
nodo1.coordenada_x=1
nodo1.coordenada_y=2
nodo2 = Nodo('B')
nodo2.coordenada_x=8
nodo2.coordenada_y=1
nodo3 = Nodo('C')
nodo3.coordenada_x=4
nodo3.coordenada_y=6
nodo4 = Nodo('D')
nodo4.coordenada_x=10
nodo4.coordenada_y=2
nodo5 = Nodo('E')
nodo5.coordenada_x=12
nodo5.coordenada_y=10
nodo6 = Nodo('F')
nodo6.coordenada_x=15
nodo6.coordenada_y=8

cantNodos = 6

#definimos al nodo 5 como nodo final
nodo5.estadoF = 'F'
nodo1.estadoI = 'I'

#logica

#relaciones nodo A (B,C)
nodo1.conexiones.append(nodo2.nombre)
nodo1.conexiones.append(nodo3.nombre)

#relaciones nodo B (A,D)
nodo2.conexiones.append(nodo1.nombre)
nodo2.conexiones.append(nodo4.nombre)

#relaciones nodo C (A,D,E)
nodo3.conexiones.append(nodo1.nombre)
nodo3.conexiones.append(nodo4.nombre)
nodo3.conexiones.append(nodo5.nombre)

#relaciones nodo D (B,E)
nodo4.conexiones.append(nodo2.nombre)
nodo4.conexiones.append(nodo5.nombre)

#relaciones nodo E (C,D)
nodo5.conexiones.append(nodo3.nombre)
nodo5.conexiones.append(nodo4.nombre)


nodos= []

nodos+=[nodo6,nodo1,nodo5,nodo3,nodo4,nodo2]

# calculo de heuristica
i= 0
while i < cantNodos:
    heuristica = distanciaManhattan(nodos[i],nodo6)
    nodos[i].heuristica = heuristica
    i= i+ 1

calcularMaximaPendiente(nodos)

# print(nodos)
# #array de nodos


# print(nodo2.conexiones)





# print("El nodo 1 es:" , nodo1.nombre , "con coordenadas:" , nodo1.coordenada_x , "y", nodo1.coordenada_y, "su heuristica es:", heuristica)
# print("El nodo 2 es:", nodo2.nombre, "con coordenadas:" , nodo2.coordenada_x , "y", nodo2.coordenada_y, "su heuristica es:", heuristica2)