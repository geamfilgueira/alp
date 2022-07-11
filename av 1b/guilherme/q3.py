n=input('digite seu nome')
h=float(input('digite o numero de horas trabalhadas'))
nd=float(input('digite o numero de dependentes'))
print(12*h+nd*40)
sb=12*h+nd*40
inss=sb*0.085
print("seu nome ", n)
print("desnconto do inss")
print( sb*0.085)
ir=sb*0.05
print('desconto do ir')
print(sb*0.05)
print("seu salario liquido " )
print(sb-inss-ir)
#certo 20