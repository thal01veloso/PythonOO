class EquacaoSegundoGrau():
    __A=float()
    __B=float()
    __C=float()
   
#contrutor da classe
    def __init__(self,A,B,C):
        self.__A = A
        self.__B = B
        self.__C = C
    
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