#Ex33
# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []

print('\nDepartamento Estadual de Meteorologia\n')
count = int(input('Quantas temperaturas deseja registrar? '))

for i in range(count):

    temperatura = int(input(f'Insira a {i+1}º temperatura: '))
    temperaturas.append(temperatura)

maiorTemp = max(temperaturas)
menorTemp = min(temperaturas)
mediaTemp = sum(temperaturas) / len(temperaturas)

print(f'\n{maiorTemp}°C foi a maior temperatura registrada.')
print(f'{menorTemp}°C foi a menor temperatura registrada.')
print(f'{mediaTemp}°C foi a média das temperaturas registradas.\n')

