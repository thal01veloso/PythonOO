from SegundoGrau import *
from math import sqrt
class Resolucao():
    __delta = float()
    __x1 = float()
    __x2 = float()
    def calcularDelta(self,EquacaoSegundoGrau):
        
        self.__delta = (EquacaoSegundoGrau.getB()**2)-4*EquacaoSegundoGrau.getA()*EquacaoSegundoGrau.getC()
        return "Delta = {}".format(self.__delta)
    def calcularRaizes(self, EquacaoSegundoGrau):
        self.__x1 = (- EquacaoSegundoGrau.getB()+sqrt(self.__delta))/2*EquacaoSegundoGrau.getA()
        self.__x2 = (- EquacaoSegundoGrau.getB()-sqrt(self.__delta))/2*EquacaoSegundoGrau.getA()
        return "Raizes da equação são: {} {}".format(self.__x1,self.__x2)
    def analiseDelta(self, EquacaoSegundoGrau):
        if(self.__delta==0):
            return "As raizes são iguais(duplas)"
        elif(self.__delta<0):
            return "As raizes são Complexas"
        else:
            return "Possui duas raizes distintas"