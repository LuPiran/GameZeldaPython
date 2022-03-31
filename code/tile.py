import pygame
from Code.settings import *

class Tile(pygame.srpite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image
        self.rect = self.image.get_rect(topleft = pos)
