import pygame

class Level:
    def __init__(self):
        #obter a superfície de exibição
        self.display_surface = pygame.display.get_surface()
        
        # configuração do grupo sprite
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        # atualize e desenhe o jogo
        pass
