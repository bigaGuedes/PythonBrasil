#Ex14
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

listaPares = []
listaImpares = []

for i in range(10):
    num = int(input(f'Insira o {i+1}º número inteiro: '))
    
    if num % 2 == 0:
        listaPares.append(num)
    
    else:
        listaImpares.append(num)

pares = len(listaPares)
impares = len(listaImpares)

print(f'\nEntre os números inseridos, {pares} são pares e {impares} são ímpares.\n')