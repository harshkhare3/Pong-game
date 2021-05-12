import pygame
import time
from paddle import Paddle
from ball import Ball

# General Setup
pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong using pygame @harshkhare3")

bg_color = pygame.Color('grey12')
player_a_score = 0
player_b_score = 0

def main():
    run = True
    FPS = 60

    paddle_vel = 5

    clock = pygame.time.Clock()

    paddle_a = Paddle(0, 275)
    paddle_b = Paddle(740, 270)
    ball = Ball(360, 360)

    score_font = pygame.font.SysFont("comicsans", 60)

    def check_score():
        global player_a_score
        global player_b_score

        if ball.x <=0 and not(ball.y >= paddle_a.y and ball.y <= paddle_a.y + 140):
            player_b_score += 1
        if ball.x >=730 and not(ball.y >= paddle_b.y and ball.y <= paddle_b.y + 140):
            player_a_score += 1
            print(player_a_score)
    def redraw_window():
        WIN.fill(bg_color)
        
        # Draw Paddles and balls
        paddle_a.draw(WIN)
        paddle_b.draw(WIN)
        ball.draw(WIN)

        # Score
        score_a_label = score_font.render(f"Player A: {player_a_score}", 1, (255, 255, 255))
        score_b_label = score_font.render(f"Player B: {player_b_score}", 1, (255, 255, 255))
        
        WIN.blit(score_a_label, (10, 10))
        WIN.blit(score_b_label, (WIDTH - score_b_label.get_width() - 10, 10))

        pygame.display.update()  # Refresh Display

    while run:
        clock.tick(FPS)
        redraw_window()
        ball.ball_movement()
        check_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and paddle_a.y > 5:
            paddle_a.y -= paddle_vel
        if keys[pygame.K_s] and paddle_a.y + 140 < HEIGHT:
            paddle_a.y += paddle_vel
        if keys[pygame.K_UP] and paddle_b.y > 5:
            paddle_b.y -= paddle_vel
        if keys[pygame.K_DOWN] and paddle_b.y + 140 < HEIGHT:
            paddle_b.y += paddle_vel


main()