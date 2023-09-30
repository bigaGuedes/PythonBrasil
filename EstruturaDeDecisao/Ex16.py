#Ex16
#Faça um programa que calcule as raízes de uma equação do segundo grau,
#na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
#fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do
#segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import sys

a = int(input("Informe o valor de [a]: "))

if a == 0 :
    sys.exit("A Equação não é do segundo grau.")


b = int(input("Informe o valor de [b]: "))
c = int(input("Informe o valor de [c]: "))

delta = (b ** 2) - (4 * a * c)

x1 = (((-1) * b) + (delta ** 0.5))/(2 * a)
x2 = (((-1) * b) - (delta ** 0.5))/(2 * a)

if delta < 0 :
    sys.exit("A Equação não possui raízes reais.")

if delta == 0 :
    print(f"A Equação possui apenas uma raíz. Seu valor é: {x1}")
elif delta > 0 :
    print(f"A Equação possui duas raízes reais. Seus valores são:")
    print(f"Raíz Positiva: {x1}")
    print(f"Raíz Negativa: {x2}")




