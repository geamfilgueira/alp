a = int(input())

b = 0

if a > 0:
    while b < a:
        print(b)
        b = b + 2
else:
    if a % 2 == 0:
        while a <= b:
            print(a)
            a = a + 2
    else: 
        a = a + 1
        while a <= b:
            print(a)
            a = a + 2 

