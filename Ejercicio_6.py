# Ejercicio 6

import math

def max_cuerda(diametro, porcentaje): #calcular la máxima longitud de la cuerda

    #Calcular el radio del parche circular de hierba
    radio = diametro / 2

    #Calcular el área del parche
    area = math.pi * (radio ** 2)

    #Calcular el área máxima que el burro puede acceder
    porcentaje = porcentaje / 100
    area_max = area * porcentaje
