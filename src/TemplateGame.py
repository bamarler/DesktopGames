import pygame
import sys
from TemplateConstants import *
from GameMenu import *
from highscores import *

pygame.init()

# Game class
class TemplateGame():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameMenu = GameMenu(self.screen, TEMPLATEGAME_TEXT)
        self.highScore = load_high_score(TEMPLATEGAME)
        self.score = 0
        self.gameEnd = True
        self.pause = False
        pygame.display.set_caption('Template Game')
    
    # makes scene and updates display by calling flip()
    # Effect: draws everything onto the screen (overwriting previous items)
    def makeScene(self):
        self.screen.fill((255, 255, 255))

        scoreText = SCORE_FONT.render('High Score: ' + str(self.highScore) + '  Score: ' + str(self.score), True, SCORE_COLOR)
        
        if (self.gameEnd):
            self.gameMenu.drawPlay(scoreText)
        elif (self.pause):
            self.gameMenu.drawPause(scoreText)
        else:
            pass

        pygame.display.flip()
    
    # this is called every frame
    # Effect: moves the fish and updates the score
    def onTick(self):
        if (self.gameEnd):
            pass
        elif (self.pause):
            pass
        else:
            pass
        
        if (self.highScore < self.score):
            save_high_score(TEMPLATEGAME, self.highScore)
            self.highScore = self.score
    
    # Effect: changes our direction parameters or resets the game
    def onKeyEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = True
        if event.type == pygame.KEYUP:
            pass

    def onMouseEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.gameEnd and self.gameMenu.playButtonClicked(event.pos)):
                self.reset()
            if (self.pause and self.gameMenu.resumeButtonClicked(event.pos)):
                self.pause = False

    # Effect: resets the game
    def reset(self):
        self.score = 0
        self.gameEnd = False

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
