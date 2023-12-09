#Ex28
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

valorCDs = []

qtCDs = int(input('\nInsira a quantidade de CDs: '))

for i in range(qtCDs):
    precoCD = float(input(f'Insira o valor do {i+1}º CD: R$'))
    valorCDs.append(precoCD)

custoTotal = sum(valorCDs)
precoMedio = custoTotal / len(valorCDs)

print(f'\nO investimento total da coleção foi de R${custoTotal}.')
print(f'Cada CD tem um custo médio de R${precoMedio}.')