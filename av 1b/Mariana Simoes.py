ncv=int(input("digite o numero de carros vendidos"))
vtv=int(input("digite o valor de vendas"))
sf=int(input("digite seu salario fixo"))
vpcv=int(input("digite o valor que recebe por carros vendidos"))

cvv= vtv*0.05
salf= sf+ncv+cvv

print(salf)




nome=input("digite seu nome")
numh=int(input("digite o numero de hotas trabalhadas"))
numd=int(input("digite o numero de dependentes"))

hora= 12*numh
dep=40*numd

sb=hora+dep
di=sb-0.85
dir=sb-0.05

sl= (sb-di-dir)


print(nome, sb, di, dir, sl)
