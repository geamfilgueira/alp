while True:
    print("digite 1 para questao 1:")
    print("digite 2 para questao 2:")
    print("digite 3 para questao 3:")
    print("digite 4 para questao 4:")
    print("digite 5 para questao 5:")
    print("digite 0 para sair")

    z = int(input("digite sua escolha:"))
    if z == 0 :
       print("fim do progama")
    if z == 1:

        preco = int(input("digite o preço do seu kmh:"))
        num = int(input("digite o seu numero:"))
        quant = int(input("digite a quantidade de kmh consumidos durante um mes:"))
        maior = 1
        menor = -1
        cod = int(input("digite seu tipo de codigo"))
        while num != 0:
            if quant > maior:
                print (quant)
            if quant < menor:
                print(quant)
#Solução não está completa, 15 pontos!
    if z == 2 :
       print("não fiz")

    if z == 3:
        x = 1
        d = 0
        while d + x >= x ** 3:
            x = int(input("digite um numero"))
            d += d
            print(x)
#Solução errada!
    if z == 4:
        print("não fiz")


    if z == 5:
         qcf = str(input("qual o curso que voce faz?"))
         qme = str(input("qual o motivo da escolha?  remuneracao obtida pela profissao, aptidao ou outros"))
         idd = int(input("qual sua idade?"))
         gnr = str(input("qual seu genero?"))
         f = str(input("digite 0 se deseja sair"))
         b = 1
         while f != 0:
                if idd < 20 and qme == aptidao:
                    print(b)
                    b += b

#Solução errada
