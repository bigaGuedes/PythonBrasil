#Ex19
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numNums = int(input('\nInsira quantos números você vai adicionar: '))
listaNums = []

while True:
    
    for nums in range(numNums):
        
        num = int(input(f'Insira o {nums + 1}º número: '))
        
        if num >= 0 and num <= 1000:
            listaNums.append(num)
        
        else:
            print('\nPor favor, insira um número entre 0 e 1000.\n')
            continue
    
    break

maiorNum = max(listaNums)
menorNum = min(listaNums)
somaNums = sum(listaNums)

print(f'\nO maior número fornecido é: {maiorNum}')
print(f'\nO menor número fornecido é: {menorNum}')
print(f'\nA soma de todos os números é: {somaNums}\n')


