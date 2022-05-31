#Main para rodar os testes de Diagonal
from Diagonal import Diagonal

class MainSomaArray:
    try:
        testes = [
        [[55, 25, 15],
        [30, 44, 2], 
        [11, 45, 77]],

        [[11,2,4],
        [4,5,6],
        [10,8,-12]],

        [[0, 2], 
        [1, 1], 
        [2, 0]], 

        [[2,3,4], 
        [4,3,3], 
        [3,3,4]]]
        
        x = Diagonal.DiagonalMethod(testes);
        if x == True:
            print("Testes Realizado com Sucesso!")
        elif x == None:
            print("Erro, valor nulo retornado! (CODE:ERR01)")
        else:
            raise Exception("Erro na Execução do programa!\n (CODE:ERR02)")
    except:
        print("Erro na Execução do programa! \n (CODE:ERR03)")
    pass