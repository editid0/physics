# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 500

BALL_POSITION = (WIDTH // 2, HEIGHT // 2)
RADIUS = 75

ticks_in_air = 0

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    if (BALL_POSITION[1] + RADIUS) > HEIGHT:
        ticks_in_air = 0
    else:
        ticks_in_air += 1
        # Update the ball position
        BALL_POSITION = (BALL_POSITION[0], BALL_POSITION[1] + 1)
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), BALL_POSITION, RADIUS)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
