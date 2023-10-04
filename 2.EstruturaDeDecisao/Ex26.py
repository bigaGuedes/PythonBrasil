#Ex26
#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = float(input("Quantos litros vendidos? "))
combustivel = input('Qual o tipo de combustível? Responda "A" para Álcool e "G" para Gasolina: ')

if combustivel == "A" or combustivel == "a":
    if litros <= 20:
        preco = litros * 1.90 - (litros * (1.90 * 0.03))
    else:
        preco = litros * 1.90 - (litros * (1.90 * 0.05))
elif combustivel == "G" or combustivel == "g":
    if litros <= 20:
        preco = litros * 2.50 - (litros * (2.50 * 0.03))
    else:
        preco = litros * 2.50 - (litros * (2.50 * 0.03))

print(f"Valor a ser pago: R${preco}")