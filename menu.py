import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

game_height = 800
game_width = 600

pygame.init()
screen = pygame.display.set_mode([game_height, game_width])
pygame.display.set_caption('Snek v Snek')
allspriteslist = pygame.sprite.Group()

screen.fill(BLACK)

menuScreen = True;
while menuScreen:


    mouse = pygame.mouse.get_pos()

    print(mouse)
    pygame.draw.rect(screen, WHITE, (150, 450, 100, 50))
    pygame.draw.rect(screen, WHITE, (550, 450, 100, 50))

    allspriteslist.draw(screen)

    pygame.display.flip()

    if 150 < mouse[0] < 150+100 and 450 <  mouse[1] < 450+50 and pygame.mouse.get_pressed()[0] == 1:
        menuScreen = False
        pygame.quit()


pygame.quit()
