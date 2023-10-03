#Ex27
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kilosmo = float(input("Quantos quilos (Kg) de Morango? "))
kilosma = float(input("Quantos quilos (Kg) de Maçã? "))

if kilosmo <= 5:
    preco1 = 2.5 * kilosmo
else:
    preco1 = 2.2 * kilosmo

if kilosma <= 5:
    preco2 = 1.80 * kilosma
else:
    preco2 = 1.50 * kilosma

preco = preco1 + preco2

if kilosmo + kilosma > 8 or preco > 25:
    preco = preco - (preco * 0.1)

print(f"Valor total a ser pago: R$ {preco}.")