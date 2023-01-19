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

    #Calcular la longitud máxima de la cuerda
    longitud_max = 2 * math.pi * radio * (1 - math.sqrt(1 - area_max / area))

    #Redondear paar tener la longitud como un número entero
    return round(longitud_max)

if __name__ == "__main__":
    diametro = 10
    porcentaje = 50
    print("La longitud máxima de la cuerda es",max_cuerda(diametro, porcentaje),"pasos de ogro.")
