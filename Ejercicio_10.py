#Ejercicio 10

def xbonacci(firma, n): #devuelve una lista con los n primeros números de la secuencia de Fibonacci
    secuencia = firma[:n]
    for i in range(n-len(firma)):
        secuencia.append(sum(secuencia[-len(firma):]))
    return secuencia
