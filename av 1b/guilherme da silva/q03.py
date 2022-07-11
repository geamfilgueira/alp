nome = str(input('digite seu nome: '))
hora = int(input('quantas horas você trabalha: '))
dpd = int(input('quantidade de dependentes: '))
valor1 = hora*12
valor2 = dpd*40
valor3 = valor1+valor2
inss = (valor3*0.085)
ir = (valor3*0.05)
saliq = (valor3-(inss+ir))
print(nome)
print('salario bruto',valor3)
print('inss', inss)
print('ir', ir)
print('salario liquido', saliq)


#guilherme da silva
#acertou 20