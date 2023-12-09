#Ex37
# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

altAlunos = {}
pesoAlunos = {}
alturaTotal = []
pesoTotal = []

while True:
    
    codAluno = int(input('\nInsira seu código (ou digite 0 para encerrar): '))

    if codAluno == 0:
        break

    altura = float(input('Insira a sua altura em cm: '))
    peso = float(input('Insira o seu peso em kg: '))

    altAlunos[codAluno] = altura
    alturaTotal.append(altura)
    pesoAlunos[codAluno] = peso
    pesoTotal.append(peso)

    print('\nObrigado! Dados registrados com sucesso.')

if alturaTotal:
    codMaisAlto = max(altAlunos, key=altAlunos.get)
    codMaisBaixo = min(altAlunos, key=altAlunos.get)
    maisAlto = altAlunos[codMaisAlto]
    maisBaixo = altAlunos[codMaisBaixo]
    mediaAltura = sum(alturaTotal) / len(alturaTotal)

else:
    maisAlto = maisBaixo = mediaAltura = 0

if pesoTotal:
    codMaisGordo = max(pesoAlunos, key=pesoAlunos.get)
    codMaisMagro = min(pesoAlunos, key=pesoAlunos.get)
    maisGordo = pesoAlunos[codMaisGordo]
    maisMagro = pesoAlunos[codMaisMagro]
    mediaPeso = sum(pesoTotal) / len(pesoTotal)

else:
    maisGordo = maisMagro = mediaPeso = 0

print('\n##################')
print('\nCenso | Academia Sem Noção\n')
print(f'Cliente mais alto: Código {codMaisAlto} | Altura: {maisAlto}cm')
print(f'Cliente mais baixo: Código {codMaisBaixo} | Altura: {maisBaixo}cm')
print(f'Cliente mais gordo: Código {codMaisGordo} | Peso: {maisGordo}kg')
print(f'Cliente mais magro: Código {codMaisMagro} | Peso: {maisMagro}kg')
print(f'Média de altura entre os alunos: {round(mediaAltura, 2)}cm')
print(f'Média de peso entre os alunos: {round(mediaPeso, 2)}kg\n')
