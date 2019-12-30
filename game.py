import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)

pixel_width = 15
pixel_height = 15
pixel_margin = 3

game_height = 800
game_width = 600

x_speed = pixel_width + pixel_margin
y_speed = 0

class Segment(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface([pixel_width,pixel_height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()
screen = pygame.display.set_mode([game_height, game_width])
pygame.display.set_caption('Snek v Snek')
allspriteslist = pygame.sprite.Group()

snake = []
for i in range(3):
    x = game_width / 2
    y = game_height / 2 + (pixel_width + pixel_margin) * i
    segment = Segment(x,y)
    snake.append(segment)
    allspriteslist.add(segment)

clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (pixel_width + pixel_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (pixel_width + pixel_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (pixel_height + pixel_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (pixel_height + pixel_margin)
 
    old_segment = snake.pop()
    allspriteslist.remove(old_segment)
 
    x = snake[0].rect.x + x_speed
    y = snake[0].rect.y + y_speed
    segment = Segment(x, y)
 
    snake.insert(0, segment)
    allspriteslist.add(segment)
 
    screen.fill(BLACK)
 
    allspriteslist.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(5)
 
pygame.quit()
