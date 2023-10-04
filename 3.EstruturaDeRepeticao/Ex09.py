#Ex09
#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

lista = list(range(1, 51))

for num in lista:
    if num % 2 != 0:
        print(num)