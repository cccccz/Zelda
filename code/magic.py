import pygame
from settings import *

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player

    def heal(self,player,strength,cost,groups):
        print('heal')
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost

    def flame(self):
        pass