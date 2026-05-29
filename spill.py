import pygame  # Import pygame for game graphics and input handling
import sys  # Import sys to exit the program cleanly
import random  # Import random to place the apple at a random position

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Lag vinduet
pygame.display.set_caption("Moving Square")  # Gi vinduet navn

# Bruk klokke for å styre bildefrekvens
clock = pygame.time.Clock()

# Rutenettinnstillinger
TILE = 20
ROWS = COLS = WIDTH // TILE  # Antall ruter på hver akse

# Slangeinnstillinger
posisjon = [[WIDTH // 2, HEIGHT // 2]]  # Start på midten
square_size = 20  # Størrelsen på slangen og eplet

dir_x, dir_y = 0, 0  # Start uten bevegelse
speed = TILE  # Flytt én rute per oppdatering

# Startposisjon for eplet
circle_X = random.randint(0, WIDTH // TILE - 1) * TILE
circle_Y = random.randint(0, HEIGHT // TILE - 1) * TILE

bomb_X = random.randint(0, WIDTH // TILE - 1) * TILE
bomb_Y = random.randint(0, HEIGHT // TILE - 1) * TILE

# Farger
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BG = (30, 30, 30)
SNAKE_COLOR = (0, 200, 255)
APPLE_COLOR = (255, 100, 0)
BANNANA_COLOR = (255, 255, 0)
bomb_color = (255, 255, 212)
font = pygame.font.SysFont(None, 36)



# Font for tekstx|
font = pygame.font.Font(None, 36)
myFont = pygame.font.SysFont("Times New Roman", 18)


def draw_grid():
    """Tegner rutenettet på skjermen."""
    for x in range(0, WIDTH, TILE):
        for y in range(0, HEIGHT, TILE):
            rect = pygame.Rect(x, y, TILE, TILE)
            pygame.draw.rect(screen, WHITE, rect, 1)  # Tegn kantlinje for hver rute


def draw_text(text, x, y, color=WHITE):
    """Tegner tekst på skjermen på posisjon (x, y)."""
    surface = font.render(text, True, color)  # Lag tekstsurface
    screen.blit(surface, (x, y))  # Tegn tekst på skjermen


def reset_game():
    """Setter spillet tilbake til startverdier."""
    score = 0  # Tilbakestill poengsum
    global posisjon, dir_x, dir_y, circle_X, circle_Y
    posisjon = [[WIDTH // 2, HEIGHT // 2]]  # Plasser slangen midt på skjermen
    dir_x, dir_y = 0, 0  # Stopp bevegelser
    circle_X = random.randint(0, WIDTH // TILE - 1) * TILE  # Ny tilfeldig epleposisjon
    circle_Y = random.randint(0, HEIGHT // TILE - 1) * TILE
    bomb_X = random.randint(0, WIDTH // TILE - 1) * TILE
    bomb_Y = random.randint(0, HEIGHT // TILE - 1) * TILE
    
    black = (0, 0, 0)  # Farge for tekst


def main_menu():
    """Viser hovedmenyen før spillet starter."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Start spillet
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(BG)  # Fyll bakgrunnen
        draw_text("HOVEDMENY", WIDTH // 2 - 90, HEIGHT // 2 - 80)
        draw_text("Trykk ENTER for å starte", WIDTH // 2 - 170, HEIGHT // 2 - 20)
        draw_text("Trykk ESC for å avslutte", WIDTH // 2 - 170, HEIGHT // 2 + 20)

        pygame.display.flip()  # Oppdater skjermen
        clock.tick(30)  # Hold menyen til 30 FPS


def game_loop():
    """Hovedspill-løkken som kjører etter menyen."""
    global dir_x, dir_y, circle_X, circle_Y, bomb_X, bomb_Y
    running = True
    move_bomb = 0
    score = 0
   

   

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


         
        
       

        keys = pygame.key.get_pressed()  # Sjekk tastetrykk for bevegelse
        if keys[pygame.K_LEFT]:
            dir_x = -1
            dir_y = 0
        elif keys[pygame.K_RIGHT]:
            dir_x = 1
            dir_y = 0
        elif keys[pygame.K_UP]:
            dir_x = 0
            dir_y = -1
        elif keys[pygame.K_DOWN]:
            dir_x = 0
            dir_y = 1
        move_bomb += 1
        if move_bomb == 60:
            move_bomb = 0
            for i in range(3):  
                bomb_X = random.randint(0, WIDTH // TILE - 1) * TILE  # Ny tilfeldig bombeplassering
                bomb_Y = random.randint(0, HEIGHT // TILE - 1) * TILE
                # Vent litt for å unngå at bombene spawner på samme sted

        posisjon[0][0] += dir_x * speed  # Flytt hodet i x-retning
        posisjon[0][1] += dir_y * speed  # Flytt hodet i y-retning

        # Flytt hvert segment til posisjonen til segmentet foran
        for i in range(len(posisjon) - 1, 0, -1):
            posisjon[i][0] = posisjon[i - 1][0]
            posisjon[i][1] = posisjon[i - 1][1]

        # Sørg for at slangen holder seg innenfor skjermen
        posisjon[0][0] = max(0, min(WIDTH - square_size, posisjon[0][0]))
        posisjon[0][1] = max(0, min(HEIGHT - square_size, posisjon[0][1]))

        screen.fill(BG)  # Fyll bakgrunnen på nytt
        draw_grid()  # Tegn rutenettet

        slange = pygame.Rect(posisjon[0][0], posisjon[0][1], square_size, square_size)
        eple = pygame.Rect(circle_X, circle_Y, square_size, square_size)
        BANNANA = pygame.Rect(circle_Y, circle_X, square_size, square_size)
        bombe = pygame.Rect(bomb_X, bomb_Y, square_size, square_size)

        if slange.colliderect(BANNANA):  # Sjekk om slangen treffer bananen
            circle_X = random.randint(0, WIDTH // TILE - 1) * TILE
            circle_Y = random.randint(0, HEIGHT // TILE - 1) * TILE
            
            posisjon.append(posisjon[-1][:])  # Legg til nytt segment bakerst
            posisjon.append(posisjon[-1][:])  # Legg til nytt segment bakerst
            posisjon.append(posisjon[-1][:])  # Legg til nytt segment bakerst
            score += 3
        if score >= 100:
            draw_text("You win!", WIDTH // 2 - 80, HEIGHT // 2 - 20, color=(0, 255, 0))
            pygame.display.flip()  # Oppdater skjermen for å vise You win!
            pygame.time.wait(2000)  # Vent i 2 sekunder før du starter
            reset_game()  # Start spillet på nytt

        if slange.colliderect(bombe):  # Sjekk om slangen treffer bomben
            draw_text("GAME OVER", WIDTH // 2 - 80, HEIGHT // 2 - 20, color=(255, 0, 0))
            pygame.display.flip()  # Oppdater skjermen for å vise GAME OVER
            pygame.time.wait(2000)  # Vent i 2 sekunder før du starter
            reset_game()  # Start spillet på nytt
            score = 0  # Tilbakestill poengsum

        if slange.colliderect(eple):  # Sjekk om slangen treffer eplet
            circle_X = random.randint(0, WIDTH // TILE - 1) * TILE
            circle_Y = random.randint(0, HEIGHT // TILE - 1) * TILE
            posisjon.append(posisjon[-1][:])  # Legg til nytt segment bakerst
            score += 1 

        for segment in posisjon:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], square_size, square_size))

        pygame.draw.rect(screen, APPLE_COLOR, eple)  # Tegn eplet
        pygame.draw.rect(screen, BANNANA_COLOR, BANNANA)  # Tegn bananen
        pygame.draw.rect(screen, bomb_color, bombe)  # Tegn bomben
        displayScore = myFont.render("Score: " + str(score), 1, (255, 255, 255))
        displayScoreRect = displayScore.get_rect()
        displayScoreRect.topleft = (10, 10)
        screen.blit(displayScore, displayScoreRect)  # Vis poengsummen
        
        pygame.display.flip()  # Oppdater skjermen
        clock.tick(10)  # Spillet kjører i 10 bilder per sekund

    pygame.quit()
    sys.exit()



reset_game()  # Sett spillet til startverdier
main_menu()  # Vis menyen først
game_loop()  # Start selve spillet
