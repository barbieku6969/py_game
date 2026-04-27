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

# Grid
TILE = 20
ROWS = COLS = WIDTH // TILE

# Square settings
posisjon = [
        [WIDTH // 2, HEIGHT // 2]
        ]
square_size = 20
dir_x, dir_y = 0, 0
speed = 20


circle_X =  random.randint(0, WIDTH // TILE - 1) * TILE
circle_Y =  random.randint(0, HEIGHT // TILE - 1) * TILE


# Simple maze layout (1 = wall, 0 = path)



BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BG = (30, 30, 30)



# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BG)
    for x in range(0, WIDTH, TILE):
        for y in range(0, HEIGHT, TILE):
            rect = pygame.Rect(x, y, TILE, TILE)
            pygame.draw.rect(screen, WHITE, rect, 1)



    # Check collision with all snake segments
    colliding = False
    for segment in posisjon:
        slange = pygame.Rect(segment[0], segment[1], square_size, square_size)
        eple = pygame.Rect(circle_X, circle_Y ,20,20)
        if slange.colliderect(eple):
            colliding = True
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dir_x = -1
        dir_y = 0
    if keys[pygame.K_RIGHT]:
        dir_x = 1
        dir_y = 0
    if keys[pygame.K_UP]:
        dir_y = -1
        dir_x = 0
    if keys[pygame.K_DOWN]:
        dir_y = 1
        dir_x = 0

    posisjon[0][0] += dir_x * speed
    posisjon[0][1] += dir_y * speed
    # Move each body segment to follow the one before it
    for i in range(len(posisjon) - 1, 0, -1):
        posisjon[i][0] = posisjon[i-1][0]
        posisjon[i][1] = posisjon[i-1][1]
    # Keep square on screen
    posisjon[0][0] = max(0, min(WIDTH - square_size, posisjon[0][0]))
    posisjon[0][1] = max(0, min(HEIGHT - square_size, posisjon[0][1]))

    # Drawing - draw all snake segments
    for segment in posisjon:
        pygame.draw.rect(
            screen,
            (0, 200, 255),
            pygame.Rect(segment[0], segment[1], square_size, square_size)
        )

    pygame.draw.rect( screen, (255, 100, 0),eple)

    # Text
    if (colliding):
        circle_X =  random.randint(0, WIDTH // TILE - 1) * TILE
        circle_Y =  random.randint(0, HEIGHT // TILE - 1) * TILE
        # Add new segment to snake (duplicate the last segment)
        posisjon.append(posisjon[-1][:])
        
        
        




    pygame.display.flip()
    clock.tick(10)
