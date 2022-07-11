nome = input("digite seu nome: ")
cpf = input ("digite seu cpf: ")
conta = int( input("digite seu tipo de conta: "))
valor = int(input("digite o valor investido: "))
meses = int(input("digite a quantia de meses investidos: "))


if conta == 1:
        print(nome, "sendo seu investimento do tipo poupanca, seu rendimento total foi de",valor*0.5/100*meses,"%")
        print("sendo assim, a quantia atual dos seus investimentos e de: ", valor*0.5/100+valor)
else:
          if conta== 2:
              print(nome, "sendo seu investimento do tipo fundos de renda fixa, seu rendimento total foi de",valor*1/100*meses,"%")
              print("sendo assim, a quantia atual dos seus investimentos e de: ", valor*1/100+valor)
          else:
             if conta== 3:
                  print("sendo seu investimento do tipo lci ou lca, seu rendimento total foi de",valor*1.5/100*meses,"%")
                  print("sendo assim, a quantia atual dos seus investimentos e de: ", valor*1.5/100+valor)
             else:
                print("tipo de conta nao reconhecido")



p1=input ("digite o codigo do primeiro item:")

if p1==100:
    print("sendo o cachorro quente o seu primeiro item, custara r$ 3,0")
else:
  if p1==101:
    print("sendo o hamburguer o seu primeiro item, custara r$ 3,50")
  else:
        if p1==103:
          print("sendo o bauru completo o seu primeiro item, custara r$ 5,0")
        else:
         print("iteM nao reconhecidos")

        p2=input("digite o codigo do primeiro item:")
        if p2==100 :
               print("sendo o cachorro quente o seu primeiro item, custara r$ 3,0")
        else:
                    if p2==101:
                      print("sendo o hamburguer o seu primeiro item, custara r$ 3,50")
                    else:
                     if p2==103:
                              print("sendo o bauru completo o seu primeiro item, custara r$ 5,0")
                     else:
                         print("itens nao reconhecidos")
                         if p1==100 and p2==100:
                              print("o valor total eh r$6,0")
                         else:
                              if (p1==101 and p2==100) or (p2==101 and p1==100):
                                print("o valor total eh r$6,50")
                              else:
                                    if (p1==103 and p2==100) or (p2==103 and p1==100):
                                     print("o valor total eh r$8,0")
                                    else:
                                        if (p1==101 and p2==103) or (p2==101 and p1==103):
                                         print("o valor total eh r$8,50")
                                         if (p1==101 and p2==101) or (p2==101 and p1==101):
                                           print("o valor total eh r$7,0")
                                         else:
                                          if (p1==103 and p2==103) or (p2==103 and p1==103):
                                           print("o valor total eh r$10,0")

