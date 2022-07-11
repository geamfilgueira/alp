cond=int(input("digite um codigo 100,101 ou 103"))
cond1=int(input("digite um codigo 100,101 ou 103"))
if cond==100 and cond1== 101:
     c=3+3.50
     print("o valor eh de" , c ,"reais" )
elif cond==100 and cond1== 103:
     c1=3+5
     print("o valor eh de", c1 ,"reais" )
elif cond==101 and cond1== 103:
     c2=3.50+5
     print("o valor eh de" , c2 ,"reais" )
elif cond==103 and cond1== 100:
     c3=3+5
     print("o valor eh de", c3 , "reais" )
elif cond==103 and cond1== 101:
     c4=3.50+5
     print("o valor eh de" , c4 , "reais" )
elif cond==101 and cond1== 100:
     c5=3+3.50
     print("o valor eh de" , c5 , "reais" )
elif cond==100 and cond1==100:
    c6=3+3
    print("0 valor eh de", c6 , "reias" )
elif cond==101 and cond1==101:
    c7=3.50+3.50
    print("0 valor eh de", c7 , "reais" )
elif cond==103 and cond1==103:
    c8=5+5
    print("0 valor eh de", c8 , "reais" )
else:
    print("algo deu errado ,tente novamente1")

# poxa só faltou a quantidade
# mas irei considerar a resposta 20