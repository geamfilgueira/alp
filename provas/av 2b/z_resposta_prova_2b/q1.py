#inicializei com zero para poder entrar no while
num = 0
#Variaveis contadoras dos intervalos
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while num >= 0:
    num = int(input("Digite um numero (para sair digite um numero negativo): "))
    if num >= 0 and num <=25:
        intervalo_0_25+=1
    elif num >= 26 and num <=50:
        intervalo_26_50+=1
    elif num >= 51 and num <=75:
        intervalo_51_75+=1
    elif num >= 76 and num <=100:
        intervalo_76_100+=1
    else:
        print("Numero fora do intervalo")

print("[0 - 25]: ", intervalo_0_25, "\n[26 - 50]: ", intervalo_26_50, "\n[51 - 75]: ", intervalo_51_75, "\n[76 - 100]: ", intervalo_76_100)