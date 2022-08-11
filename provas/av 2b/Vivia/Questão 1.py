n=0
tipo1=0
tipo2=0
tipo3=0
tipo4=0
while n>=0:
    n=int(input("digite um número:"))
    if n<=25 and n>=0:
        tipo1=tipo1+1
    elif n<=50 and n>=26:
        tipo2=tipo2+1
    elif n<=75 and n>=51:
        tipo3=tipo3+1
    elif n<=100 and n>=76:
        tipo4=tipo4+1
    else:
        print("Esse número não está entre 0 e 100")
print("Existem essa quantidade de números entre 0-25", tipo1)
print("Existem essa quantidade de números entre 26-50", tipo2)
print("Existem essa quantidade de números entre 51-75", tipo3)
print("Existem essa quantidade de números entre 76-100", tipo4)


#25 pontos