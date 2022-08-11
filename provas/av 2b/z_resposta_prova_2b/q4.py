# problema das idades
#idades iniciais
chico   = 1.5
juca    = 1.1
# quantidades de anos até Juca ficar maior que Chico
quant_anos = 0

# repetir enquando juca menor que chico
while juca <= chico:
    chico+=0.02 # crescimento ano a ano de chico
    juca+=0.03 # crescimento ano a ano de juca
    quant_anos+=1 # a cada ano adicionar mais 1 

print("Juca demorou", quant_anos, "anos para ficar maior que Chico!")