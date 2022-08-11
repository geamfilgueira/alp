#leislane simplicio rodrigues
#questao 1

cpf = float(input('digite seu cpf: '))
nome = input("digite seu nome: ")
conta = int(input("digite o tipo de conta: "))
meses = int(input('digite a quantidae de meses de investimento: '))
if conta == 1:
    print('rendemento mensal de' , (meses*0.5/100))
elif conta == 2:
    print('fundos de renda fixa, com rendimeto mensal de' , (meses*1)/100)
elif conta == 3:
    print('LCI OU LCA, com rendimento mensal de' , (meses*1.5)/100)