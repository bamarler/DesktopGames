import pygame
import sys
from GamesConstants import *
from Button import *
from util import *

class GameMenu:
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.nameRect = name.get_rect()
        self.nameRect.center = GAMENAME_TEXT_CENTER
        self.playButton = Button(self.screen, GAME_MENU_BUTTON_WIDTH, GAME_MENU_BUTTON_HEIGHT, PB_NAME, GAME_MENU_BUTTON_FONT, PB_CX, PB_CY)
        self.resumeButton = Button(self.screen, GAME_MENU_BUTTON_WIDTH, GAME_MENU_BUTTON_HEIGHT, R_NAME, GAME_MENU_BUTTON_FONT, PB_CX, PB_CY)
        self.mainMenuButton = Button(self.screen, GAME_MENU_BUTTON_WIDTH, GAME_MENU_BUTTON_HEIGHT, MM_NAME, GAME_MENU_BUTTON_FONT, MM_CX, MM_CY)
    
    def drawPlay(self, scoreText):
        pygame.draw.rect(self.screen, CHARCOAL, RESTART_SCREEN_POS)
        self.screen.blit(self.name, self.nameRect)

        scoreRect = scoreText.get_rect()
        scoreRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 15 / 32)
        self.screen.blit(scoreText, scoreRect)

        self.playButton.draw()
        self.mainMenuButton.draw()

    def drawPause(self, scoreText):
        pygame.draw.rect(self.screen, CHARCOAL, RESTART_SCREEN_POS)
        self.screen.blit(self.name, self.nameRect)

        scoreRect = scoreText.get_rect()
        scoreRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 15 / 32)
        self.screen.blit(scoreText, scoreRect)

        self.resumeButton.draw()
        self.mainMenuButton.draw()

    def playButtonClicked(self, pos):
        return self.playButton.clicked(pos)
    
    def resumeButtonClicked(self, pos):
        return self.resumeButton.clicked(pos)
    
    def mainMenuButtonClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.mainMenuButton.clicked(event.pos)