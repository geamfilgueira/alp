neg = " "
inter1 = 0
inter2 = 0
inter3 = 0
inter4 = 0
rep = int(input("digite a quantidade de numeros: "))
i = 1

while neg != '-1':
    while i < rep:
          i += 1
          n = int(input("digite o numero desejado: "))
          if n > 0:
              if n >= 0 and n <= 25:
                   inter1 = n
              elif n >= 26 and n <= 50:
                   inter2 = n
              elif n >= 51 and n <= 75:
                   inter3 = n
              elif n >= 76 and n <= 100:
                   inter4 = n
          else:
              neg = input('''digite -1 se deseja sair,
              ou NAO, se deseja continuar ''')
          print(inter1)
          print(inter2)
          print(inter3)
          print(inter4)




#considerei 15 pontos


