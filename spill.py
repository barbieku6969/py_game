import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Square")
pygame.display.set_caption("Collision Detector")

# Clock
clock = pygame.time.Clock()

# Square settings
square_size = 50
square_x = WIDTH // 2
square_y = HEIGHT // 2
speed = 5

circle_X =  random.randint(0, WIDTH)
circle_Y =  random.randint(0, HEIGHT)

kropp_Y = square_y - 10
kropp_x = square_x 

kropp_x = -1000
kropp_Y = -1000

kroppListe = []
follow = False






# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    eple = pygame.Rect(circle_X, circle_Y ,20,20)
    slange = pygame.Rect(square_x, square_y, square_size, square_size)
    kropp  = pygame.Rect(kropp_x - 10, kropp_Y, 50, 50)
    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    # Keep square on screen
    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    # Drawing
    screen.fill((30, 30, 30))  # background
    pygame.draw.rect(
        screen,
        (0, 200, 255),
        slange
    )
    pygame.draw.rect(screen, (255, 0, 0), kropp)


    pygame.draw.rect( screen, (255, 100, 0),eple)

    colliding = slange.colliderect(eple)
    # Text
    if (colliding):
        circle_X =  random.randint(0, WIDTH)
        circle_Y =  random.randint(0, HEIGHT)
        follow = True
        

    if (follow):
        kropp_Y = square_y 
        kropp_x = square_x -20




    pygame.display.flip()
    clock.tick(60)
