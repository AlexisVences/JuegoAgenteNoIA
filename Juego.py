import tkinter as tk
import random

# Crear la ventana principal
root = tk.Tk()
root.title("Juego con Movimiento Aleatorio")

# Tamaño del tablero
SIZE = 10
CELL_SIZE = 50

# Crear el lienzo para dibujar el tablero
canvas = tk.Canvas(root, width=SIZE * CELL_SIZE, height=SIZE * CELL_SIZE)
canvas.pack()

# Posiciones iniciales del jugador y del objetivo
player_position = [0, 0]
goal_position = [random.randint(0, SIZE-1), random.randint(0, SIZE-1)]

# Dibujar el tablero y los elementos
def draw_board():
    canvas.delete("all")  # Limpiar el lienzo
    for row in range(SIZE):
        for col in range(SIZE):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")
    # Dibujar al jugador
    px, py = player_position
    canvas.create_rectangle(px * CELL_SIZE, py * CELL_SIZE,
                            (px + 1) * CELL_SIZE, (py + 1) * CELL_SIZE,
                            fill="blue")

    # Dibujar el objetivo
    gx, gy = goal_position
    canvas.create_rectangle(gx * CELL_SIZE, gy * CELL_SIZE,
                            (gx + 1) * CELL_SIZE, (gy + 1) * CELL_SIZE,
                            fill="red")

# Movimiento aleatorio de un objeto en el tablero
def move_randomly(position):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Abajo, Arriba, Derecha, Izquierda
    move = random.choice(directions)
    new_x = position[0] + move[0]
    new_y = position[1] + move[1]

    # Asegurarse de que el movimiento esté dentro del tablero
    if 0 <= new_x < SIZE and 0 <= new_y < SIZE:
        position[0] = new_x
        position[1] = new_y

# Actualizar la posición del jugador y del objetivo aleatoriamente
def update_positions():
    move_randomly(player_position)
    move_randomly(goal_position)
    
    # Comprobar si el jugador ha alcanzado el objetivo
    if player_position == goal_position:
        canvas.create_text(SIZE * CELL_SIZE // 2, SIZE * CELL_SIZE // 2, text="¡Ganaste!", font=("Arial", 24), fill="green")
        return
    
    draw_board()
    root.after(1000, update_positions)  # Actualizar posiciones cada 1000 ms (1 segundo)

# Dibujar el tablero inicial
draw_board()

# Iniciar la actualización automática de posiciones
root.after(1000, update_positions)

# Iniciar el bucle principal
root.mainloop()
