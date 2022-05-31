#Main para rodar os testes de Palindromo
from Palindromo import Palindromo

class MainPalindromo:
    try:
        testes = [
        "ABBA",
        "SOCORRAM ME SUBI NO ONIBUS EM MARROCOS",
        "ABCDCBA",
        "ABAB",
        "OVO",
        "BICICLETA",
        "MULA",
        "MUMUM"
        ];
        x = Palindromo.PalindromoMethod(testes)
        if x != None:
            print("Testes Realizado com Sucesso!")
        elif x == None:
            print("Erro, valor nulo retornado! (CODE:ERR01)")
        else:
            raise Exception("Erro na Execução do programa!\n (CODE:ERR02)")
    except:
        print("Erro na Execução do programa! \n (CODE:ERR03)")
    pass