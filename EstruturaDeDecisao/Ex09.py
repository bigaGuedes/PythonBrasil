#Ex09
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Insira o preço do primeiro produto: "))
n2 = float(input("Insira o preço do segundo produto: "))
n3 = float(input("Insira o preço do terceiro produto: "))

if n1 < n2:
    n1, n2 = n2, n1

if n1 < n3:
    n1, n3 = n3, n1

if n2 < n3:
    n2, n3 = n3, n2

print(f"Ordem decrescente: {n1}, {n2} e {n3}")