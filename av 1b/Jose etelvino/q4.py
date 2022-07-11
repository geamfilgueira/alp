salario_fixo=float(input("salario fixo: "))
valor_das_vendas=float(input("valor dos carros: "))
carros_vendidos=int(input("quantidade de carros vendidos"))
comissão=float(input("valor da comissão: "))
porcentagem_das_vendas1=(valor_das_vendas)*0.05
carros=valor_das_vendas*carros_vendidos
salario_final=(salario_fixo+carros+comissão+porcentagem_das_vendas1)
print(salario_final)

# ok 20
