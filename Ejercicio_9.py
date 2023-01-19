#Ejercicio 9

import datetime

def numero_lunes(cumpleaños, fecha_actual):
    # calcular edad
    edad = fecha_actual.year - cumpleaños.year - ((fecha_actual.month, fecha_actual.day) < (cumpleaños.month, cumpleaños.day))
    if edad < 22 or edad > 78: #los lunes no cuentan si no estás en edad laboral
        return 0
    else:
        #calcular la cantidad de días que ha pasado desde que cumple los 22 y entra en edad de trabajar
        años_trabajo = min(78, edad) - 22
        dias_trabajo = años_trabajo * 365
        fecha_inicio = cumpleaños + datetime.timedelta(days=22*365)
        fecha_fin = fecha_inicio + datetime.timedelta(days=dias_trabajo)
        lunes = 0
        dia_actual = fecha_inicio
        while dia_actual <= fecha_fin:
            if dia_actual.weekday() == 0:
                lunes += 1
            dia_actual += datetime.timedelta(days=1)
        return lunes
