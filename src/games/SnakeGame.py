import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from src.constants.SnakeConstants import *
from src.classes.GameMenu import *
from src.classes.highscores import *
from src.classes.util import *

from random import randint


pygame.init()

class SnakeSegment():
    def __init__(self, screen, pos):
        self.screen = screen
        self.x, self.y = pos
        self.currTile = pos

    def draw(self):
        pygame.draw.circle(self.screen, SNAKE_COLOR, (self.x, self.y), SNAKE_SIZE)

    def move(self, pos):
        self.x, self.y = pos

    def updateCurrTile(self):
        # Calculate the current tile's center position
        tile_x = int((self.x - SNAKE_TILE_BASE_X) // SNAKE_TILE_SIZE)
        tile_y = int((self.y - SNAKE_TILE_BASE_Y) // SNAKE_TILE_SIZE)

        if not ((tile_x < 0) or (tile_y < 0) or (tile_x >= X_TILES) or (tile_y >= Y_TILES)):
            self.currTile = SNAKE_TILE_POSITIONS[tile_x][tile_y]

class SnakeHead(SnakeSegment):
    def __init__(self, screen, pos, direction):
        super().__init__(screen, pos)
        self.dir = direction
        self.nextDir = direction
    
    def draw(self):
        pygame.draw.circle(self.screen, SNAKE_COLOR, (self.x, self.y), SNAKE_HEAD_SIZE)
    
    def move(self):
        if self.canTurn():
            self.dir = self.nextDir

        self.x, self.y = (self.x + self.dir[0] * SNAKE_SPEED, self.y + self.dir[1] * SNAKE_SPEED)
    
    def turn(self, direction):
        self.nextDir = direction

    def canTurn(self):
        # Check if the snake's current position is within the tolerance range of the tile's center
        return abs(self.x - self.currTile[0]) < TOLERANCE and abs(self.y - self.currTile[1]) < TOLERANCE
    
    def dead(self, covered):        
        # Calculate the current tile's center position
        tile_x = int((self.x - SNAKE_TILE_BASE_X) // SNAKE_TILE_SIZE)
        tile_y = int((self.y - SNAKE_TILE_BASE_Y) // SNAKE_TILE_SIZE)

        if (tile_x < 0) or (tile_y < 0) or (tile_x >= X_TILES) or (tile_y >= Y_TILES):
            return True

        covered.remove(self.currTile)
        if (len(covered) < SNAKE_SEGS_PER_TILE):
            covered = list()
        else:
            covered = covered[int(3 * SNAKE_SEGS_PER_TILE):]

        for tile in covered:
            if self.currTile == tile:
                return True


        
        return False

class Apple():
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = (-100, -100)

    def draw(self):
        pygame.draw.circle(self.screen, APPLE_COLOR, (self.x, self.y), APPLE_SIZE)
    
    def pickPos(self, covered):
        newPos = SNAKE_TILE_POSITIONS[randint(0, X_TILES - 1)][randint(0, Y_TILES - 1)]
        repeat = False

        for tile in  covered:
            if newPos == tile:
                repeat = True

        if repeat:
            self.pickPos(covered)
        else:
            self.x, self.y = newPos

    def eaten(self, pos):
        return isWithinCircle(pos, self.x, self.y, APPLE_SIZE)

    
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
        self.snakeSegments = [SnakeSegment(self.screen, (CX, CY))]
        self.coveredTiles = list()
        self.apple = Apple(self.screen)
        self.apple.pickPos(self.coveredTiles)
  
        pygame.display.set_caption('Snake Game')
    
    # makes scene and updates display by calling flip()
    # Effect: draws everything onto the screen (overwriting previous items)
    def makeScene(self):
        self.screen.fill(SNAKE_BACKGROUND_COLOR)

        for row in range(0, Y_TILES):
            for col in range(0, X_TILES):
                if ((row + col) % 2 == 0):
                    pygame.draw.rect(self.screen, TILE_COLOR_A, (SNAKE_TILE_BASE_X + row * SNAKE_TILE_SIZE, SNAKE_TILE_BASE_Y + col * SNAKE_TILE_SIZE, SNAKE_TILE_SIZE, SNAKE_TILE_SIZE))
                else:
                    pygame.draw.rect(self.screen, TILE_COLOR_B, (SNAKE_TILE_BASE_X + row * SNAKE_TILE_SIZE, SNAKE_TILE_BASE_Y + col * SNAKE_TILE_SIZE, SNAKE_TILE_SIZE, SNAKE_TILE_SIZE))
        
        self.apple.draw()
        self.snakeHead.draw()
        for seg in self.snakeSegments:
            seg.draw()

        scoreText = SCORE_FONT.render('High Score: ' + str(self.highScore) + '  Score: ' + str(self.score), True, SCORE_COLOR)
        #scoreText = SCORE_FONT.render("Curr pos: " + str((self.snakeHead.x, self.snakeHead.y)) + "  Curr Tile: " + str(self.snakeHead.currTile), True, SCORE_COLOR)

        if (self.gameEnd):
            self.gameMenu.drawPlay(scoreText)
        elif (self.pause):
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
            self.snakeHead.turn((0,0))
        elif (self.pause):
            pass
        else:
            self.snakeHead.move()

            prevSegPos = (self.snakeHead.x, self.snakeHead.y)
            for seg in self.snakeSegments:
                currSegPos = (seg.x, seg.y)
                seg.move(prevSegPos)
                prevSegPos = currSegPos
            
            if (self.apple.eaten((self.snakeHead.x, self.snakeHead.y))):
                self.score += 1
                self.apple.pickPos(self.coveredTiles)
                for i in range(1, int(SNAKE_SEGS_PER_TILE)):
                    self.snakeSegments.append(SnakeSegment(self.screen, (self.snakeSegments[-1].x, self.snakeSegments[-1].y)))
            
            self.coveredTiles = list()
            self.snakeHead.updateCurrTile()
            self.coveredTiles.append(self.snakeHead.currTile)

            for seg in self.snakeSegments:
                seg.updateCurrTile()
                self.coveredTiles.append(seg.currTile)
            
            #print(str(self.coveredTiles))

            self.gameEnd = self.snakeHead.dead(self.coveredTiles)
            

        if (self.highScore < self.score):
            save_high_score(TEMPLATEGAME, self.highScore)
            self.highScore = self.score
    
    # Effect: changes our direction parameters or resets the game
    def onKeyEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = True
            if event.key == pygame.K_UP and self.snakeHead.dir != DIR_DOWN:
                self.snakeHead.turn(DIR_UP)
            elif event.key == pygame.K_DOWN and self.snakeHead.dir != DIR_UP:
                self.snakeHead.turn(DIR_DOWN)
            elif event.key == pygame.K_LEFT and self.snakeHead.dir != DIR_RIGHT:
                self.snakeHead.turn(DIR_LEFT)
            elif event.key == pygame.K_RIGHT and self.snakeHead.dir != DIR_LEFT:
                self.snakeHead.turn(DIR_RIGHT)
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
        self.snakeHead = SnakeHead(self.screen, (CX, CY), (0, 0))
        self.snakeSegments = [SnakeSegment(self.screen, (CX, CY))]
        self.coveredTiles = list()
        self.apple = Apple(self.screen)
        self.apple.pickPos(self.coveredTiles)

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
