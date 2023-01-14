import pygame
import time

# Initialize pygame
pygame.init()

# Set the screen size and caption
width = 500
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Set the snake's initial position and size
snake_pos = [250, 250]
snake_body = [[250, 250], [240, 250], [230, 250]]

# Set the initial direction of the snake
direction = "right"

# Set the initial speed of the snake
speed = 10

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move the snake
    if direction == "right":
        snake_pos[0] += speed
    elif direction == "left":
        snake_pos[0] -= speed
    elif direction == "up":
        snake_pos[1] -= speed
    elif direction == "down":
        snake_pos[1] += speed

    # Insert the new position of the snake's head into the snake body
    snake_body.insert(0, list(snake_pos))

    # Remove the last segment of the snake's body
    snake_body.pop()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Wait for a while
    time.sleep(0.05)

