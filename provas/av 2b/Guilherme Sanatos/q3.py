h=''
maior= 0
menor= 1000
mu=0
ho=0
altuho=0
altumu=0
i=0
mediapo=0




while h!= 'nao':
    mediamu=0
    t= input("digite o nome do habitante")
    o= input("digite o sexo do habitante(M ou F)")
    altu= int(input("digite a altura do habitante em cm"))
    if altu> maior:
        maior=altu
    if altu< menor:
        menor= altu
    if o== "M":
        altuho=altuho+altu
        ho=ho+1
        altuho=altuho
    if o ==" F ":
        altumo=altumo+altu
        mu=mu+1
        mediamu=mediamu+altumo
    i=i+1
    h= input("deseja continuar'")




print("maior altura: " , maior)
print("menor altura:" , menor)
print( mediamu )

print()
print()




#considerei 10 pontos