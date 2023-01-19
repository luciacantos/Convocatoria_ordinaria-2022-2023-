#Ejercicio 5

def hollow_triangle(altura): #devuelve un triángulo hueco de la altura indicada
    triangulo = []

    for i in range(1, altura+1): #dibujar el triángulo
        line = '_'*(altura-i) + '#'
        if i > 1:
            line += '_'*(2*i-3) + '#'
        line += '_'*(altura-i)
        triangulo.append(line)
    triangulo.append('#'*(2*altura-1))
    return triangulo

if __name__ == '__main__':
    h = 9
    print(*hollow_triangle(h), sep='\n')
    print("---- Final Height")

    c = 6
    print(*hollow_triangle(c), sep='\n')
    print("---- Final Height")
