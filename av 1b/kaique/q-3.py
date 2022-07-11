#kayque ferreira de albuquerque#
a = str(input("digite seu nome"))
b = int(input("digite sua quantidade de horas trabalhadas"))
c = int(input("digite a quantiade de dependentes"))
hr = b * 12
dp = c * 40
print (a)
print (c)
print ("o INSS vai desconrar 8.5 por cento do seu salário")
print (" o  IR vai descontar 5.0 por cento do seu salário")
print ("seu salário bruto vai ser de: ",hr+dp)
l = hr+dp
desc = ((l - 13.5)-l)
print ("o seu salário líquido vai ser de",desc)

#calculo errado
# 7