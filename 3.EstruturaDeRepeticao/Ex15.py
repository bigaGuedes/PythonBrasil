#Ex15
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.

num = int(input('\nInsira o termo desejado: '))

ultNum = 1
penNum = 1

sequenciaLista = [1, 1]

while ultNum < num:
    novoNum = ultNum + penNum
    sequenciaLista.append(novoNum)
    penNum = ultNum
    ultNum = novoNum

print(f'\nUsando o termo de valor [{num}] como limite, a sequência gerada é: {sequenciaLista}\n')