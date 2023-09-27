#Ex18
#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe o
#tempo aproximado de download do arquivo usando este link (em minutos).

ta = float(input("Tamanho do arquivo a ser baixado (MB): "))
vi = float(input("Velocidade da sua internet (Mbps): "))

td = ta / vi / 60
print("\nTempo aproximado de download:",td, "min")