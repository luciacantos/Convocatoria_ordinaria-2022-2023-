#Ejercicio 3

def numero_letras(n):
    #escribir la palabra de cada número en inglés para contar en nº de letras en una lista
    valores = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    #lista vacía para añadir el resultado
    resultado = []
    while n != 4: #4 es el único número que su palabra tiene el mismo número de letras que su valor
        palabra = ""
        cont = n
        while cont > 0:
            palabra += valores[cont % 10]
            cont = cont // 10
        resultado.append(palabra)
        n = len(palabra)
    resultado.append("four")
    return resultado

if __name__ == "__main__":
    print("[60] ->",numero_letras(60))
    print("[1] ->",numero_letras(1))
