#Ex20
#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota01 = float(input("Insira a primeira nota: "))
nota02 = float(input("Insira a primeira nota: "))
nota03 = float(input("Insira a primeira nota: "))

media = (nota01 + nota02 + nota03) / 3

if media == 10 :
    print(f"Aprovado com Distinção! Média: {media}")
elif media >= 7:
    print(f"Aprovado! Média: {media}")
else : print(f"Reprovado. Média: {media}")
