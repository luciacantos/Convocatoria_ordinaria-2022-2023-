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

# matriz de 8x8 que representa el tablero de ajedrez
    tablero = [[-1] * 8 for _ in range(8)]
    tablero[inicial_pos[0]][inicial_pos[1]] = 0

# cola de búsqueda
    queue = deque([inicial_pos])

    while queue: #movimer el caballo hasta que llegue a la posición final
        pos = queue.popleft()
        for mover in movimientos:
            x, y = pos[0] + mover[0], pos[1] + mover[1]
            if 0 <= x < 8 and 0 <= y < 8 and tablero[x][y] == -1:
                tablero[x][y] = tablero[pos[0]][pos[1]] + 1
                queue.append((x, y))
                if (x, y) == final_pos:
                    return tablero[x][y]
    return -1
