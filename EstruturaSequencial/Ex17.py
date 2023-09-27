#Ex17
#Faça um Programa para uma loja de tintas. O programa deverá pedir o
#tamanho em metros quadrados da área a ser pintada. Considere que a
#cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
#tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
#de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades
#de tinta a serem compradas e os respectivos preços em 3 situações:
#1. comprar apenas latas de 18 litros;
#2. comprar apenas galões de 3,6 litros;
#3. misturar latas e galões, de forma que o desperdício de tinta seja menor.
#4. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
#considere latas cheias.

m2 = float(input("Quantos m² de área a ser pintada? "))

import math
ltbruto = m2 / 6
lttotal = ltbruto * 1.1

#Apenas Latas (18l)
qtlata = math.ceil(lttotal / 18)
prtotal_lata = qtlata * 80
print("\n Apenas Latas:")
print("• Quantidade de latas:", qtlata)
print("• Preço total: R$", prtotal_lata)

#Apenas Galões (3.6l)
qtgalao = math.ceil(lttotal / 3.6)
prtotal_galao = qtgalao * 25
print("\n Apenas Galões:")
print("• Quantidade de galões:", qtgalao)
print("• Preço total:", prtotal_galao)

#Misturando Galões e Latas
qtlata_mix = int(lttotal // 18)
lttotal_sobra = lttotal - (qtlata_mix * 18)
qtgalao_mix = math.ceil(lttotal_sobra / 3.6)
prtotal_mix = (qtlata_mix * 80) + (qtgalao_mix * 25)
print("\n Latas e Galões:")
print("• Quantidade de latas:", qtlata_mix)
print("• Quantidade de galões:", qtgalao_mix)
print("• Preço total: R$", prtotal_mix)