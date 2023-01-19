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
