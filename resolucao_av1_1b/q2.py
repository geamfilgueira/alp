it_1 = int(input("Digite primeiro item (100, 101, 102): "))
qt_1 = int(input("Digite a quantidade do primeiro item: "))
it_2 = int(input("Digite o segundo item diferente do primeiro (100, 101, 102):"))
qt_2 = int(input("Digite a quantidade do segundo item: "))

if it_1 == 100 and it_2 == 101:
    vtc = (3*qt_1) + (3.5*qt_2)
    print ("Seu joao ganhou: ", vtc)
elif it_2 == 100 and it_1 == 101:
    vtc = (3*qt_2) + (3.5*qt_1)
    print ("Seu joao ganhou: ", vtc)
elif it_1 == 100 and it_2 == 102:
    vtc = (3*qt_1) + (5*qt_2)
    print ("Seu joao ganhou: ", vtc)
elif it_2 == 102 and it_1 == 100:
    vtc = (5*qt_2) + (3*qt_1)
    print ("Seu joao ganhou: ", vtc)
elif it_1 == 101 and it_2 == 102:
    vtc = (3.5*qt_1) + (5*qt_2)
    print ("Seu joao ganhou: ", vtc)
elif it_2 == 102 and it_1 == 101:
    vtc = (5*qt_2) + (3.5*qt_1)
    print ("Seu joao ganhou: ", vtc)
else:
    print("vah comprar em outro lugar")