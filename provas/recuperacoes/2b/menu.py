i=0
while i != 6:
    print("menu")
    print("[1]questao1")
    print("[2]questao2")
    print("[3]questao3")
    print("[4]questao4")
    print("[5]questao5")
    print("[6]sair")
    n=int(input("digite um numero que esta no menu que deseja ver"))
    if n == 1:
        n2=1
        maior=0
        menor=100000
        res=0
        com=0
        ind=0
        soma=0
        soma1=0
        while n2!=0:
            n1=float(input("digite o preco do kwh: "))
            n3=int(input("digite a quantidade de kwh consumidos durante o mes; "))
            n4=str(input("digite o codigo do tipo de consumidor ex; residencial,comecial ou industrial; "))
            if n3>maior:
                maior=n3
            elif n3<menor:
                menor=n3
            if  n4=="residencial":
                res+=1
            elif n4=="comecial":
                com+=1
            elif n4=="industrial":
                ind+=1
            soma=soma+n3
            soma1+=1
            n2=int(input("digite o seu numero de consumidor.atencao se quiser parar digite o numero 0: "))
        print("o maior consumo foi de; "  ,maior)
        print("o menor consumo foi de; " , menor)
        print("foram",res,"consumidores residencial", com ,"comecial" "e" , ind ,"industrial" )
        print("e a media de consumo foi de " , soma/soma1 )
#20
    elif n == 2:
        nu=int(input("digite um numero inteiro e positivo e que seja diferente de 0; "))
        if nu>0:
            x=1+(2/(1**2))+(3/(2**3))+(nu/((nu-1**n)))
        print("x  =", x )
#errado
    elif n==3:
        x=int(input("digite um numero para ver"))
        fim=x*3
        i=0
        while i!=fim:
            nu=int(input("digite um numero"))
            i=i+nu
            if i>fim:
                i=0
        print("fim...")
#20
    elif n==4:
        n5=int(input("digite um numero"))
        i=n5
        while i!=2000:
            soma= i%n5
            if soma==0:
                print(i)
            i+=1
#solução errada
    elif n==5:
        print("infelismente nao deu tempo")

    elif n==6:
        i=6
print("fim...")






