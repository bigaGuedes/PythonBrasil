#Ex08
#Faça um programa que pergunte o preço de três produtos e informe qual produto
#você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Insira o preço do primeiro produto: "))
p2 = float(input("Insira o preço do segundo produto: "))
p3 = float(input("Insira o preço do terceiro produto: "))

if p1 < p2 and p1 < p3 :
    print("Você deve comprar o primeiro produto.")
elif p2 < p1 and p2 < p3 :
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")