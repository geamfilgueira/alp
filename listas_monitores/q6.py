import os

while True:
    print("|----------------------- Menu Simples -----------------------|")
    print("|  Se quiser cadastrar funcionário, digite 1                 |")
    print("|  Se quiser cadastrar alimento, digite 2                    |")
    print("|  Se quiser cadastrar fornecedor, digite 3                  |")
    print("|                                                            |")
    print("|  Se quiser sair do programa, digite 0                      |")
    print("|------------------------------------------------------------|")
    print("")
    a = int(input("Digite aqui: "))

    if a == 0:
        break
    os.system('clear')

