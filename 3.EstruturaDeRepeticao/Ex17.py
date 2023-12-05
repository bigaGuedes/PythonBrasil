#Ex17
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Insira um número inteiro: '))

contador = 1
resultado = 1

while contador <= num:
    resultado *= contador
    contador += 1

print(f'O fatorial de {num} é {resultado}\n')



