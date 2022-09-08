r=0
r1=0
while r != 'sim':
    print("[=======================]\n"
          "[-resoluçao questao 1   ]\n"
          "[-resoluçao questao 2   ]\n"
          "[-resoluçao questao 3   ]\n"
          "[-resoluçao questao 4   ]\n")


    r=int(input("qual resposta deseja ver: "))


    if r == 1:
        preco=0
        numero=0
        qntkwh=0
        tipocons=0
        maiorv=0
        menorv=0
        i=1

        while i>0:
            preco=int(input("digite aqui o preço: "))
            numero=int(input("digite aqui o numero do consumidor: "))

            if numero == 0:
                break
            if numero > maiorv:
                maiorv=numero+1

            if numero< menorv:
                    menorv=menorv+1

        print(maiorv, menorv)

# questão 1 não está completa, considerei 15pontos !





    if r == 2:
        x=int(input("digite um numero "))
        s=int(input("digite um numero "))
        resultado=1
        while x <= s:
            x=int(input("digite um numero "))


            resultado=resultado+1
            s=s-1

        print(resultado)
# questão 2 está errada!

    if r == 3:
        n=int(input("digite um numero: "))
        d=0
        while n >=0:
            d=d-1
            while d <= 0:
                n=n+1
# questão 3 está errada!
    if r == 4:
        curso=0
        motiv=0
        idade=0
        genero=0
        r=0
        while r >= 0:
            curso=float(input("Digite seu curso(administracao, computacao, madicina, direito e jornalismo): "))
            motiv=float(input("Digite aqui o seu motivo por escolher essa profissão: "))
            idade=int(input("Digite aqui sua idade: "))
            genero=float(input("Digite aqui seu genero: "))

        if curso == 'administracao':
            administracao=curso+1



