from SegundoGrau import *
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
class Resolucao():
    __delta = float()
    __x1 = float()
    __x2 = float()
    __eixo_x=float()
    __y=float()
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
    def gerarGrafico(self, EquacaoSegundoGrau):
        self.__eixo_x=np.linspace(-1,1,100)
        self.__y=(EquacaoSegundoGrau.getA()*(self.__eixo_x)**2)+EquacaoSegundoGrau.getB()*self.__eixo_x+EquacaoSegundoGrau.getC()
        p=plt.plot(self.__eixo_x,self.__y)
        return plt.show(p)