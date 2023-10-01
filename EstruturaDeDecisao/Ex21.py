#Ex21
#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Que quantia você gostaria de sacar? "))
print (f"Saque solicitado: R$ {saque}")

if saque < 10 :
    print("Valor insuficiente para realizar saque")
    print("Valor mínimo para saque: R$ 10")
elif saque > 600 :
    print("Valor excede o limite para realizar saque")
    print("Valor máximo para saque: R$ 600")
else :       
    cem = int(saque / 100)
    saque = int(saque - (cem * 100))
    cinq = int(saque / 50)
    saque = int(saque - (cinq * 50))
    dez = int(saque / 10)
    saque = int(saque - (dez * 10))
    cinc = int(saque / 5)
    saque = int(saque - (cinc * 5))
    um = saque

    if cem > 0 :
        print(f"{cem} nota(s) de R$ 100")
    if cinq > 0 :
        print(f"{cinq} nota(s) de R$ 50")
    if dez > 0 :
        print(f"{dez} nota(s) de R$ 10")
    if cinc > 0 :
        print(f"{cinc} nota(s) de R$ 5")
    if um > 0 :
        print(f"{um} nota(s) de R$ 1")