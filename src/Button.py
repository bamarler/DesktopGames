import pygame
from Constants import *

pygame.init()

class Button():
    def __init__(self, screen, name, font, cx, cy, lx, rx, ly, ry):
        self.screen = screen
        self.name = name
        self.font = font
        self.text = font.render(name, True, BUTTON_TEXT_COLOR)
        self.rect = self.text.get_rect(center=(cx, cy))
        self.lx = lx
        self.rx = rx
        self.ly = ly
        self.ry = ry
    
    def draw(self):
        pygame.draw.rect(self.screen, BUTTON_COLOR, (self.lx, self.ly, self.rx - self.lx, self.ry - self.ly))
        self.screen.blit(self.text, self.rect)

    def clicked(self, pos):
        x, y = pos
        return self.lx < x < self.rx and self.ly < y < self.ry