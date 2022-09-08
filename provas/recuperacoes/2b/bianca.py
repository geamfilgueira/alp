op = 0
while op == 0:
    print("1. questao 1\n"
          "2. questao 2\n"
          "3. questao 3\n"
          "4. questao 4\n"
          "5. questao 5")
    op=int(input("digite a questao requerida(digite 0 para sair): "))

    if op==1:
     n1=1
     q1=0
     t1=0
     tt1=0
     mac1=0
     mec1=100000
     ci1=0
     cc1=0
     cr1=0
     mc1=0
     p1=0

     while n1!=0:
        n1=int(input("numero do consumidor(digite 0 para 'sair'): "))
        q1=int(input("quantidede de kWh consumidos durante o mes: "))
        t1=input("codigo do tipo de consumidor(r. residencial, c. comercial, i. industrial): ")

        if q1<mec1:
         mec1=q1
        elif q1>mac1:
         mac1=q1

        if t1=="i" :
            ci1+=q1
        elif t1=="c" :
            cc1+=q1
        elif t1=="r" :
            cr1+=q1

        mc1+=q1
        p1+=1
     print("maior consumo: ", mac1, " menor consumo:", mec1)
     print("consumo do residencial:", cr1,"consumo do comercial: ", cc1, "consumo industrial: ", ci1)
     print("media de consumo: ", mc1/p1 )

#Solução OK!
    elif op==2:
      print("nao lembro como faz")

    elif op==3:
        x3=0
        l3=0

        x3=int(input("digite numero x: "))
        while l3+(l3+1)!=x3:
            l3=int(input("digite numero qualquer: "))
            print(l3, "e o numero procurado")
#Solução errada!
    elif op==4:
        i4=1
        r4=0
        n4=int(input("digite um numero qualquer: "))
        while n4 > 0:
         if n4 % i4 == 0:
            r4=i4
         print("os divisores de", n4, "sao: ", r4)
#Solução OK!
    elif op==5:
        while c!= "FIM":
            print("1. administracao\n"
                  "2. computacao\n"
                  "3. medicina\n"
                  "4. direito\n"
                  "5.jornalismo")
            c=input("qual curso?:")
            i=input("qual motivo da escolha? (remuneracao; obtida pela profissao; aptidao ou outros)")
            i2= int(input("idade: "))
            g=input("genero:")


print("fim do programa")
