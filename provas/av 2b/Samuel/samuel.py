qnt = 0
qnt_n = 0
qnt2 = 0
qnt2_n = 0
qnt3 = 0
qnt3_n = 0
qnt4 = 0
qnt4_n = 0
while qnt >= 0:
    qnt = int(input("Digite a quantidade de numeros:"))
    if qnt >= 0 and qnt <= 25:
        qnt_n = qnt_n + 1
    elif qnt >= 26 and qnt <= 50:
        qnt2 = qnt2 + 1
    elif qnt >= 51 and qnt <= 75:
        qnt3 = qnt3 + 1
    elif qnt >= 76 and qnt <= 100:
        qnt4 = qnt4 + 1
    else:
        print("numero maoir que 100")
print("A quantidade de numeros na primeira intervalo eh:",qnt_n)
print("A quantidade de numeros na segunda intervalo eh:",qnt2)
print("A quantidade de numeros na terceira intervalo eh:",qnt3)
print("A quantidade de numeros na quarta intervalo eh:",qnt4)


#25 pontos