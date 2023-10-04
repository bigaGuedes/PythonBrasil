#Ex14
#Faça um programa que lê as duas notas parciais obtidas por um aluno
#numa disciplina ao longo de um semestre, e calcule a sua média.
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
#e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota01 = float(input("Insira a primeira nota parcial do aluno: "))
nota02 = float(input("Insira a segunda nota parcial do aluno: "))

media = (nota01 + nota02) / 2

if media >= 9 :
    print(f"Nota 01: {nota01}")
    print(f"Nota 02: {nota02}")
    print(f"Média: {media}")
    print("Conceito: A")
    print("Resultado: APROVADO")
elif media >=7.5 and media < 9 :
    print(f"Nota 01: {nota01}")
    print(f"Nota 02: {nota02}")
    print(f"Média: {media}")
    print("Conceito: B")
    print("Resultado: APROVADO")
elif media >= 6 and media < 7.5 :
    print(f"Nota 01: {nota01}")
    print(f"Nota 02: {nota02}")
    print(f"Média: {media}")
    print("Conceito: C")
    print("Resultado: APROVADO")
elif media >= 4 and media < 6 :
    print(f"Nota 01: {nota01}")
    print(f"Nota 02: {nota02}")
    print(f"Média: {media}")
    print("Conceito: D")
    print("Resultado: REPROVADO")
else :
    print(f"Nota 01: {nota01}")
    print(f"Nota 02: {nota02}")
    print(f"Média: {media}")
    print("Conceito: D")
    print("Resultado: REPROVADO")