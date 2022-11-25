import time

# obtenemos:
# (i) fecha y hora actual
# (ii) HORA ACTUAL: hora y minutos
actual = time.localtime()
hora_y_fecha = time.strftime("%a, %d %b %Y %H:%M:%S",actual)
horas_entero = int(time.strftime("%H",actual))
minutos_entero = int(time.strftime("%M",actual))

# verificamos si la hora actual es igual o superior a las 19 h
def horarioLaboral(hora):
    if hora >= 19:
        laboral = False
    else:
        laboral = True
    return laboral

# mensaje según la hora actual
def que_mensaje(laboral, h, m):
    if laboral == True:
        tiempo_restante = ((19 - h) * 60) - m
        h_restantes = str(tiempo_restante // 60)
        m_restantes = str(tiempo_restante % 60)
        mensaje = ("Falta: " + h_restantes + ":" + m_restantes)
    else:
        mensaje = "Es hora de ir a casa"
    return mensaje

laboral = horarioLaboral(horas_entero)
mensaje = que_mensaje(laboral, horas_entero, minutos_entero)

print("Fecha y hora: " + hora_y_fecha)
print(mensaje)
