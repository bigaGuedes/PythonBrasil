#Ex16
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
#de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas
#de tinta a serem compradas e o preço total.

m2 = float(input("Quantos m² de área a ser pintada? "))

import math

lttotal = m2 / 3
qtlata = math.ceil(lttotal / 18)
prtotal = qtlata * 80

print("Quantidade de latas:", qtlata)
print("Preço total: R$", prtotal)