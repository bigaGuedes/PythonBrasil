#Ex04
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Insira uma letra: ")

if letra.isalpha():
    if letra == "a" or letra == "A":
        print("A letra inserida é uma vogal.")
    elif letra == "e" or letra == "E":
        print("A letra inserida é uma vogal.")
    elif letra == "i" or letra == "I":
        print("A letra inserida é uma vogal.")
    elif letra == "o" or letra == "O":
        print("A letra inserida é uma vogal.")
    elif letra == "u" or letra == "U":
        print("A letra inserida é uma vogal.")
    else:
        print("A letra inserida é uma consoante.")
else:
    print("Você não inseriu uma letra!")       