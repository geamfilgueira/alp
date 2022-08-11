a = input()
b = input()
i = 0
cont = 0

while i < len(a):
    if a[i] == b:
        cont += 1
    i = i + 1

print(cont)