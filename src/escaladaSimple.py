
class nodo:
    esInicial = ''
    esFinal = ''
    conectaCon = []
    peso = 0

    def setPeso(self,pesaje):
        self.peso = pesaje
    
    def setConexiones(self, conexiones):
        self.conectaCon = conexiones

    def setEsInicial(self,bool):
        self.esInicial = bool

    def setEsFinal(self,bool):
        self.setEsFinal = bool



nodos = [['A',40],['B',50],['C',20],['D',15],['E',25],['F',10]]


