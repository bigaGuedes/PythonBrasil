#Ex22
#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input("Insira um número inteiro: "))

mod = num % 2

if mod == 1 :
    print(f"{num} é um número ímpar.")
else : print(f"{num} é um número par.")