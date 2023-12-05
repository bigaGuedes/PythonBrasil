#Ex20
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    
    print('\nGostaria de calcular o fatorial?')
    opSistema = input('Digite: [S] para SIM e [N] para NÃO: ').upper()
    
    if opSistema == 'S':
        
        while True: 
            
            num = int(input('\nInsira um número inteiro, positivo e menor que 16: '))

            if num < 0 or num > 16:
                print('\nNúmero inválido. Tente novamente.')
                continue

            else:
                contador = 1
                resultado = 1

                while contador <= num:
                    resultado *= contador
                    contador += 1
            
            print(f'\nO fatorial de {num} é {resultado}.\n')
            break
    
    elif opSistema == 'N':
        print('\nObrigado por utilizar nosso sistema!\n')
        exit()
    
    else:
        print('\Resposta inválida. Tente novamente.\n')
        continue



