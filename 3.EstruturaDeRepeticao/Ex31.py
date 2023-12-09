#Ex31
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

caixa = []

while True:

    count = 1

    print('\nLojas Tabajara\n')

    while count > 0:

        valor = float(input(f'Produto {count}: R$ '))

        if valor == 0:
            break

        else:
            caixa.append(valor)

        count += 1

    total = sum(caixa)
    print(f'\nTotal: {total}')

    while True:

        pago = float(input('Dinheiro: R$ '))

        if pago == total:
            print('Troco: R$ 0.00')

        elif pago < total:
            print('\nValor insuficiente. Tente novamente.\n')
            continue

        else:
            troco = pago - total
            print(f'Troco: R$ {troco}\n')
        
        break
