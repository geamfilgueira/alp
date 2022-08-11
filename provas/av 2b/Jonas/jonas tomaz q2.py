n = int(input("diga um numero: "))
e = n - 1

while n == 4:
    e = n * e
    print(e)
    while n == 5:
        e = n * e
        print(e)
    if n == 4 and e == 24:
        print(e)
    elif n == 5 and e == 120:
        print(e)
    n = n + 5
#errado