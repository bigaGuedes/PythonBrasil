#Ex07
#Faça um programa que leia 5 números e informe o maior número.

while True:
    nums = list(map(float, input("Insira 5 (cinco) números: ").split()))
    if len(nums) < 5 or len(nums) > 5:
        print("\nPor favor, informe 5 números.")
        continue
    else: print(f"O maior número da lista é: {max(nums)}")
    break