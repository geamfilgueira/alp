
#Questao01
cpf = input("Escreva o CPF: ")
nome = input("Escreva o seu nome: ")
conta = input("Escreva o tipo de conta (poupanca, FRF, LCI): ")
investido = float(input("Escreva o valor investido: "))
meses = int(input("Escreva a quantidade de meses que o valor ficou investido: "))
pp= (0.5/100)
frf=(1/100)
lci=(1.5/100)
print ("Nome: ",nome)
print ("CPF: ",cpf)
print ("Conta: ",conta)
print ("Valor investido: ",investido)
print ("Meses desde o investimento: ",meses)
if conta=="poupanca":
    print ("O valor que você tem agora é de: ", investido+investido*(meses*pp))
elif conta=="FRF":
    print ("O valor que você tem agora é de: ", investido+investido*(meses*frf))
elif conta=="LCI":
    print ("O valor que você tem agora é de: ", investido+investido*(meses*lci))
else:
    print ("Algo está errado, tente novamente.")

# 20