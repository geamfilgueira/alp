i=1
b=0.00
c=b<1000.0
z= b>0.0

while i<100:

    z=int(input("digite seu numero"))
    if z ==0:
        print("masculino")
    elif z==1:
        print("feminino")
    else:
        print("sexo desconhecido")
        break

    b=float(input("digite a altura"))
    if b>0.0:
        b=z
        print(z)
    elif b<1000.0:
        b=c
        print(c)
    h=z/c
    print(h)
    nn1=input("digite se deseja sair")

    z=0
    x=z

    if nn1 =="sim":
     print ("tchau")

    elif nn1 =="nao":
      print("continue")
