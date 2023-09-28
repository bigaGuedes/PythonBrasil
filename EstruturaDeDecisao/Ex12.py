#Ex12
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
#descontos são do Imposto de Renda, que depende do salário bruto
#(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
#a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade
#de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%

vh = float(input("Informe o valor da hora: "))
ht = float(input("Informe a quantidade de horas trabalhadas no mês: "))

sb = vh * ht
SIND = sb * 0.03

if sb <= 900 :
    print(f"Salário Bruto: R$ {sb}")
    IR = 0
    print(f"Imposto de Renda (Isento): R$ {IR}")
    print(f"Contribuição Sindical (3%): R$ {SIND}")
    FGTS = sb * 0.11
    print(f"FGTS (11%): R$ {FGTS}")
    dt = IR + SIND
    print(f"Descontos Totais: R$ {dt}")
    print(f"Salário Líquido: R$ {sb - dt}")

if sb > 900 and sb <= 1500 :
    print(f"Salário Bruto: R$ {sb}")
    IR = sb * 0.05
    print(f"Imposto de Renda (5%): R$ {IR}")
    print(f"Contribuição Sindical (3%): R$ {SIND}")
    FGTS = sb * 0.11
    print(f"FGTS (11%): R$ {FGTS}")
    dt = IR + SIND
    print(f"Descontos Totais: R$ {dt}")
    print(f"Salário Líquido: R$ {sb - dt}")

if sb > 1500 and sb <= 2500 :
    print(f"Salário Bruto: R$ {sb}")
    IR = sb * 0.1
    print(f"Imposto de Renda (10%): R$ {IR}")
    print(f"Contribuição Sindical (3%): R$ {SIND}")
    FGTS = sb * 0.11
    print(f"FGTS (11%): R$ {FGTS}")
    dt = IR + SIND
    print(f"Descontos Totais: R$ {dt}")
    print(f"Salário Líquido: R$ {sb - dt}")

if sb > 2500 :
    print(f"Salário Bruto: R$ {sb}")
    IR = sb * 0.2
    print(f"Imposto de Renda (20%): R$ {IR}")
    print(f"Contribuição Sindical (3%): R$ {SIND}")
    FGTS = sb * 0.11
    print(f"FGTS (11%): R$ {FGTS}")
    dt = IR + SIND
    print(f"Descontos Totais: R$ {dt}")
    print(f"Salário Líquido: R$ {sb - dt}")    



