# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)

WIDTH, HEIGHT = 1000, 800

BALL_POSITION = (WIDTH // 2, HEIGHT // 2)
RADIUS = 75

ticks_in_air = 0
velocity_y = 0  # Add velocity tracking

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # Move the ball up and give it initial upward velocity
                BALL_POSITION = (BALL_POSITION[0], BALL_POSITION[1] - 50)
                velocity_y = -15  # Negative for upward movement
                ticks_in_air = 1

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Check if ball is on the ground
    if (BALL_POSITION[1] + RADIUS) >= HEIGHT:
        # Ball is on ground
        BALL_POSITION = (BALL_POSITION[0], HEIGHT - RADIUS)  # Keep ball on ground
        ticks_in_air = 0
        velocity_y = 0
    else:
        # Ball is in air - apply physics
        ticks_in_air += 1
        gravity = 0.8  # Constant gravity acceleration
        velocity_y += gravity  # Increase downward velocity
        # Update the ball position
        BALL_POSITION = (BALL_POSITION[0], BALL_POSITION[1] + velocity_y)

    # Draw a solid blue circle
    pygame.draw.circle(screen, (200, 200, 255), BALL_POSITION, RADIUS)
    text_surface = my_font.render(f"Velocity: {velocity_y:.1f}", False, (0, 0, 0))
    screen.blit(text_surface, (BALL_POSITION[0] - RADIUS, BALL_POSITION[1] - RADIUS))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
