import pygame
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from src.constants.GamesConstants import *

pygame.init()

# name of this game
SNAKEGAME_TEXT = GAMENAME_TEXT_FONT.render(SNAKEGAME, True, GAMENAME_TEXT_COLOR)

# score constants
SCORE_SIZE = SCREEN_WIDTH / 30
SCORE_FONT = pygame.font.Font(None, int(SCORE_SIZE))
SCORE_COLOR = (255, 255, 255)

SIZE_TO_SCORE = SCREEN_AREA / 250000

# unique constants for this game
X_TILES = 15
Y_TILES = 15

SNAKE_TILE_SIZE = SCREEN_AREA / (X_TILES * Y_TILES * 100)
SNAKE_HEAD_SIZE = SNAKE_TILE_SIZE / 2
SNAKE_SIZE = SNAKE_HEAD_SIZE / 1.5

SNAKE_TILE_BASE_X = CX - SNAKE_TILE_SIZE * X_TILES / 2
SNAKE_TILE_BASE_Y = CY - SNAKE_TILE_SIZE * Y_TILES / 2
SNAKE_TILE_BASE_CX = SNAKE_TILE_BASE_X + SNAKE_TILE_SIZE / 2
SNAKE_TILE_BASE_CY = SNAKE_TILE_BASE_Y + SNAKE_TILE_SIZE / 2

SNAKE_BACKGROUND_COLOR = (44, 73, 23)
SNAKE_COLOR = (3, 80, 150)
TILE_COLOR_A = (109, 204, 61)
TILE_COLOR_B = (86, 147, 47)

APPLE_SIZE = SNAKE_HEAD_SIZE
APPLE_COLOR = (220, 20, 60)

SNAKE_SPEED = SCREEN_AREA / 450000
DIR_UP = (0, -1)
DIR_DOWN = (0, 1)
DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)

SNAKE_SEGS_PER_TILE = SNAKE_TILE_SIZE / SNAKE_SPEED

TOLERANCE = 0.1

SNAKE_TILE_POSITIONS = [[0 for _ in range(X_TILES)] for _ in range(Y_TILES)]

for row in range(0, Y_TILES):
    for col in range(0, X_TILES):
        SNAKE_TILE_POSITIONS[row][col] = (SNAKE_TILE_BASE_CX + SNAKE_TILE_SIZE * row, SNAKE_TILE_BASE_CY + SNAKE_TILE_SIZE * col)