in1=0
in2=0
in3=0
in4=0
i=1
while i !=0:
    n=int(input("digite um numere"))
    if n>0 and n<=25:
        in1=n
    elif n >=26 and n <=50:
        in2=n
    elif n >=51 and n <=75:
        in3=n
    elif n >=76 and n <=100:
        in4=n
    n=int(input("se quiser para digite 0; "))
    i=1+1
print("o total de numeros digitados entre 0-25 sao", in1 ,"o total de numeros digitados entre 26-50 sao", in2 ,"o total de numeros digitados entre 51-75 sao", in3 ,"o total de numeros digitados entre 76-100 sao", in4 ,)

#considerei 10 pontos