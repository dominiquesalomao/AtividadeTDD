
class Palindromo:

      def PalindromoMethod(testes):  
        
        cont = 1;
        for r in testes: 
            r = r.replace(" ","")
            resposta = r
    
            if resposta:
                print("Teste "+str(cont)+" : A palavra '"+r+"' É um Palíndromo!")
                cont = cont + 1;
            else:
                print("Teste "+str(cont)+" : A palavra '"+r+"' NÃO é um Palíndromo!")
                cont = cont + 1;
        return testes == testes[::-1]