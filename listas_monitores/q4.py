a = int(input("Digite a base: "))
base = a
b = int(input("Digite o expoente: "))
i = 1
while i < b:
    a = a * base
    i += 1
print(a)
# ou simplemente 
# print(a**b)