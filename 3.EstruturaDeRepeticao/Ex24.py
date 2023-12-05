# Ex24
# Faça um programa que calcule o mostre a média aritmética de N notas.

opNotas = int(input('\nInsira o número de notas que gostaria de adicionar: '))

notas = []

for i in range(opNotas):
    nota = float(input(f'Insira a {i + 1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'\nA média final é: {media}')