#Ex04
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota01 = float(input("Insira a primeira nota: "))
nota02 = float(input("Insira a segunda nota: "))
nota03 = float(input("Insira a terceira nota: "))
nota04 = float(input("Insira a quarta nota: "))

media = (nota01 + nota02 + nota03 + nota04) / 4

if media >= 7.0 :
    print("Aprovado! Sua média foi: ", media)
else: print("Reprovado. Sua média foi: ", media)
