# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# dice colors
red = pygame.color.Color('#FF0000')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

# initializing values
x = 250
y = 250
x2 = 250
y2 = 250
x3 = 250
y3 = 250
x4 = 250
y4 = 250
x5 = 250
y5 = 250
x6 = 250
y6 = 250

while running:
    screen.fill(black)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    # Generate values to draw dice in game for dice values 1 through 6
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        num = random.randrange(1, 7)
        if num == 1:
            x = 250
            y = 250
            x2 = 250
            y2 = 250
            x3 = 250
            y3 = 250
            x4 = 250
            y4 = 250
            x5 = 250
            y5 = 250
            x6 = 250
            y6 = 250
        elif num == 2:
            x = 210
            y = 210
            x2 = 210
            y2 = 210
            x3 = 210
            y3 = 210
            x4 = 210
            y4 = 210
            x5 = 210
            y5 = 210
            x6 = 290
            y6 = 290
        elif num == 3:
            x = 210
            y = 210
            x2 = 210
            y2 = 210
            x3 = 210
            y3 = 210
            x4 = 210
            y4 = 210
            x5 = 290
            y5 = 290
            x6 = 250
            y6 = 250
        elif num == 4:
            x = 210
            y = 210
            x2 = 290
            y2 = 290
            x3 = 290
            y3 = 210
            x4 = 210
            y4 = 290
            x5 = 210
            y5 = 210
            x6 = 210
            y6 = 210
        elif num == 5:
            x = 210
            y = 210
            x2 = 290
            y2 = 290
            x3 = 290
            y3 = 210
            x4 = 210
            y4 = 290
            x5 = 250
            y5 = 250
            x6 = 250
            y6 = 250
        else:
            x = 210
            y = 210
            x2 = 290
            y2 = 290
            x3 = 290
            y3 = 210
            x4 = 210
            y4 = 290
            x5 = 210
            y5 = 250
            x6 = 290
            y6 = 250

    pygame.draw.rect(screen, red, (200, 200, 100, 100))
    pygame.draw.circle(screen, white, [x, y], 8)
    pygame.draw.circle(screen, white, [x2, y2], 8)
    pygame.draw.circle(screen, white, [x3, y3], 8)
    pygame.draw.circle(screen, white, [x4, y4], 8)
    pygame.draw.circle(screen, white, [x5, y5], 8)
    pygame.draw.circle(screen, white, [x6, y6], 8)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()