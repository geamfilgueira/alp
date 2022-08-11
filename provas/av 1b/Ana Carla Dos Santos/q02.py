#questão 02
codigo1 = int(input("Digite o código do seu primeiro lanche: "))
quantcod1 = int(input("Digite quantos lanches você comprou do seu primeiro lanche: "))
if codigo1 == 100:
    print ("O preço de uma unidade do seu primeiro lanche será 3.00 reais")
elif codigo1 == 101:
    print ("O preço de uma unidade do seu primeiro lanche será 3.50 reais")
elif codigo1 == 103:
    print ("O preço de uma unidade do seu primeiro lanche será 5.00 reais")
print ("Quando for digitar o preço, digite do modelo que está no comando. Ex: 3.50")
preco1 = float (input("Digite o preço de uma unidade do seu primeiro lanche: "))
precototalum = quantcod1*preco1
print ("O preço total do seu primeiro lanche será em reais: ", precototalum)
codigo2 = int(input("Digite o código do seu segundo lanche: "))
quantcod2 = int(input("Digite quantos lanches você comprou do seu segundo lanche: "))
if codigo2 == 100:
    print ("O preço de uma unidade do seu segundo lanche será 3.00 reais")
elif codigo2 == 101:
    print ("O preço de uma unidade do seu segundo lanche será 3.50 reais")
elif codigo2 == 103:
    print ("O preço de uma unidade do seu segundo lanche será 5.00 reais")
print ("Quando for digitar o preço, digite do modelo que está no comando. Ex: 3.50")
preco2 = float (input("Digite o preço da unidade do seu segundo lanche: "))
precototaldois = quantcod2*preco2
print ("O preço total do seu segundo lanche será em reais:", precototaldois)
valortotal = precototalum + precototaldois
print ("Você irá pagar no total R$: ", valortotal)

## 20 pontos






