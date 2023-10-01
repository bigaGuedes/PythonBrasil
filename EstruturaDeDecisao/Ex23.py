#Ex23
#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Insira um número: "))

if round(num) != num :
    print(f"{num} é um número decimal.")
else: print(f"{int(num)} é um número inteiro.")