import pygame
from pygame.locals import *

class GameGUI:
    def __init__(self, board, agent1, agent2):
        pygame.init()
        self.board = board
        self.agent1 = agent1
        self.agent2 = agent2
        self.screen_size = 600
        self.cell_size = self.screen_size // board.size
        self.button_height = 50
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size + 2 * self.button_height))
        pygame.display.set_caption('Simple Game')

        self.start_button = pygame.Rect(0, self.screen_size + self.button_height, self.screen_size // 2, self.button_height)
        self.obstacle_button = pygame.Rect(self.screen_size // 2, self.screen_size + self.button_height, self.screen_size // 2, self.button_height)

        self.start_button_color = (255, 0, 0)
        self.obstacle_button_color = (0, 0, 255)
        self.button_text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)

        self.game_started = False
        self.place_obstacles_mode = False

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for x in range(self.board.size):
            for y in range(self.board.size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                color = (0, 0, 0) if self.board.grid[x, y] == 1 else (0, 255, 0) if self.board.grid[x, y] == 2 else (255, 255, 255)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.agent1.x * self.cell_size + self.cell_size // 2, self.agent1.y * self.cell_size + self.cell_size // 2), self.cell_size // 4)
        pygame.draw.circle(self.screen, (0, 0, 255), (self.agent2.x * self.cell_size + self.cell_size // 2, self.agent2.y * self.cell_size + self.cell_size // 2), self.cell_size // 4)
        
        if not self.game_started:
            self.draw_start_button()
            self.draw_obstacle_button()

        pygame.display.flip()

    def draw_start_button(self):
        pygame.draw.rect(self.screen, self.start_button_color, self.start_button)
        text_surface = self.font.render('Start Game', True, self.button_text_color)
        text_rect = text_surface.get_rect(center=self.start_button.center)
        self.screen.blit(text_surface, text_rect)

    def draw_obstacle_button(self):
        pygame.draw.rect(self.screen, self.obstacle_button_color, self.obstacle_button)
        text_surface = self.font.render('Place Obstacles', True, self.button_text_color)
        text_rect = text_surface.get_rect(center=self.obstacle_button.center)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                pos = event.pos
                if not self.game_started:
                    if self.start_button.collidepoint(pos):
                        self.game_started = True
                    elif self.obstacle_button.collidepoint(pos):
                        self.place_obstacles_mode = not self.place_obstacles_mode
                if self.place_obstacles_mode and not self.game_started:
                    # Verifica si el clic está dentro del área del tablero
                    if pos[1] < self.screen_size:  # Asegúrate de que el clic esté en el área del tablero
                        # Ajusta las coordenadas del clic para el tablero
                        board_x = pos[0] // self.cell_size
                        board_y = pos[1] // self.cell_size
                        if self.board.is_within_bounds(board_x, board_y):
                            # Coloca un obstáculo en la celda correspondiente
                            self.board.set_obstacle(board_x, board_y)

    def draw_final_message(self):
        font = pygame.font.Font(None, 74)
        text_surface = font.render('FINAL', True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.screen_size // 2, self.screen_size // 2))
        self.screen.blit(text_surface, text_rect)


    def update(self):
        if self.game_started:
            game_over = self.agent1.update(self.board, self.board.goal_position[0], self.board.goal_position[1], self.agent2)
            if game_over:
                self.game_started = False
                self.draw_final_message()
            else:
                self.draw_board()
            pygame.time.delay(300)
        else:
            self.draw_board()
            pygame.time.delay(300)




