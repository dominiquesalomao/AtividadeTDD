import numpy as np 
class Diagonal:

    def DiagonalMethod(testes):
        cont = 1
        try:
            for r in testes:
                diagonalx = np.asarray(r)
                diagonaly = np.fliplr(r)
                diagonalx = np.trace(diagonalx)
                diagonaly = np.trace(diagonaly)
                sub = diagonalx - diagonaly
                sub = abs(sub)
                print("O valor absoluto do teste "+str(cont)+" é: "+str(sub))
                cont = cont + 1;
            return True
        except:
            return False