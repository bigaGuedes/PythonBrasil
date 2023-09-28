#Ex13
#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input("Insira um número entre 1 e 7: "))

if num == 1 :
    print("Esse número corresponde a Domingo.")
elif num == 2 :
    print("Esse número corresponde a Segunda.")
elif num == 3 :
    print("Esse número corresponde a Terça.")
elif num == 4 :
    print("Esse número corresponde a Quarta.")
elif num == 5 :
    print("Esse número corresponde a Quinta.")
elif num == 6 :
    print("Esse número corresponde a Sexta.")
elif num == 7 :
    print("Esse número corresponde a Sábado.")
else :
    print("Valor Inválido!")