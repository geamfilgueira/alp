

cpf = int(input("Digite seu cpf:"))
nome = str(input("Digite seu nome:"))
tc = int(input("Digite o tipo da conta:"))
vi = float(input("Digite o valor do investido:"))
qmi = int(input("Digite a quanidade de meses investidos:"))
rt = (vi * qmi)/100
print("O rendimento total foi de:",rt)
if tc == 1 :
    print("Poupança")
elif tc == 2:
    print("Fundos de Renda Fixa")
elif tc == 3:
    print("LCI ou LCA")


# logica errada - faltando a solucao
# 15


