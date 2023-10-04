#Ex09
#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#Fórmula: C = 5 * ((F-32) / 9)

F = float(input("Insira uma Temperatura em Fahrenheit: "))
C = 5 * ((F - 32) / 9)
print("Em graus Celsius, essa temperatura equivale a", C)