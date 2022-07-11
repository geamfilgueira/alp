#Questao 01
cpf = int(input("Digite seu cpf: "))
nome = str(input("Digite seu nome: "))
tc = int(input("Digite seu tipo de conta (1, 2 ou 3): "))
vi = float(input("Digite seu valor investido: "))
qm = int(input("Digite a quantidade de meses do investimento: "))

if tc == 1:
    rt = qm * (vi * 0.5)/100
    print ("Seu rendimento eh ", rt)
elif tc == 2:
    rt = qm * (vi * 1)/100
    print ("Seu rendimento eh ", rt)
elif tc == 3:
    rt = qm * (vi * 1.5)/100
    print ("Seu rendimento eh ", rt)
else:
    print("Investimento não existe!!!")