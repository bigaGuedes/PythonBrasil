#Ex28
#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carne = int(input("Qual tipo de carne? Insira [1] para Filé Duplo, [2] para Alcatra ou [3] para Picaha: "))
kilos = float(input("Quantos quilos (Kg)? "))
pagamento = int(input("A compra será realizada com o Cartão Tabajara? Insira [1] para 'Sim' ou [2] para 'Não': "))

if carne == 1:
    carne = "Filé Duplo"
    if kilos <= 5:
        preco = kilos * 4.90
    else:
        preco = kilos * 5.80

if carne == 2:
    carne = "Alcatra"
    if kilos <= 5:
        preco = kilos * 5.90
    else:
        preco = kilos * 6.80

if carne == 3:
    carne = "Picanha"
    if kilos <= 5:
        preco = kilos * 5.90
    else:
        preco = kilos * 7.80         

if pagamento == 1:
    tipopag = "Cartão Tabajara"
    desconto = preco * 0.05
    total = preco - desconto
else:
    tipopag = "Dinheiro ou Outro Cartão"
    desconto = 0
    total = preco 

print("\nCUPOM FISCAL\n")
print("################\n")
print(f"Carne: {carne}")
print(f"Quantidade: {kilos} Kg")
print(f"Preço Total: R$ {preco}")
print(f"Tipo de Pagamento: {tipopag}")
print(f"Valor do Desconto: R$ {desconto}")
print(f"Valor a Pagar: R$ {total}")