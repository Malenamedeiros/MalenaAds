_, dia_i = input().split() 
hora_i, min_i, seg_i = map(int, input().split(" : "))
_, dia_f = input().splir()
hora_f, min_f, seg_f = map(int, input().split(" : "))

dia_i = int(dia_i)
dia_f = int(dia_f)

dias = dia_f - dia_i
horas = hora_f - hora_i
minutos = min_f - min_i
segundos = seg_f - seg_i

if segundos < 0:
    segundos = segundos + 60
    minutos = minutos - 1

if minutos < 0:
    minutos = minutos + 60
    horas = horas - 1

if horas < 0:
    horas = horas + 24
    dias = dias -1

print (f"{dias:.0f} dia(s)")
print(f{horas:.0f} hora(s))
print(f"{minutos:.0f} minuto(s)")
print(f"{segundos:.0f} segudo(s)")



