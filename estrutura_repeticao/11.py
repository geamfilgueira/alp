x = int(input("Digite o num de funcionario: "))
i = 1
soma_salario = 0.0
while i <= x:
    salario = float(input("Digite o salario do funcionario: "))
    soma_salario = soma_salario + salario
    i = i+1

print("A media dos salarios eh ", soma_salario/x)