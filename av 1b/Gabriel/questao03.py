#aluno: Gabriel Kleber da Silva Batista
n = input('digite seu nome: ')
h = int(input('digite a quantidade de horas trabalhadas: '))
d = int(input('digite o número de dependentes: '))
s = float(input('digite seu salario bruto: '))
inss = (s * 8.5 / 100)
ir = (s * 5 / 100)
des = inss + ir
sl = (h * 12) + (d * 40) + s - des
print('o salario liquido do funcionario {} é de R${:.2f}'.format(n, sl))

# Calculo errado, o salario bruto era para ser (h * 12) + (d * 40) e não solicitar do usuario
# considerei 15
