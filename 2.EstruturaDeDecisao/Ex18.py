#Ex18
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("Insira uma data no formato dd/mm/aaaa.")
dd = int(input("Insira o dia: "))
mm = int(input("Insira o mês: "))
aaaa = int(input("Insira o ano: "))

check = False

if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
    if (dd <= 31 and dd > 0):
        check = True
elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
    if (dd <= 30 and dd > 0):
        check = True
elif (mm == 2):
    if (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 400 == 0):
        if (dd <= 29 and dd > 0):
            check = True
    elif (dd <= 28 and dd > 0):
        check = True

if(check and (aaaa > 0 and aaaa < 9999)):
    print("Data Válida.")
else:
    print("Data Inválida.")