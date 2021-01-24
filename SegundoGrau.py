class EquacaoSegundoGrau(object):
    __A=None
    __B=None
    __C=None
   
#contrutor da classe
    def __init__(self):
            pass
   
#métodos get e set
    def setA(self,A):
        self.__A=A
    def getA(self):
        return self.__A
    def setB(self,B):
        self.__B=B
    def getB(self):
        return self.__B
    def setC(self,C):
        self.__C=C
    def getC(self):
        return self.__C
#método toString para visualizar os atributos do objeto
    def __str__(self):
        return self.__A,self.__B,self.__C