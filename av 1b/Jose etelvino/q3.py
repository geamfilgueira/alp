nome=str(input("nome : "))
horas=int(input("horas trabalhadas: "))
dependentes=int(input("dependentes: "))
pagamento=horas*12
pagamento2=dependentes*40
salario=(pagamento+pagamento2)*0.85
salario2=(pagamento+pagamento2)*0.5
salario_bruto=pagamento+pagamento2
salario_liquido=salario+salario2
print(nome , horas ,  dependentes ,  salario , salario2)
print(salario_liquido, salario_bruto )
# erro de logico 10