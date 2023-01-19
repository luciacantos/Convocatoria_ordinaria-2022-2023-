#Ejercicio 9

import datetime

def numero_lunes(cumpleaños, fecha_actual):
    # calcular edad
    edad = fecha_actual.year - cumpleaños.year - ((fecha_actual.month, fecha_actual.day) < (cumpleaños.month, cumpleaños.day))
