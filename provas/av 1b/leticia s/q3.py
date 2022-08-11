nome = str(input("digite seu nome: "))
horas = int(input("digite as horas: "))
dependentes = int(input("digite o numero de dependentes: "))
n1 = horas * 12
n2 = dependentes * 40
s = n1 + n2
d1 =  s*8.5 /100
d2 = s*5/100

sb = s- ((s*8/100)+(s*5/100))

print("seu nome eh: ", nome, "as horas trabalhadas foram", horas, "o numero de dependentes são: ",dependentes, "o desconto do inss eh:", d1, "o desconto do ir eh: ", d2,"seu salario bruto eh",sb )

# 20