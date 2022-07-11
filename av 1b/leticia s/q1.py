cpf=int(input("digite seu cpf: "))
nome=str(input("digite seu nome: "))
tipo=int (input("digie 1 para popança, 2 para fundos de renda fixa ou 3 para lci ou lca: "))
valor = float (input("digite o valor invesido"))
quant_meses = int(input("digite o total de meses"))
print("o cpf eh: ", cpf, "o nome eh: ", nome,"o tipo de conta eh :", tipo, "o rendimento eh: ")
if tipo == 1:
    print(valor*quant_meses* 0.5/100)
elif tipo == 2:
    print(valor*quant_meses* 1/100)
elif tipo == 3:
    print(valor*quant_meses* 1.5/100)


# ok
# 20