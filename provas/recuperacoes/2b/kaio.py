while True:
    print("-------------menu-------------")
    print("|questao 1                   |")
    print("|questao 2                   |")
    print("|questao 3                   |")
    print("|questao 4                   |")
    print("|questao 5                   |")
    print("------------------------------")

    op = int(input("digite um numero:"))

    if op == 1:
        maior = - 1000
        menor = 1000
        residencial = 0
        r = 0
        c = 0
        i = 0
        industrial = 0
        comercial = 0
        media = 0
        while True:
            c_tipo = input("tipo de consumidor:")
            preço = float(input("digite o preço do kwh :"))
            n_consumidor = int(input("digite o numero do consumidor:"))
            q_consumidos = int(input("digite  a quantidade de kwh consumidor durante o mes:"))


            if maior < q_consumidos:
                maior = q_consumidos
            elif menor > q_consumidos:
               menor = q_consumidos

            if c_tipo == residencial:
                r = r + q_consumidos
            elif c_tipo == comercial:
                c = c + q_consumidos
            elif c_tipo == industrial:
                i = i + q_consumidos
            if n_consumidor > 0:
                media = n_consumidor/q_consumidos
            elif n_consumidor == 0:
                break
        print("o maior consumo",maior)
        print("o menor consumo",menor)
        print(" consumidor residencial",r)
        print(" consumidor comercial",c)
        print(" consumidor industrial",i)
        print("media do consumo")

    elif op == 2:
        n = int(input("digite um numero:"))
        i = 1
        X = 1
        e = 1
        while 0 <= n:
            j = i
            while 0 <= j:
                j -= 1
                X = j * j/n
        print(X)

 #   elif op == 3:












