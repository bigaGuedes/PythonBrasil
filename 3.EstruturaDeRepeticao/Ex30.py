#Ex30
# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,

preco = 0.18

print('\nPanificador Pão de Ontem - Tabela de Preços\n')

for i in range(50):
    novoPreco = round((preco * (i+1)), 2)
    print(f'{i+1} - {novoPreco}')