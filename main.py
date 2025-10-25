import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
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
    background = pygame.image.load('tloTest.png')
    while run:
        clock+= pygame.time.Clock().tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(background,(0,0))
        pygame.display.update()

if __name__=="__main__":
    main()