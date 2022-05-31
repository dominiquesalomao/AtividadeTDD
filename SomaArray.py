class SomaArray:

    def SomaArrayMethod(testes):
        cont = 1;     
        soma = 0;
        try:
            for r in testes:
                for i in range(0, len(r)):    
                    soma = soma + r[i];  
                print("A resposta do teste "+str(cont)+" é "+str(soma))
                soma = 0;  
                cont = cont + 1;
            return True
        except:
            return False