#Ex22
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input('\nInsira um número inteiro: '))

mults = []

for count in range(2, num):
    if (num % count == 0):
        mults.append(count)

countMult = len(mults)

if (countMult > 0 or num == 1):
    print(f'\nO número {num} não é primo.')
    print(f'{num} é divisível por {mults}')

else:
    print(f'\nO número {num} é primo.')