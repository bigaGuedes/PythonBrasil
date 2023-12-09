#Ex36
# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário.

while True:

    num = int(input('\nMontar a tabuada de: '))
    comeco = int(input('Começar por: '))
    fim = int(input('Terminar em: '))

    if comeco > fim:
        print(f'\nO valor de término ({fim}) é menor que o de começo ({comeco}). Tente novamente.')
        continue

    else:
        print(f'\nVou montar a tabuada de {num}, começando em {comeco} e terminando em {fim}:\n')

        for i in range(comeco, fim+1):
            multNum = num * i
            print(f'{num} x {i} = {multNum}')
    
    break