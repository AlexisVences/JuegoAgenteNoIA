import numpy as np

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.goal_position = None

    def set_obstacle(self, x, y):
        if self.is_within_bounds(x, y):
            self.grid[x, y] = 1

    def set_goal(self, x, y):
        if self.is_within_bounds(x, y):
            self.goal_position = (x, y)
            self.grid[x, y] = 2

    def is_within_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def __str__(self):
        return str(self.grid)
