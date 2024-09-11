import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 50  # Size of each grid cell
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basis and Dimensions Game")

# Player variables
player_x = 0
player_y = 0

# Objects collected (basis vectors collected)
objects_collected = 0
required_objects = 3  # Example: Player needs to collect 3 objects to span a new dimension

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if player_x > 0:
            player_x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if player_x < GRID_WIDTH - 1:
            player_x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if player_y > 0:
            player_y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if player_y < GRID_HEIGHT - 1:
            player_y += 1

    # Draw player
    pygame.draw.rect(screen, RED, (player_x * GRID_SIZE, player_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw objects (basis vectors)
    # For simplicity, let's draw some objects randomly on the grid
    # Each collected object increases `objects_collected`

    # Example of drawing objects (basis vectors)
    if objects_collected < required_objects:
        pygame.draw.rect(screen, BLUE, (3 * GRID_SIZE, 3 * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    if objects_collected < required_objects:
        pygame.draw.rect(screen, BLUE, (5 * GRID_SIZE, 6 * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    if objects_collected < required_objects:
        pygame.draw.rect(screen, BLUE, (7 * GRID_SIZE, 4 * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Check if player collects an object
    if (player_x == 3 and player_y == 3) or (player_x == 5 and player_y == 6) or (player_x == 7 and player_y == 4):
        objects_collected += 1

    # Check if player has enough objects to increase dimensionality
    if objects_collected >= required_objects:
        # Increase dimensionality (e.g., unlock new areas of the grid)
        required_objects += 1  # Increase the requirement for the next dimensionality increase

    # Update the display
    pygame.display.flip ()

# Quit pygame
pygame.quit()
sys.exit()
