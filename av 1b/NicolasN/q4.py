nc = int(input("Número de carros vendidos: "))
nv = float(input("Valor total dos carros vendidos: "))
sf = float(input("Salário fixo: "))
cv = float(input("Valor por carro vendido: "))
st = sf+nc*cv+nv*(5/100)
print ("O salário final é de: ", st)
#20