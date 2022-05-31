#Main para rodar os testes de Soma Array
from SomaArray import SomaArray

class MainSomaArray:
    try:
        testes = [
        [1, 2, 3, 4, 5], 
        [4,4,8,8,12,12], 
        [1,8,3,4,7,2],
        [1500,200,300],
        [1],
        []
        ];
        x = SomaArray.SomaArrayMethod(testes);
        if x == True:
            print("Testes Realizado com Sucesso!")
        elif x == None:
            print("Erro, valor nulo retornado! (CODE:ERR01)")
        else:
            raise Exception("Erro na Execução do programa!\n (CODE:ERR02)")
    except:
        print("Erro na Execução do programa! \n (CODE:ERR03)")
    pass