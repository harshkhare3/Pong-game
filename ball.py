import pygame

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball_vel_x = 5
        self.ball_vel_y = 3
       
    def draw(self, window):
        pygame.draw.ellipse(window, (255, 255, 255), (self.x, self.y, 20, 20))

    def ball_movement(self):
        self.x += self.ball_vel_x
        self.y += self.ball_vel_y

        if self.y <=0 or self.y >= 730:
            self.ball_vel_y *= -1
        if self.x <=0 or self.x >= 730:
            self.ball_vel_x *= -1

        