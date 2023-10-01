#Ex24
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
print("Que operação deseja realizar?")
op = input("Insira: +, -, * ou / : ")

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2 

if op == "+":
    if soma % 2 == 0:
        paridade = "Par"
    else: paridade = "Ímpar"
    if soma > 0:
        clasf = "Positivo"
    else: clasf = "Negativo"
    if soma == round(soma):
        tipo = "Inteiro"
    else: tipo = "Decimal"            
elif op == "-":
    if sub % 2 == 0:
        paridade = "Par"
    else: paridade = "Ímpar"
    if sub > 0:
        clasf = "Positivo"
    else: clasf = "Negativo"
    if sub == round(sub):
        tipo = "Inteiro"
    else: tipo = "Decimal"            
elif op == "*":
    if mult % 2 == 0:
        paridade = "Par"
    else: paridade = "Ímpar"
    if mult > 0:
        clasf = "Positivo"
    else: clasf = "Negativo"
    if mult == round(mult):
        tipo = "Inteiro"
    else: tipo = "Decimal"            
elif op == "/":
    if div % 2 == 0:
        paridade = "Par"
    else: paridade = "Ímpar"
    if div > 0:
        clasf = "Positivo"
    else: clasf = "Negativo"
    if div == round(div):
        tipo = "Inteiro"
    else: tipo = "Decimal"

if op == "+":
    print(f"Resultado: {soma} - {paridade}, {clasf} e {tipo}")
elif op == "-":
    print(f"Resultado: {sub} - {paridade}, {clasf} e {tipo}")
elif op == "*":
    print(f"Resultado: {mult} - {paridade}, {clasf} e {tipo}")
elif op == "/":
    print(f"Resultado: {div} - {paridade}, {clasf} e {tipo}")                  