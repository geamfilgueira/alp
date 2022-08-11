n = int(input("Digite o numero: "))
E = 1 # inicializando com 1 que eh o primeiro valor de E
i=1
j=1
while i <= n:
    # variavel f representa o valor do fatorial a cada iteração
    f = j
    fat=1 # inicializando com 1 para calculo do fatorial
    #calculo do fatorial do num
    while f >= 1:
        fat = fat * f 
        f-=1
    #calculo do valor de E a cada interação
    E = E + i/fat
    #incremento das variaveis de controle
    i+=1
    j+=1

print("O valor final de E:", E)