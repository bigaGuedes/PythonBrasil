#Ex06
#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))

if n1 > n2 and n1 > n3 :
    print("O maior número é:", n1)
elif n2 > n1 and n2 > n3 :
    print("O maior número é:", n2)
else:
    print("O maior número é:", n3)