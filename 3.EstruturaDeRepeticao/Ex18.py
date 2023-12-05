#Ex18
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numNums = int(input('\nInsira quantos números você vai adicionar: '))
listaNums = []

for nums in range(numNums):
        
    num = int(input(f'Insira o {nums + 1}º número: '))
    listaNums.append(num)

maiorNum = max(listaNums)
menorNum = min(listaNums)
somaNums = sum(listaNums)

print(f'\nO maior número fornecido é: {maiorNum}')
print(f'\nO menor número fornecido é: {menorNum}')
print(f'\nA soma de todos os números é: {somaNums}\n')


