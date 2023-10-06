#Ex12
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

while True:
    num = float(input("Insira um número: "))   
    if round(num) != num:
        print("Por favor, insira um número inteiro.\n")
        continue
    else:
        num = int(num)
        print(f"\nTabuada de {num}:\n")
        for mult in range(1,11):
            print(f"{num} x {mult} = {num * mult}")
    break