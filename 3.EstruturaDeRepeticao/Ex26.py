#Ex26
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print('\nBem-vind@ as eleições!')
print('Candidatos: Zezim da Feira [10] | Maria do Carro [20] | João Gasteiro [30]\n')

opNumEleitores = int(input('Insira o número de eleitores: '))

votosZezim = 0
votosMaria = 0
votosJoao = 0
votosNulos = 0

for eleitores in range(opNumEleitores):

    voto = input('Insira o seu voto: ')

    if voto == '10':
        votosZezim += 1
        
    elif voto == '20':
        votosMaria += 1
        
    elif voto == '30':
        votosJoao += 1
        
    else:
        votosNulos +=1
    
print('\nResultados | Votação\n')
print(f'Zezim da Feira | Votos: {votosZezim}')
print(f'Maria do Carro | Votos: {votosMaria}')
print(f'João Gasteiro | Votos: {votosJoao}\n')

if votosZezim > votosMaria and votosZezim > votosJoao:
    print(f'Zezim da Feira eleito!\n')

elif votosMaria > votosZezim and votosMaria > votosJoao:
    print(f'Maria do Carro eleita!\n')

elif votosJoao > votosZezim and votosJoao > votosMaria:
    print(f'João Gasteiro eleito!\n')

