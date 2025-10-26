import pygame


class autorzy_okno():
    def __init__(self, okno):
        self.okno = okno
        self.okno.fill((0,0,0))
        pygame.font.Font("assets/czcionka.ttf",40)

        pygame.display.update()
    def draw(self):
        pass