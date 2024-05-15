class Nodo:
    def __init__(self, nombre):
        self.nombre= nombre
        self.coordenada_x= None
        self.coordenada_y= None
        self.heuristica= None
        self.estadoI= None
        self.estadoF=None
        self.minLoc=None
        self.padre=None
        self.conexiones= []


    
