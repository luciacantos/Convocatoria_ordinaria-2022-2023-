#Ejercicio 10

def xbonacci(firma, n): #devuelve una lista con los n primeros números de la secuencia de Fibonacci
    secuencia = firma[:n]
    for i in range(n-len(firma)):
        secuencia.append(sum(secuencia[-len(firma):]))
    return secuencia

if __name__ == "__main__":
    print("xbonacci {1,1,1,1} 10 =",xbonacci([1,1,1,1], 10))
    print("xbonacci {0,0,0,0,1} 10 =",xbonacci([0,0,0,0,1], 10))
    print("xbonacci {1,0,0,0,0,0,1} 10 =",xbonacci([1,0,0,0,0,0,1], 10))
