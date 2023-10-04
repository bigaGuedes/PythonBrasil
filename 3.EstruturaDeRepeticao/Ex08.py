#Ex08
#Faça um programa que leia 5 números e informe a soma e a média dos números.

while True:
    nums = list(map(float, input("Insira 5 números: ").split()))
    if len(nums) < 5 or len(nums) > 5:
        print("\nPor favor, informe 5 números.")
        continue
    else:
        soma = sum(nums)
        media = soma / 5
        print(f"Soma: {soma}")
        print(f"Média: {media}")
    break