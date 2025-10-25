import pygame
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
    run = True
    clock=0

    background = pygame.image.load('assets/tło.png').convert()
    przycisk_start = pygame.image.load('assets/przycisk_start.png').convert_alpha()
    przycisk_autorzy = pygame.image.load('assets/przycisk_autorzy.png').convert_alpha()


    przycisk_start = pygame.transform.scale(przycisk_start, (180, 60))
    przycisk_autorzy = pygame.transform.scale(przycisk_autorzy, (180, 60))


    przycisk_start_rect = przycisk_start.get_rect(topleft=(320, 250))
    przycisk_autorzy_rect = przycisk_autorzy.get_rect(topleft=(320, 350))

    while run:
        pozycja_myszki = pygame.mouse.get_pos()


        window.blit(background, (0, 0))


        if przycisk_start_rect.collidepoint(pozycja_myszki):
            przycisk_start_hover = przycisk_start.copy()
            przycisk_start_hover.fill((50, 50, 50, 50), special_flags=pygame.BLEND_RGBA_ADD)
            window.blit(przycisk_start_hover, przycisk_start_rect)
        else:
            window.blit(przycisk_start, przycisk_start_rect)


        if przycisk_autorzy_rect.collidepoint(pozycja_myszki):
            przycisk_autorzy_hover = przycisk_autorzy.copy()
            przycisk_autorzy_hover.fill((50, 50, 50, 50), special_flags=pygame.BLEND_RGBA_ADD)
            window.blit(przycisk_autorzy_hover, przycisk_autorzy_rect)
        else:
            window.blit(przycisk_autorzy, przycisk_autorzy_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if przycisk_start_rect.collidepoint(pozycja_myszki):
                    print("Kliknięto START")


                if przycisk_autorzy_rect.collidepoint(pozycja_myszki):
                    print("Kliknięto AUTORZY")



        pygame.display.update()

if __name__=="__main__":
    main()