hora_i, min_i = map(int, input().split(":"))
hora_f, min_f = map(int, input().split(":"))

hora = hora_f - hora_i
minutos = hora * 60
minu = mini_f - min_i


    
if tempo <= 15:
    print("Gratis")
elif tempo >= 15:
    print("Valor a pagar: R$ 2,00")
elif tempo >= 60:
    print("Valor a pagar: R$ 3,00")
    




