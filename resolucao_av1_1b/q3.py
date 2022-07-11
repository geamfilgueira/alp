nome = str(input("Digite seu nome: "))
horas = int(input("Digite suas horas trabalhadas: "))
dep = int(input("Digite a sua quant de dependentes: "))
#salario bruto
sb = (horas*12) + (dep*40)

#descontos
inss = (sb * 8.5)/100
ir = (sb * 5)/100

sl = sb - inss - ir
print("Seu salario bruto eh ", sb)
print("Seu salario liquido eh ", sl)