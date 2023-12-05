#Ex16
# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

ultNum = 1
penNum = 1

sequenciaLista = [1, 1]

while ultNum < 500:
    novoNum = ultNum + penNum
    sequenciaLista.append(novoNum)
    penNum = ultNum
    ultNum = novoNum

print(f'\nUsando o valor [500] como limite, a sequência gerada é: {sequenciaLista}\n')