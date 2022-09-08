
op = 0
while op != 6:
    print("1 - Questao 01")
    print("2 - Questao 02")1
    print("3 - Questao 03")
    print("4 - Questao 04")
    print("5 - Questao 05")
    print("6 - Sair ")
    op = int(input("Digite uma opção: "))

    if op == 1:
        n1 = int(input("Digite o numero"))
        n2 = int(input("Digite o numero"))
        print(n1+n2)
    elif op == 2:
        print("Anderson o lider!")