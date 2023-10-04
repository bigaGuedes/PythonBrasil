#Ex15
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.

vh = float(input("Quanto você recebe por hora? "))
ht = float(input("Quantas horas você trabalhou este mês? "))

sb = vh * ht

IR = sb * 0.11
INSS = sb * 0.08
SIND = sb * 0.05

sl = sb - (IR + INSS + SIND)

print("Salário Bruto:", sb)
print("INSS [11%]:", INSS)
print("Sindicato [5%]:", SIND)
print("Salário Líquido:", sl)
