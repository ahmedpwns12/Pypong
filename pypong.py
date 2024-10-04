import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_x_vel = 5 * random.choice((1, -1))
ball_y_vel = 5 * random.choice((1, -1))

paddle_width, paddle_height = 20, 100
paddle_speed = 7
left_paddle_y = HEIGHT // 2 - paddle_height // 2
right_paddle_y = HEIGHT // 2 - paddle_height // 2

left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

# Main game loop
running = True
clock = pygame.time.Clock()

def draw_game():
    win.fill(BLACK)
    
    # Draw paddles
    pygame.draw.rect(win, WHITE, (20, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(win, WHITE, (WIDTH - 40, right_paddle_y, paddle_width, paddle_height))
    
    # Draw ball
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), ball_radius)
    
    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    win.blit(left_text, (WIDTH // 4, 20))
    win.blit(right_text, (3 * WIDTH // 4, 20))
    
    pygame.display.update()

while running:
    clock.tick(60)  # 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys
    keys = pygame.key.get_pressed()
    
    # Move left paddle
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - paddle_height:
        left_paddle_y += paddle_speed
    
    # Move right paddle (AI controlled)
    if ball_y < right_paddle_y + paddle_height // 2 and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if ball_y > right_paddle_y + paddle_height // 2 and right_paddle_y < HEIGHT - paddle_height:
        right_paddle_y += paddle_speed
    
    # Move ball
    ball_x += ball_x_vel
    ball_y += ball_y_vel
    
    # Ball collision with top and bottom
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_y_vel *= -1
    
    # Ball collision with paddles
    if ball_x - ball_radius <= 40 and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_x_vel *= -1
    if ball_x + ball_radius >= WIDTH - 40 and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_x_vel *= -1
    
    # Ball out of bounds
    if ball_x - ball_radius <= 0:
        right_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_x_vel *= random.choice((1, -1))
        ball_y_vel *= random.choice((1, -1))
    
    if ball_x + ball_radius >= WIDTH:
        left_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_x_vel *= random.choice((1, -1))
        ball_y_vel *= random.choice((1, -1))
    
    # Draw everything
    draw_game()

pygame.quit()