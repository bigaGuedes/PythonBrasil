# Ex27
# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = []

qtTurmas = int(input('\nInsira a quantidade de turmas: '))

for i in range(qtTurmas):
    
    qtAlunos = int(input(f'Insira a quantidade de alunos na {i+1}º turma: '))

    while True: 
        
        if qtAlunos > 40:
            print('\nQuantidade excede o limite máximo de alunos (40). Tente novamente.\n')
            qtAlunos = int(input(f'Insira a quantidade de alunos na {i+1}º turma: '))
            continue
    
        elif qtAlunos <= 40:
            turmas.append(qtAlunos)
    
        break

media = sum(turmas) / len(turmas)

print(f'\nA média de alunos por turma é igual a {media}')