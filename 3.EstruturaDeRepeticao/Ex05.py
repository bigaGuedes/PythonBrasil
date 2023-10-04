#Ex05
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

print("\nCálculo de crescimento populacional.")
print("Insira 2 (duas) populações e 2 (duas) taxas de crescimento.\n")
print("Obs: Para realizar a operação, a taxa de crescimento da menor população precisa ser maior.\n")

ano = 0

while True:
    pop1 = float(input("Informe a população do país com maior taxa de crescimento: "))
    taxapop1 = float(input("Informe a taxa de crescimento populacional do país acima: "))
    pop2 = float(input("Informe a população do segundo país: "))
    taxapop2 = float(input("Informe a taxa de crescimento populacional do país acima: "))

    if pop1 > pop2:
        print("Impossível calcular: a população do primeiro país já é maior.")
        print("Tente novamente.\n")
        continue
    elif taxapop1 < taxapop2:
        print("Impossível calcular: a taxa de crescimento populacional do primeiro país é menor.")
        print("Tente novamente.\n")
        continue
    else: 
        while pop1 <= pop2:
            pop1 += pop1 * (taxapop1 * 0.01)
            pop2 += pop2 * (taxapop2 * 0.01)
            ano += 1
        print(f"A população do primeiro país vai ultrapassar a do segundo em {ano} anos.")
        break


