#Ex25
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

opNumPessoas = int(input('\nInsira o número de alunos: '))

alunos = []

for pessoa in range(opNumPessoas):
    idade = int(input(f'Insira a idade do {pessoa +1}º aluno: '))
    alunos.append(idade)

media = sum(alunos) / len(alunos)

if media > 0 and media <=25:
    print('\nEssa é uma turma jovem!')

elif media > 25 and media <=60:
    print('\nEssa é uma turma adulta!')

else:
    print('\nEssa é uma turma idosa!')