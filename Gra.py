import pygame
from pygame.sysfont import font_constructor


class gra_okno():
    def __init__(self):
        okno= pygame.display.set_mode((1920,1080))
        self.okno = okno
        self.okno.fill((0,0,0))
        pygame.font.Font("assets/czcionka.ttf",40)
        self.text_surface = font_constructor('assets/czcionka.ttf', True, (255, 255, 255), 2)

        pygame.display.update()
    def draw(self):
        pass


