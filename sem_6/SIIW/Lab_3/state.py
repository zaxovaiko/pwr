from colorama import Fore
from player import Player


class State:
    def __init__(self):
        self.against = False
        self.turn = 0
        self.players = [
            Player(inverted=True, name='A', color=Fore.GREEN), 
            Player(name='B', color=Fore.BLUE)
        ]