from SegundoGrau import *
class Resolucao():
    def calcularDelta(self,EquacaoSegundoGrau):
        
        delta = (EquacaoSegundoGrau.getB()**2)-4*EquacaoSegundoGrau.getA()*EquacaoSegundoGrau.getC()
        return delta
