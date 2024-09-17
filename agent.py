import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "searching"  # El estado puede ser "searching" o "returning"

    def move_randomly(self, board, blue_agent):
        if self.state == "searching":
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                new_x, new_y = self.x + dx, self.y + dy

                # Verifica si el nuevo movimiento es válido
                if board.is_within_bounds(new_x, new_y):
                    # Permite movimiento hacia el objetivo, incluso si es verde
                    if board.grid[new_x, new_y] == 0 or (new_x == board.goal_position[0] and new_y == board.goal_position[1]):
                        if not (new_x == blue_agent.x and new_y == blue_agent.y):  # Restricción
                            self.x, self.y = new_x, new_y
                            break



    def move_towards(self, target_x, target_y):
        if self.x < target_x:
            self.x += 1
        elif self.x > target_x:
            self.x -= 1
        elif self.y < target_y:
            self.y += 1
        elif self.y > target_y:
            self.y -= 1

    def update(self, board, goal_x, goal_y, blue_agent):
        if self.state == "searching":
            self.move_randomly(board, blue_agent)
            if self.x == goal_x and self.y == goal_y:
                self.state = "returning"
        elif self.state == "returning":
            self.move_towards(blue_agent.x, blue_agent.y)
            if self.x == blue_agent.x and self.y == blue_agent.y:
                # El agente rojo ha alcanzado al agente azul
                return True  # Se puede usar esta señal para indicar que el juego debe finalizar
        return False

