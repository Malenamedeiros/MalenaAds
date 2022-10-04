#GASTO DE COMBUSTIVEL
#CONSUMO = 12KM/L

#ler o tempo de viagem e velocidade media.
horas = int(input())
velocidade = int(input())
#Calcular a KM total da viagem.
km_total = horas * velocidade
consumo = km_total / 12
#Calcular o consumo total, sabendo q são 12 KM/L e imprimir com 3 casas decimais.
print(f'{consumo:.3f}')