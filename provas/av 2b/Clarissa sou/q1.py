n=0
int_1=0
int_2=0
int_3=0
int_4=0
while n>=0 and n<=100:

    n=int(input("digite um número: Se quiser parar o código use um número negativo"))

    if n>=0 and n<=25:
        int_1=int_1+1
        print("int_1 recebe:",int_1)
    if n>=26 and n<=50:
        int_2= int_2+1
        print("int_2 recebe:",int_2)
    if n>=51 and n<=75:
        int_3=int_3+1
        print("int_3 recebe:",int_3)
    if n>=76 and n<=100:
        int_4= int_4+1
        print("int_4 recebe:",int_4)
print("A quantidade de números entre 0 e 25 é:", int_1, "A quantidade de números entre 26 e 50 é:", int_2, "A quantidade de números entre 51 e 75 é:", int_3, "A quantidade de números entre 76 e 100 é:", int_4)

# 25 pontos