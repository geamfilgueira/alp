num = int(input('Digite um número maior que 0: '))
nu = 0
n = 1
while n <= num:
    for c in range(n, nu, -1):
        print(c, end=' ')
    print()
    n += 1
