import pygame
import sys
from SnakeConstants import *
from GameMenu import *
from highscores import *

pygame.init()

class SnakeSegment():
    def __init__(self, screen, pos):
        self.screen = screen
        self.pos = pos

    def draw(self):
        pygame.draw.circle(self.screen, SNAKE_COLOR, self.pos, SNAKE_SIZE)

    def move(self, pos):
        self.pos = pos

class SnakeHead(SnakeSegment):
    def __init__(self, screen, pos, velocity):
        super().__init__(screen, pos)
        self.vx, self.vy = velocity
    
    def draw(self):
        pygame.draw.circle(self.screen, SNAKE_COLOR, self.pos, SNAKE_SIZE)
    
    def move(self):
        pos = (self.pos[0] + self.vx, self.pos[1] + self.vy)
    
    def changeVelocity(self, velocity):
        self.vx, self.vy = velocity

class Apple():
    def __init__(self, screen):
        self.screen = screen
        self.pos = (-100, -100)

    def draw(self):
        pygame.draw.circle(self.screen, APPLE_COLOR, self.pos, APPLE_SIZE)
    
# Game class
class SnakeGame():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameMenu = GameMenu(self.screen, SNAKEGAME_TEXT)
        self.highScore = load_high_score(TEMPLATEGAME)
        self.score = 0
        self.gameEnd = True
        self.pause = False
        self.snakeHead = SnakeHead(self.screen, (CX, CY), (0, 0))
        self.snakeSegments = list()
        pygame.display.set_caption('Snake Game')
    
    # makes scene and updates display by calling flip()
    # Effect: draws everything onto the screen (overwriting previous items)
    def makeScene(self):
        self.screen.fill(SNAKE_BACKGROUND_COLOR)

        for row in range(0, Y_TILES):
            for col in range(0, X_TILES):
                if ((row + col) % 2 == 0):
                    pygame.draw.rect(self.screen, TILE_COLOR_A, (TILE_BASE_X + row * TILE_SIZE, TILE_BASE_Y + col * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                else:
                    pygame.draw.rect(self.screen, TILE_COLOR_B, (TILE_BASE_X + row * TILE_SIZE, TILE_BASE_Y + col * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
        self.snakeHead.draw()

        scoreText = SCORE_FONT.render('High Score: ' + str(self.highScore) + '  Score: ' + str(self.score), True, SCORE_COLOR)
        
        if (self.gameEnd):
            self.gameMenu.drawPlay(scoreText)
        if (self.pause):
            self.gameMenu.drawPause(scoreText)
        else:
            scoreRect = scoreText.get_rect()
            scoreRect.center = (CX, SCORE_SIZE)
            self.screen.blit(scoreText, scoreRect)

        pygame.display.flip()
    
    # this is called every frame
    # Effect: moves the fish and updates the score
    def onTick(self):
        if (self.gameEnd):
            pass
        if (self.pause):
            pass
        else:
            self.snakeHead.move()
        
        if (self.highScore < self.score):
            save_high_score(TEMPLATEGAME, self.highScore)
            self.highScore = self.score
    
    # Effect: changes our direction parameters or resets the game
    def onKeyEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = True
            if event.key == pygame.K_UP:
                self.snakeHead.changeVelocity((0, -1))
            elif event.key == pygame.K_DOWN:
                self.snakeHead.changeVelocity((0, 1))
            elif event.key == pygame.K_LEFT:
                self.snakeHead.changeVelocity((-1, 0))
            elif event.key == pygame.K_RIGHT:
                self.snakeHead.changeVelocity((1, 0))
        if event.type == pygame.KEYUP:
            pass

    def onMouseEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.gameMenu.playButtonClicked(event.pos)):
                self.reset()
            if (self.pause and self.gameMenu.resumeButtonClicked(event.pos)):
                self.pause = False

    # Effect: resets the game
    def reset(self):
        self.score = 0
        self.gameEnd = False

    # returns "MainMenu" if pressed
    def mainMenu(self, event):
        return self.gameMenu.mainMenuButtonClicked(event)

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
                if self.mainMenu(event):
                    running = False
                    return MAINMENU
            
            self.onTick()
            self.makeScene()
            clock.tick(TICK_SPEED)
        
        pygame.quit()
        sys.exit()
