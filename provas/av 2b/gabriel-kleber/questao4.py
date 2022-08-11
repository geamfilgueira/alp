chico = 1.50
juca = 1.10
anos = 0
while chico > juca:
    anos += 1
    juca += 0.03
    chico += 0.02
print('Levou {:.0f} ano(s) para Juca ficar maior que Chico'.format(anos))
