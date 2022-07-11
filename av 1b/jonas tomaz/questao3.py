
#jonas ramos tomaz

nome = (input("digite o nome: "))
hora = (input("digite as horas trabalhadas: "))
dep = (input("digite o numero de dependencias: "))
hr = hora * 12
sb = dep * 40 + hr
inss = 8.5/100 + sb
ir = 5/100 + inss
sl = ir


print("o nome dele(a) eh ", nome," o seu salario bruto eh: ",sb)
print("o desconto do inss eh ", inss, "e o do ir eh: ", ir)
print("com isso oseu salario liquido e: ", sl)

# logica errada
# 5