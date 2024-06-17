import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from src.constants.ComingSoonConstants import *
from src.classes.ComingSoonMenu import *
from src.classes.highscores import *

pygame.init()

# Game class
class ComingSoon():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameMenu = ComingSoonMenu(self.screen, COMINGSOON_TEXT)
        pygame.display.set_caption(COMINGSOON)
    
    # makes scene and updates display by calling flip()
    # Effect: draws everything onto the screen (overwriting previous items)
    def makeScene(self):
        self.screen.fill(CYAN)

        self.gameMenu.drawMainMenu()

        pygame.display.flip()
    
    # this is called every frame
    # Effect: moves the fish and updates the score
    def onTick(self):
        pass
    
    # Effect: changes our direction parameters or resets the game
    def onKeyEvent(self, event):
        pass

    def onMouseEvent(self, event):
        pass

    # Effect: resets the game
    def reset(self):
        pass

    # Runs the game
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return QUIT
                self.onKeyEvent(event)
                self.onMouseEvent(event)
                if self.gameMenu.mainMenuButtonClicked(event):
                    running = False
                    return MAINMENU
            
            self.onTick()
            self.makeScene()
            clock.tick(TICK_SPEED)
        
        pygame.quit()
        sys.exit()
