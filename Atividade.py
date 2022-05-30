#Atividade de Dominique Salomão.

#Importando bibliotecas utilizadas
import numpy as np 

#Iniciando Interface Simples.
opcoes=True

#Apresentar Opções.
while opcoes:
    print ("""
    Qual código você deseja executar? 

    1.Soma de um Array
    2.Diferença Diagonal
    3.Palíndromo
    4.Fechar
    """)

#Aguardar Comando do Usuário.
    opcoes=input() 
    
#Opção 1: Código de Soma de um Array.
    if opcoes=="1": 
      testes = [[1, 2, 3, 4, 5], [4,4,8,8,12,12], [1,8,3,4,7,2],[1500,200,300],[1],[]];
      cont = 1;     
      soma = 0;
      for r in testes:
        for i in range(0, len(r)):    
            soma = soma + r[i];  
        print("A respota do teste "+str(cont)+" é "+str(soma))
        soma = 0;  
        cont = cont + 1;

#Opção 2: Código de Diferença das Diagonais.
    elif opcoes=="2":
      testes = [[[55, 25, 15], [30, 44, 2], [11, 45, 77]], [[11,2,4], [4,5,6], [10,8,-12]], [[0, 2], [1, 1], [2, 0]], [[2,3,4], [4,3,3], [3,3,4]]]
      cont = 1
      for r in testes:
        diagonalx = np.asarray(r)
        diagonaly = np.fliplr(r)
        diagonalx = np.trace(diagonalx)
        diagonaly = np.trace(diagonaly)
        sub = diagonalx - diagonaly
        sub = abs(sub)
        print("O valor absoluto do teste "+str(cont)+" é: "+str(sub))
        cont = cont + 1;

#Opção 3: Código do Identificador de Palíndromos.
    elif opcoes=="3":
      def Palindromo(testes):  
        return testes == testes[::-1]
      testes = ["ABBA","SOCORRAM ME SUBI NO ONIBUS EM MARROCOS","ABCDCBA","ABAB","OVO","BICICLETA","MULA","MUMUM"]
      cont = 1;
      for r in testes: 
        r = r.replace(" ","")
        resposta = Palindromo(r)
 
        if resposta:
         print("Teste "+str(cont)+" : A palavra '"+r+"' É um Palíndromo!")
         cont = cont + 1;
        else:
         print("Teste "+str(cont)+" : A palavra '"+r+"' NÃO é um Palíndromo!")
         cont = cont + 1;

#Opção 4: Fechar Programa.
    elif opcoes=="4":
      print("\n Programa Encerrado!")
      exit()

#Opção inexistente, tente outra vez.
    elif opcoes !="":
      print("\n Tente novamente com outra opção.") 