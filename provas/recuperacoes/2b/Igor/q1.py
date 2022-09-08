op = 0

print("=============================\n"
      "| 01 - Resolução questão 01 |\n"
      "| 02 - Resolução questão 02 |\n"
      "| 03 - Resolução questão 03 |\n"
      "| 04 - Resolução questão 04 |\n"
      "| 05 - Resolução questão 05 |\n"
      "| 06 - Sair do sistema      |\n"
      "===============================")
op = int(input("Digite a questão que deseja: "))
while op != 6:
 if op == 1:
     print("Não fiz!")
 elif op == 2:
     n = int(input("Digite um número inteiro e positivo"))
     x = 1 + 2/(1^2) + 3/(2^3) + n/((n - 1)^n)
     print(x)
 elif op == 3:
     x = int(input("Digite um número inteiro e positivo: "))
     i = 1
     n = 0
 while x > n:
     b = int(input("Digite um número: "))
     i = i + b
     n = n + i
     print(n)
 elif op == 4:
     print("Não fiz!")
