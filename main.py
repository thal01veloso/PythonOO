from SegundoGrau import *
from Resolucao import *

def main():
    eq = EquacaoSegundoGrau()
    eq.setA(1)
    eq.setB(2)
    eq.setC(1)
    rel = Resolucao()
    print(eq.__str__())
    print(rel.calcularDelta(eq))


    
main()