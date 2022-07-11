#José Etelvino de Medeiros Neto





cpf=int(input("digite seu cpf: "))
nome=str(input("digite seu nome: "))
valor_investido=float(input("digite o valor investido: "))
meses_investidos=int(input("digite a quantidade de meses que houve investimento: "))

poupança=(valor_investido*meses_investidos)*0.05
fundo_de_renda_fixa=(valor_investido*meses_investidos)*0.1
lci_lca=(valor_investido*meses_investidos)*.15
esclha=str(input("esclha: "))

if esclha  = 1:
    print(poupança, cpf , nome)

elif esclha = 2:
    print(fundo_de_renda_fixa, cpf , nome)

elif esclha = 3:
    print(lci_lca, cpf , nome)

else:
print("escolha 1 2 ou 3")

# não rodou