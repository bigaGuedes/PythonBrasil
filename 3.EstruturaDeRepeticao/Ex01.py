#Ex01
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    num = int(input("Insira uma nota entre 0 e 10: "))
    if 0 > num or 10 < num:
        print("Valor inválido. Tente novamente.\n")
        continue
    else:
        break

