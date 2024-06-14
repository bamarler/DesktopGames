import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from src.constants.Constants import *

pygame.init()

class Button():
    def __init__(self, screen, width, height, name, font, cx, cy):
        self.screen = screen
        self.name = name
        self.font = font
        self.text = font.render(name, True, BUTTON_TEXT_COLOR)
        self.rect = self.text.get_rect(center=(cx, cy))
        self.lx = cx - width / 2
        self.rx = cx + width / 2
        self.ly = cy - height / 2
        self.ry = cy + height / 2
    
    def draw(self):
        pygame.draw.rect(self.screen, BUTTON_COLOR, (self.lx, self.ly, self.rx - self.lx, self.ry - self.ly))
        self.screen.blit(self.text, self.rect)

    def clicked(self, pos):
        x, y = pos
        return self.lx < x < self.rx and self.ly < y < self.ry