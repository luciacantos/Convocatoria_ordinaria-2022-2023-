#Ejercicio 7

from collections import deque
#Un objeto deque es un contenedor de datos del módulo collections similar a una lista o una cola que
#permite añadir o suprimir elementos por sus dos extremos.

def caballo(inicial, final):
    # convertir las posiciones de notación algebraica a coordenadas (fila, columna)
    inicial_pos = (8 - int(inicial[1]), ord(inicial[0]) - ord('a'))
    final_pos = (8 - int(final[1]), ord(final[0]) - ord('a'))

 # crear una lista de movimientos del caballo
    movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
