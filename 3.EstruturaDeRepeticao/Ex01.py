#Ex01
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = int(input("Digite um número de 0 a 10: "))
while 0 > num or 10 < num:
    num = int(input("Digite um número de 0 a 10: "))
