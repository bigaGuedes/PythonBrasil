#Ex13
# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.


base = int(input("Insira a base: "))
expo = int(input("Insira o expoente: "))
potencia = 1

for num in range(expo):
    potencia *= base

print(f"Resultado: {potencia}")
