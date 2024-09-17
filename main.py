from board import Board
from agent import Agent
from gui import GameGUI

def main():
    board = Board()
    board.set_goal(0, 4)
    board.set_obstacle(5, 5)
    
    agent1 = Agent(0, 0)
    agent2 = Agent(3, 2)
    
    game_gui = GameGUI(board, agent1, agent2)
    
    while True:
        game_gui.handle_events()
        game_gui.update()

if __name__ == "__main__":
    main()
