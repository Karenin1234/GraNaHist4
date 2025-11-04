from enum import Enum

import pygame
from autorzy import autorzy_okno
from pomocnicze import Sceny
from  instrukcja import instrukcja_okno
from Gra import gra_okno
pygame.init()
window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Gra na historie")

def levelOne():
    run = True


    x = 0
    y = 0
    player = pygame.rect.Rect(x, y, 100, 100)
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        speed = 5
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        player = pygame.rect.Rect(x, y, 100, 100)

    window.fill((24, 164, 240))
    pygame.draw.rect(window, (20, 200, 20), player)
    pygame.display.update()

def main():
    aktualna_scena = Sceny.menu
    run = True
    clock=0

    background = pygame.image.load('assets/tło.png').convert()
    przycisk_start = pygame.image.load('assets/przycisk_start.png').convert_alpha()
    przycisk_autorzy = pygame.image.load('assets/przycisk_autorzy.png').convert_alpha()
    przycisk_instrukcja = pygame.image.load('assets/przycisk_autorzy.png').convert_alpha()


    przycisk_start = pygame.transform.scale(przycisk_start, (180, 60))
    przycisk_autorzy = pygame.transform.scale(przycisk_autorzy, (180, 60))
    przycisk_instrukcja = pygame.transform.scale(przycisk_instrukcja, (180, 60))

    przycisk_start_rect = przycisk_start.get_rect(topleft=(320, 250))
    przycisk_autorzy_rect = przycisk_autorzy.get_rect(topleft=(320, 350))
    przycisk_instrukcja_rect = przycisk_instrukcja.get_rect(topleft=(320, 450))

    window.blit(background, (0, 0))
    while run:

        pozycja_myszki = pygame.mouse.get_pos()
        if aktualna_scena == Sceny.menu:
            # animacja przycisku
            if przycisk_start_rect.collidepoint(pozycja_myszki):
                przycisk_start_hover = przycisk_start.copy()
                przycisk_start_hover.fill((50, 50, 50, 50), special_flags=pygame.BLEND_RGBA_ADD)
                window.blit(przycisk_start_hover, przycisk_start_rect)

            else:
                window.blit(przycisk_start, przycisk_start_rect)

            # animacja
            if przycisk_autorzy_rect.collidepoint(pozycja_myszki):
                przycisk_autorzy_hover = przycisk_autorzy.copy()
                przycisk_autorzy_hover.fill((50, 50, 50, 50), special_flags=pygame.BLEND_RGBA_ADD)
                window.blit(przycisk_autorzy_hover, przycisk_autorzy_rect)
            else:
                window.blit(przycisk_autorzy, przycisk_autorzy_rect)

            if przycisk_instrukcja_rect.collidepoint(pozycja_myszki):
                przycisk_instrukcja_hover = przycisk_instrukcja.copy()
                przycisk_instrukcja_hover.fill((50, 50, 50, 50), special_flags=pygame.BLEND_RGBA_ADD)
                window.blit(przycisk_instrukcja_hover, przycisk_autorzy_rect)
            else:
                window.blit(przycisk_instrukcja, przycisk_instrukcja_rect)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if przycisk_start_rect.collidepoint(pozycja_myszki):
                        print("Kliknięto START")
                        aktualna_scena = gra_okno
                        gra_okno()

                    if przycisk_autorzy_rect.collidepoint(pozycja_myszki):
                        print("Kliknięto AUTORZY")
                        aktualna_scena = Sceny.autorzy
                        autorzy_okno(window)

                    if przycisk_instrukcja_rect.collidepoint(pozycja_myszki):
                        print("Kliknięto AUTORZY")
                        aktualna_scena = Sceny.instrukcja
                        instrukcja_okno(window)

        elif aktualna_scena == Sceny.autorzy:
            autorzy_okno(window).draw()
        elif aktualna_scena == Sceny.Gra:
            gra_okno().draw()
        elif aktualna_scena == Sceny.instrukcja:
            instrukcja_okno(window).draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


if __name__=="__main__":
    main()
