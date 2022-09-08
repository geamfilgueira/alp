op = 0
while op != 6:
    print("1 - Resultado da questão 1")
    print("2 - Resultado da questão 2")
    print("3 - Resultado da questão 3")
    print("4 - Resultado da questão 4")
    print("5 - Resultado da questão 5")
    print("6 - Sair do programa")
    op = int(input("Digite uma opção:"))

    if op == 1:
        print("Não resolvida")

    elif op == 2:
        print("Não resolvida")

    elif op == 3:
        x = int(input("Digite um número:"))
        soma = 0
        triplo = 1
        i = 0
        j = 0
        if x > 0:
           while soma != triplo:
            i = i + 1
            print(i)
            j = i - 1
            soma = soma + j
            triplo = x * 3
            print("O triplo é :", triplo)
            print(soma)

    elif op == 4:
        num = int(input("Digite um número:"))
        i = 1
        j = 0
        divisor = 0
        while num > 0:
            num = int(input("Digite o mesmo número novamente:"))
            i = i + 1
            j = num - i
            if num % 2 == 0:
                divisor = num / i
                print("Os divisores são", i, divisor)

    else:
        print("Opção inválida")
