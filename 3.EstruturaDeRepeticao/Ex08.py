#Ex08
#Faça um programa que leia 5 números e informe o maior número.

while True:
    nums = list(map(float, input("Insira 5 (cinco) números: ").split()))
    if len(nums) < 5:
        print("\nMenos de 5 números informados. Tente novamente.")
        continue
    else: print(f"O maior número da lista é: {max(nums)}")
    break