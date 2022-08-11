i=1
x=0
z=0
y=0
h=0
l=0
while i<100:

    x=int(input("digite um numero usuario:"))
    if x>0 and x<25:
        z+=1
        print(z )
    elif x>26 and x<50:

        y+=1
        print(y)
    elif x>51 and x<75:

        h+=1
        print(h)
    elif x>76 and x==100:

        l+=1
        print(l)
    elif x== "-":
        print("seu numero esta invalido")
        break


#erro