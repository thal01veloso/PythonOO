from SegundoGrau import *
from Resolucao import *

def main():
    eq = EquacaoSegundoGrau()
    eq.setA(1)
    eq.setB(2)
    eq.setC(1)
    rel = Resolucao()
    
    print(rel.calcularDelta(eq))
    print(rel.calcularRaizes(eq))
    print(rel.analiseDelta(eq))


    
main()