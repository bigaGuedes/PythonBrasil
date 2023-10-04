#Ex03
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Insira o seu nome: ")
while len(nome) <= 3:
    print("Seu nome deve ter mais de 3 caracteres. Tente novamente: ")
    nome = input("Insira o seu nome: ")

idade = int(input("Insira a sua idade: "))
while (0 > idade) or (150 < idade):
    print("Sua idade precisa estar entre 0 e 150 anos. Tente novamente: ")
    idade = int(input("Insira a sua idade: "))

salario = float(input("Insira o seu salário: R$ "))
while 0 > salario:
    print("Seu salário precisa ser maior que zero. Tente novamente: ")
    salario = float(input("Insira o seu salário: R$ "))

sexo = input("Sexo: 'f' para feminino ou 'm' para masculino: ")
while (sexo != 'f') and (sexo != 'm'):
    print("Tente novamente: ")
    sexo = input("Sexo: 'f' para feminino ou 'm' para masculino: ")

estadoc = input("Insira seu Estado Civil. Escolha entre 's', 'c', 'v' ou 'd': ")
while (estadoc != 's') and (estadoc != 'c') and (estadoc != 'v') and (estadoc != 'd'):
    print("Valor inválido. Tente novamente: ")
    estadoc = input("Insira seu Estado Civil. Escolha entre 's', 'c', 'v' ou 'd': ")