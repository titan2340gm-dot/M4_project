import random
from app_logic import play_game, check_winner
from utils import human_turn, computer_turn

def start game():
    sticks=21
    turn =input("Хотите ходить первыми? (да/нет): ").strip().lower()
    if turn=="да":
        human_first=True
    else:
        human_first=False
    play_game(human_first,sticks)
    
start_game()
