nome = input("DIgite seu Nome: ")
nhrst = int (input("Digite sua quantidade de horas trabalhadas: "))
ndep = int (input("Digite o número de dependentes: "))
salario = (12*nhrst) + (40*ndep)
descinss = salario*(8.5/100)
descir = salario*(5/100)
salarioliq = (salario-descir)-descinss
print ("Dados do Funcionário: ")
print("Nome: ", nome)
print("Salário bruto: ", salario)
print("Valor do desconto do INSS: ", descinss)
print("Valor do desconto do IR: ", descir)
print("Salário líquido: ", salarioliq)


# ok
# 20