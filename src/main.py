import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from Controllers.herustica import *
from Controllers.maximaPendiente import calcularMaximaPendiente
from Controllers.escaladaSimple import calcularEscaladaSimple
from Controllers.graficos import *
from Views.vistaInicial import *
from Models.nodo import Nodo

# #ejemplo de como usar la funcion para distancia en linea recta
# nodo1 = Nodo('A')
# nodo1.coordenada_x=-1
# nodo1.coordenada_y=1
# nodo2 = Nodo('B')
# nodo2.coordenada_x=-2
# nodo2.coordenada_y=-2
# nodo3 = Nodo('C')
# nodo3.coordenada_x=-3
# nodo3.coordenada_y=-5
# nodo4 = Nodo('D')
# nodo4.coordenada_x=4
# nodo4.coordenada_y=4
# nodo5 = Nodo('E')
# nodo5.coordenada_x=-5
# nodo5.coordenada_y=5
# nodo6 = Nodo('F')
# nodo6.coordenada_x=6
# nodo6.coordenada_y=6
# nodo7 = Nodo('G')
# nodo7.coordenada_x=-7
# nodo7.coordenada_y=-7

# cantNodos = 7

# #definimos al nodo 5 como nodo final
# nodo7.estadoF = 'F'
# nodo1.estadoI = 'I'

# #logica
# nodos= []

# nodos+=[nodo6,nodo1,nodo5,nodo3,nodo4,nodo2,nodo7]

# # calculo de heuristica
# i= 0
# while i < cantNodos:
#     heuristica = distanciaManhattan(nodos[i],nodo7)
#     nodos[i].heuristica = heuristica
#     i= i+ 1


# #relaciones nodo A (B,C)
# nodo1.conexiones.append(nodo2)
# nodo1.conexiones.append(nodo3)

# #relaciones nodo B (A,C,D)
# nodo2.conexiones.append(nodo1)
# nodo2.conexiones.append(nodo4)
# nodo2.conexiones.append(nodo3)

# #relaciones nodo C (A,B,D,E,G)
# nodo3.conexiones.append(nodo1)
# nodo3.conexiones.append(nodo4)
# nodo3.conexiones.append(nodo5)
# nodo3.conexiones.append(nodo2)
# nodo3.conexiones.append(nodo7)

# #relaciones nodo D (B,E)
# nodo4.conexiones.append(nodo2)
# nodo4.conexiones.append(nodo5)

# #relaciones nodo E (C,D,F)
# nodo5.conexiones.append(nodo3)
# nodo5.conexiones.append(nodo4)
# nodo5.conexiones.append(nodo6)

# #relaciones nodo F (E)
# nodo6.conexiones.append(nodo5)

# #graficarGrafo(nodos)

# recorridoMaximaPendiente, nodosExploradosMP = calcularMaximaPendiente(nodos)

# # print("-------------------------------------------")

# #escaladaSimple , nodosExploradosES = calcularEscaladaSimple(nodos)

# print('Maxima pendiente')
# for s in recorridoMaximaPendiente:
#     print("Paso: ",s.nombre, "Heuristica: ", s.heuristica, 'con padre:', s.padre, "es un minimo local:", s.minLoc)

# # print('Escalada Simple')
# # for e in escaladaSimple:
# #     print("Paso: ",e.nombre, "Heuristica: ", e.heuristica, 'con padre:', e.padre, "es un minimo local:", e.minLoc)

# graficaryMostrarArbol(nodosExploradosMP, 'Arbol Maxima Pendiente', mostrarResultados=True)

# #graficarPasoAPaso(nodosExploradosES,'Arbol Escalada Simple')

# graficarPasoAPaso(nodosExploradosMP,'Arbol Maxima Pendiente')

#------------------ ARBOL-------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaPrincipal = Inicio()
    ventanaPrincipal.show()
    sys.exit(app.exec_())