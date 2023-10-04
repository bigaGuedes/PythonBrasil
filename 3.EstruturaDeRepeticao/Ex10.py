#Ex10
#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

while True:
    num1 = float(input("Insira um número: "))
    num2 = float(input("Insira outro número: "))
    if round(num1) != num1 or round(num2) != num2:
        print("\nPor favor, insira um número inteiro.")
        continue
    elif num1 > num2:
        num1 = int(num1)
        num2 = int(num2)
        num1, num2 = num2, num1
        for inter in range(num1, num2)[1:]:
            print(inter)
        break        
    else:
        num1 = int(num1)
        num2 = int(num2)
        for inter in range(num1, num2)[1:]:
            print(inter)        
    break