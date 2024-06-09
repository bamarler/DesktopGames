import pygame
from GamesConstants import *

pygame.init()

# name of this game
FEEDINGFRENZY_TEXT = GAMENAME_TEXT_FONT.render('FEEDING FRENZY', True, GAMENAME_TEXT_COLOR)

# unique constants for this game
PLAYER_COLOR = (0, 255, 0)

SPEED = SCREEN_AREA / 400000
CANDY_SPEED = SPEED * 1.5
PLAYER_COLOR = (255, 113, 181)

OCEAN_COLOR = (50, 100, 255)

SCORE_SIZE = SCREEN_WIDTH / 30
SCORE_FONT = pygame.font.Font(None, int(SCORE_SIZE))
SCORE_COLOR = (255, 255, 255)

SIZE_TO_SCORE = SCREEN_AREA / 250000

LEVEL1 = 100
LEVEL2 = 250
LEVEL3 = 550
LEVEL4 = 1150
LEVEL5 = 2350

PLAYER_SIZE1 = SCREEN_AREA / 40000
PLAYER_SIZE2 = SCREEN_AREA / 30000
PLAYER_SIZE3 = SCREEN_AREA / 25000
PLAYER_SIZE4 = SCREEN_AREA / 20000
PLAYER_SIZE5 = SCREEN_AREA / 15000
PLAYER_SIZE6 = SCREEN_AREA / 10000

BACKGROUND_MAX_SIZE1 = PLAYER_SIZE1 * 3 / 2
BACKGROUND_MAX_SIZE2 = PLAYER_SIZE2 * 3 / 2
BACKGROUND_MAX_SIZE3 = PLAYER_SIZE3 * 3 / 2
BACKGROUND_MAX_SIZE4 = PLAYER_SIZE4 * 3 / 2
BACKGROUND_MAX_SIZE5 = PLAYER_SIZE5 * 3 / 2
BACKGROUND_MAX_SIZE6 = PLAYER_SIZE6 * 3 / 2

POPULATION_CAP1 = SCREEN_AREA / 6000
POPULATION_CAP2 = SCREEN_AREA / 7000
POPULATION_CAP3 = SCREEN_AREA / 9000
POPULATION_CAP4 = SCREEN_AREA / 12000
POPULATION_CAP5 = SCREEN_AREA / 17000
POPULATION_CAP6 = SCREEN_AREA / 22000

CANDY_SIZE = SCREEN_AREA / 20000
SPEED_CANDY = "speed candy"
GROW_CANDY = "size candy"
FIVE_SECOND_TIMER = TICK_SPEED * 5


CANDY_TYPE_PROBABILITY = 5 # chance that candy is grow is 1 / CANDYTYPEPROBABILITY
CANDY_SPAWN_PROBABILITY = 300 # chance that candy spawns per tick is 1 / CANDYSPAWNPROBABILITY
BACKGROUND_SPAWN_CHANCE = 50 # chance that fish spawns per tick is 1 / BACKGROUNDSPAWNCHANCE
