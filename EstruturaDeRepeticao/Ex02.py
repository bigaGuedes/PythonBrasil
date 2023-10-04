#Ex02
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("Insira o Nome de Usuário: ").lower()
senha = input("Insira a Senha: ").lower()

while senha == user:
    print("A senha é igual ao Nome de Usuário! Por favor, insira uma senha diferente.")
    senha = input("Insira a Senha: ").lower()