#Ex11
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo .
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.

n1 = int(input("Insira um número Inteiro: "))
n2 = int(input("Insira um número Inteiro: "))
n3 = float(input("Insira um número Real: "))

ra = n1 * 2 * (n2 / 2)
rb = (n1 * 3) + n3
rc = n3 ** 3

print("a.", ra)
print("b.", rb)
print("c.", rc)