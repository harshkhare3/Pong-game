import pygame

class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, 10, 140))