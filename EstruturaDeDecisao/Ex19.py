#Ex19
#Faça um Programa que leia um número inteiro menor que 1000 e
#imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades
#Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input("Insira um número menor que 1000: "))

ctn = int(numero / 100)
dzn = int((numero - ctn * 100) / 10)
uni = int(numero - ((ctn * 100) + (dzn * 10)))

if numero >= 0 and numero < 1000:
    if ctn == 0 and dzn == 0:
        print(f"{numero} = {uni} unidade(s).")
    elif ctn == 0 and dzn >= 1 and uni == 0:
        print(f"{numero} = {dzn} dezena(s).")
    elif ctn == 0 and dzn >= 1:
        print(f"{numero} = {dzn} dezena(s) e {uni} unidade(s).")
    elif ctn >= 1 and dzn == 0 and uni == 0:
        print(f"{numero} = {ctn} centena(s).")
    elif ctn >= 1 and dzn >= 1 and uni == 0:
        print(f"{numero} = {ctn} centena(s) e {dzn} dezena(s).")
    elif ctn >= 1 and dzn == 0 and uni >= 1:
        print(f"{numero} = {ctn} centena(s) e {uni} unidade(s).")           
    elif ctn >= 1:
        print(f"{numero} = {ctn} centena(s), {dzn} dezena(s) e {uni} unidade(s).")
else: print("Número inválido.")      