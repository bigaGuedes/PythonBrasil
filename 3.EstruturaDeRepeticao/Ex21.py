#Ex21
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('\nInsira um número inteiro: '))

countMult = 0

for count in range(2, num):
    if (num % count == 0):
        countMult += 1

if (countMult > 0 or num == 1):
    print(f'\nO número {num} não é primo.')

else:
    print(f'\nO número {num} é primo.')
