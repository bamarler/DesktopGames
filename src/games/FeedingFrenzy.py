import pygame
import sys
sys.path.insert(0, 'C:\\Users\\bam27\\DesktopGames\\DesktopGames\\src')
import math
from random import randint, random
from constants.FeedingConstants import *
from classes.GameMenu import *
from classes.highscores import *
from classes.util import *

# Initialize Pygame
pygame.init()

# Fish class
class Fish():
    def __init__(self, screen, size, x, y, directionX):
        self.screen = screen
        self.size = size
        self.x, self.y = (x, y)
        self.directionX = directionX
    
    # Effect: draws this screen onto current scene
    def draw(self):
        pygame.draw.circle(self.screen, PLAYER_COLOR, (self.x, self.y), self.size)
        
        directionX = self.directionX
        if (directionX == 0):
            directionX = 1
        
        triangle_vertices = [(self.x - self.size * directionX, self.y), 
                             (self.x - self.size * 2 * directionX, self.y + self.size), 
                             (self.x - self.size * 2 * directionX, self.y - self.size)]  
        pygame.draw.polygon(self.screen, PLAYER_COLOR, triangle_vertices, 0)

    # returns the value of this fish
    def value(self):
        return self.size / SIZE_TO_SCORE
    
    # Effect: moves this Fish in the given directions by the given speed
    def move(self, directionX, directionY, speed):
        self.directionX = directionX
        self.move_X(self.directionX, speed)
        self.move_Y(directionY, speed)

    # Effect: moves this Fish in the given x-direction by the given speed
    def move_X(self, directionX, speed):
        if (self.x + directionX * speed < 0):
            self.x = SCREEN_WIDTH + directionX * speed
        elif(self.x + directionX * speed > SCREEN_WIDTH):
            self.x = directionX * speed
        else:
            self.x += directionX * speed

    # Effect: moves this Fish in the given y-direction by the given speed
    def move_Y(self, directionY, speed):
        if (self.y + directionY * speed < 0):
            self.y = 0
        elif(self.y + directionY * speed > SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT
        else:
            self.y += directionY * speed

    # Effect: updates the size of this fish
    def updateSize(self, size, growSize, grow):
        if (grow):
            self.size = growSize
        else:
            self.size = size

    # Returns the score collected from eating fish
    # Effect: removes the eaten fish from the background
    def eat(self, background):
        collectedScore = 0
        for fish in background:
            if (fish.size < self.size and self.size > math.sqrt(pow(fish.x - self.x, 2) + pow(fish.y - self.y, 2))):
                collectedScore += fish.value()
                background.remove(fish)
        return collectedScore
    
    # returns true if this fish is eaten
    def eaten(self, background):
        for fish in background:
            if (fish.size > self.size * 1.05 and fish.size > math.sqrt(pow(fish.x - self.x, 2) + pow(fish.y - self.y, 2))):
                return True
        return False
    
    # returns true if candy is consumed
    def candyConsumed(self, candy):
        if (self.size > math.sqrt(pow(candy.x - self.x, 2) + pow(candy.y - self.y, 2))):
            return True
        return False

# Background Fish Class
class BackgroundFish(Fish):
    def __init__(self, screen, backgroundMaxSize):
        super().__init__(screen, randint(0, int(backgroundMaxSize)), 0, randint(0, int(SCREEN_HEIGHT)), convertNum(randint(0, 1)))
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.vx = (random() / 2 + 0.5) * SPEED

    # Effect: draws this fish onto the current screen
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
        
        directionX = self.directionX
        if (directionX == 0):
            directionX = 1
        
        triangle_vertices = [(self.x - self.size * directionX, self.y), 
                             (self.x - self.size * 2 * directionX, self.y + self.size), 
                             (self.x - self.size * 2 * directionX, self.y - self.size)]
        pygame.draw.polygon(self.screen, self.color, triangle_vertices, 0)


    # Effect: moves this Fish in the x-direction using its velocity
    def moveBackground(self):
        self.move(self.directionX, 0, self.vx)
    
    # Effect: stops this fish from moving
    def endMoveBackground(self):
        self.move(0, 0, self.vx)

# Candy class
class Candy():
    def __init__(self, screen):
        self.screen = screen
        self.defaultX, self.defaultY = (-100, -100)
        self.defaultColor = (255, 255, 255)
        self.defaultType = ""
        self.x, self.y = (self.defaultX, self.defaultY)
        self.color = self.defaultColor
        self.type = self.defaultType

    # Effect: sets this candy to random values
    def makeCandy(self):
        self.x = randint(0, SCREEN_WIDTH)
        self.y = randint(0, SCREEN_HEIGHT)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        if (randint(0, CANDY_TYPE_PROBABILITY) == 0):
            self.type = GROW_CANDY
        else:
            self.type = SPEED_CANDY
    
    # Effect: draws this candy onto the current screen
    def draw(self):
        size = CANDY_SIZE

        # Calculate angles for each point
        angles = [2 * math.pi * i / 5 - math.pi / 2 for i in range(5)]
    
        # Generate the points
        starPoints = []
        for angle in angles:
            outer_x = self.x + size * math.cos(angle)
            outer_y = self.y + size * math.sin(angle)
            inner_x = self.x + size * 0.5 * math.cos(angle + math.pi / 5)
            inner_y = self.y + size * 0.5 * math.sin(angle + math.pi / 5)
            starPoints.append((outer_x, outer_y))
            starPoints.append((inner_x, inner_y))

        pygame.draw.polygon(self.screen, self.color, starPoints, 0)
    
    # Effect: resets the values of this candy to default
    def reset(self):
        self.x, self.y = (self.defaultX, self.defaultY)
        self.color = self.defaultColor
        self.type = self.defaultType


# Game class
class FeedingFrenzy():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameMenu = GameMenu(self.screen, FEEDINGFRENZY_TEXT)
        self.fish = Fish(self.screen, PLAYER_SIZE1, CX, CY, 0)
        self.background = list()
        self.directionX = 0
        self.directionY = 0
        self.highScore = load_high_score(FEEDINGFRENZY)
        self.score = 0
        self.grow = False
        self.speed = False
        self.gameEnd = True
        self.pause = False
        self.candy = Candy(self.screen)
        self.timer = 0
        self.backgroundMaxSize = BACKGROUND_MAX_SIZE1
        self.populationCap = POPULATION_CAP1
        pygame.display.set_caption('Feeding Frenzy')
    
    # makes scene and updates display by calling flip()
    # Effect: draws everything onto the screen (overwriting previous items)
    def makeScene(self):
        self.screen.fill(OCEAN_COLOR)

        for i in range(len(self.background)):
            self.background[i].draw()
        self.candy.draw()
        self.fish.draw()

        scoreText = SCORE_FONT.render('High Score: ' + str(self.highScore) + '  Score: ' + str(self.score), True, SCORE_COLOR)
        
        if (self.gameEnd):
            self.gameMenu.drawPlay(scoreText)
        elif (self.pause):
            self.gameMenu.drawPause(scoreText)
        else:
            self.screen.blit(scoreText, (15, 15))

            if (self.speed):
                sizeText = SCORE_FONT.render('Speed: ' + str(int(self.timer / TICK_SPEED + 1)), True, SCORE_COLOR)
                self.screen.blit(sizeText, (15, SCREEN_HEIGHT - int(SCORE_SIZE)))
            elif (self.grow):
                sizeText = SCORE_FONT.render('Grow: ' + str(int(self.timer / TICK_SPEED + 1)), True, SCORE_COLOR)
                self.screen.blit(sizeText, (15, SCREEN_HEIGHT - int(SCORE_SIZE)))

        pygame.display.flip()
    
    # this is called every frame
    # Effect: moves the fish and updates the score
    def onTick(self):
        if (self.gameEnd):
            for i in range(len(self.background)):
                self.background[i].endMoveBackground()
        elif (self.pause):
            pass
        else:
            self.addBackgroundFish()

            if (self.speed):
                self.fish.move(self.directionX, self.directionY, CANDY_SPEED)
            else:
                self.fish.move(self.directionX, self.directionY, SPEED)
            
            for i in range(len(self.background)):
                self.background[i].moveBackground()

            if (self.timer > 0):
                self.timer -= 1
            else:
                self.speed = False
                self.grow = False
            
            if (self.candy.type == "" and self.timer == 0 and randint(0, CANDY_SPAWN_PROBABILITY) == 0):
                self.candy.makeCandy()
            elif (self.fish.candyConsumed(self.candy)):
                if (self.candy.type == SPEED_CANDY):
                    self.speed = True
                elif(self.candy.type == GROW_CANDY):
                    self.grow = True
                self.candy.reset()
                self.timer = FIVE_SECOND_TIMER

            self.score += int(self.fish.eat(self.background))
            self.gameEnd = self.fish.eaten(self.background)

            self.updateParameters()
        
        if (self.highScore < self.score):
            save_high_score(FEEDINGFRENZY, self.highScore)
            self.highScore = self.score
    
    # Effect: changes our direction parameters or resets the game
    def onKeyEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause = True
            if event.key == pygame.K_LEFT:
                self.directionX = -1
            elif event.key == pygame.K_RIGHT:
                self.directionX = 1
            elif event.key == pygame.K_UP:
                self.directionY = -1
            elif event.key == pygame.K_DOWN:
                self.directionY = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.directionX = 0
            elif event.key == pygame.K_RIGHT:
                self.directionX = 0
            elif event.key == pygame.K_UP:
                self.directionY = 0
            elif event.key == pygame.K_DOWN:
                self.directionY = 0

    def onMouseEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.gameEnd and self.gameMenu.playButtonClicked(event.pos)):
                self.reset()
            if (self.pause and self.gameMenu.resumeButtonClicked(event.pos)):
                self.pause = False

    # Effect: adds a new fish to the backgorund periodically
    def addBackgroundFish(self):
        if (len(self.background) <= self.populationCap and randint(0,BACKGROUND_SPAWN_CHANCE) == 0):
            self.background.append(BackgroundFish(self.screen, self.backgroundMaxSize))

    # Effect: changes the plaers size and background max size based on level
    def updateParameters(self):
        if (self.score < LEVEL1):
            self.fish.updateSize(PLAYER_SIZE1, BACKGROUND_MAX_SIZE1 + 1, self.grow)
            self.backgroundMaxSize = BACKGROUND_MAX_SIZE1
            self.populationCap = POPULATION_CAP1
        elif (self.score < LEVEL2):
            self.fish.updateSize(PLAYER_SIZE2, BACKGROUND_MAX_SIZE2 + 1, self.grow)
            self.backgroundMaxSize = BACKGROUND_MAX_SIZE2
            self.populationCap = POPULATION_CAP2
        elif (self.score < LEVEL3):
            self.fish.updateSize(PLAYER_SIZE3, BACKGROUND_MAX_SIZE3 + 1, self.grow)
            self.backgroundMaxSize = BACKGROUND_MAX_SIZE3
            self.populationCap = POPULATION_CAP3
        elif (self.score < LEVEL4):
            self.fish.updateSize(PLAYER_SIZE4, BACKGROUND_MAX_SIZE4 + 1, self.grow)
            self.backgroundMaxSize = BACKGROUND_MAX_SIZE4
            self.populationCap = POPULATION_CAP4
        elif (self.score < LEVEL5):
            self.fish.updateSize(PLAYER_SIZE5, BACKGROUND_MAX_SIZE5 + 1, self.grow)
            self.backgroundMaxSize = BACKGROUND_MAX_SIZE5
            self.populationCap = POPULATION_CAP5
        else:
            self.fish.updateSize(PLAYER_SIZE6, BACKGROUND_MAX_SIZE6 + 1, self.grow)
            self.backgroundMaxSize = BACKGROUND_MAX_SIZE6
            self.populationCap = POPULATION_CAP6

    # Effect: resets the game
    def reset(self):
        self.fish = Fish(self.screen, PLAYER_SIZE1, CX, CY, 0)
        self.background = list()
        self.directionX = 0
        self.directionY = 0
        self.score = 0
        self.grow = False
        self.speed = False
        self.gameEnd = False
        self.candy = Candy(self.screen)
        self.backgroundMaxSize = BACKGROUND_MAX_SIZE1
        self.populationCap = POPULATION_CAP1

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