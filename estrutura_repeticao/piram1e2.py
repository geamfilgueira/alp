n = int(input("Digite o tamanho da n: "))
i = n
# pirâmide 01
while i > 0:
    j =  i 
    while j > 0:
        print (j , " ", end=" ") 
        j-=1
    i-=1
    print("\n")

print("\n")
# pirâmide 02
i = 1
while i <= n:
    j =  1 
    while j <= i:
        print (j , " ", end=" ") 
        j+=1
    i+=1
    print("\n")