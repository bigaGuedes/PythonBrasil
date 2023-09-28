#Ex15
#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

#receber os dados dos 3 lados do triangulo
#verificar se é um triangulo
#se for mentira, retornar que não é um triângulo
#se for verdade, retornar o tipo do triângulo

lado01 = float(input("Primeiro Lado: "))
lado02 = float(input("Segundo Lado: "))
lado03 = float(input("Terceiro Lado: "))

if lado01 + lado02 <= lado03 or lado01 + lado03 <= lado02 or lado02 + lado03 <= lado01 :
    print("Não pode ser um triângulo.")
elif lado01 == lado02 and lado01 == lado03 :
    print("Este triângulo é Equilátero.")
elif lado01 == lado02 or lado01 == lado03 or lado02 == lado03:
    print("Este triângulo é Isósceles.")
else :
    print("Este triângulo é Escaleno.")