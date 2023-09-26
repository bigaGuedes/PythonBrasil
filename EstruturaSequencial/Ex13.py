#Ex13
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sx = int(input("Escolha: 1. Masculino | 2. Feminino: "))
h = float(input("Altura: "))

psidm = (72.7*h) - 58
psidf = (62.1*h) - 44.7

if sx == 1 :
    print(psidm)
else: print(psidf)