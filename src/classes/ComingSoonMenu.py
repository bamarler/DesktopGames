import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from src.constants.GamesConstants import *
from src.classes.Button import *
from src.classes.util import *

class ComingSoonMenu:
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.nameRect = name.get_rect()
        self.nameRect.center = GAMENAME_TEXT_CENTER
        self.mainMenuButton = Button(self.screen, GAME_MENU_BUTTON_WIDTH, GAME_MENU_BUTTON_HEIGHT, MM_NAME, GAME_MENU_BUTTON_FONT, CX, MM_CY)
    
    def drawMainMenu(self):
        pygame.draw.rect(self.screen, CHARCOAL, RESTART_SCREEN_POS)
        self.screen.blit(self.name, self.nameRect)

        self.mainMenuButton.draw()
    
    def mainMenuButtonClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.mainMenuButton.clicked(event.pos)