#Ex11
#As Organizações Tabajara resolveram dar um aumento de salário aos seus
#colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste
#segundo o seguinte critério, baseado no salário atual:

#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

si = float(input("Por favor, insira o atual salário do colaborador: "))

#Percentual de Aumento Aplicado
paa01 = "20%"
paa02 = "15%"
paa03 = "10%"
paa04 = "5%"

#Valor do Aumento
va01 = si * 0.2
va02 = si * 0.15
va03 = si * 0.1
va04 = si * 0.05

#Novo Salário
if si <=280 :
    print(f"Salário Anterior ao Reajuste: {si}")
    print(f"Percentual de Aumento Aplicado: {paa01}")
    print(f"Valor do Aumento: R$ {va01}")
    print(f"Novo Salário: R$ {si * 1.2}")

if si > 280 and si <= 700 :
    print(f"Salário Anterior ao Reajuste: {si}")
    print(f"Percentual de Aumento Aplicado: {paa02}")
    print(f"Valor do Aumento: R$ {va02}")
    print(f"Novo Salário: R$ {si * 1.15}")

if si > 700 and si <= 1500 :
    print(f"Salário Anterior ao Reajuste: {si}")
    print(f"Percentual de Aumento Aplicado: {paa03}")
    print(f"Valor do Aumento: R$ {va03}")
    print(f"Novo Salário: R$ {si * 1.1}")

if si > 1500 :
    print(f"Salário Anterior ao Reajuste: {si}")
    print(f"Percentual de Aumento Aplicado: {paa04}")
    print(f"Valor do Aumento: R$ {va04}")
    print(f"Novo Salário: R$ {si * 1.05}")