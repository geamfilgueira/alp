nome = input ("Nome do funcioário: ")
horas = int(input ("Horas trabalhadas: "))
dependentes = int(input("Número de dependentes: "))
descontos = (8.5/100)+(5/100)
salariob=horas*12+dependentes*40
print ("Nome: ", nome)
print ("Salário bruto: ", salariob)
print ("Valor descontado do INSS: ", salariob*(8.5/100))
print ("Valor descontado do IR:", salariob*(5/100))
print ("O salário liquido é de: ", salariob-salariob*descontos)
# logica errada 
# 10