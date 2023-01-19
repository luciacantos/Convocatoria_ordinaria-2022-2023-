# Ejercicio 3

def numero_letras(n):
    #escribir la palabra de cada número en inglés para contar en nº de letras en una lista
    valores = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    #lista vacía para añadir el resultado
    resultado = []

    while n != 4: #4 es el único número que su palaabra tiene el mismo número de letras que su valor
        palabra = ""
        cont = n
        
