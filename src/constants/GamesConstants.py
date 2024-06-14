import pygame
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))
while os.path.basename(file_path) != 'src':
    file_path = os.path.dirname(file_path)
sys.path.insert(0, file_path)

from constants.Constants import *

pygame.init()

# constants for individual game start Screens
RESTART_SCREEN_WIDTH = SCREEN_WIDTH / 1.5
RESTART_SCREEN_HEIGHT = SCREEN_HEIGHT / 2
RESTART_SCREEN_POS = (CX - RESTART_SCREEN_WIDTH / 2, CY - RESTART_SCREEN_HEIGHT / 2, RESTART_SCREEN_WIDTH, RESTART_SCREEN_HEIGHT)

GAMENAME_TEXT_SIZE = SCREEN_AREA / 8000
GAMENAME_TEXT_FONT = pygame.font.SysFont(FONT, int(GAMENAME_TEXT_SIZE))
GAMENAME_TEXT_COLOR = WHITE
GAMENAME_TEXT_CENTER = (CX, SCREEN_HEIGHT * 3 / 8)

GAME_MENU_BUTTON_WIDTH = SCREEN_WIDTH / 5
GAME_MENU_BUTTON_HEIGHT = SCREEN_HEIGHT / 8

GAME_MENU_BUTTON_TEXT_SIZE = GAME_MENU_BUTTON_WIDTH / 6
GAME_MENU_BUTTON_FONT = pygame.font.SysFont(FONT, int(GAME_MENU_BUTTON_TEXT_SIZE))

PB_NAME = "Play Game"
R_NAME = "Resume"
PB_CX = SCREEN_WIDTH / 2 - GAME_MENU_BUTTON_WIDTH / 1.5
PB_CY = SCREEN_HEIGHT * 5 / 8

MM_NAME = "Main Menu"
MM_CX = SCREEN_WIDTH / 2 + GAME_MENU_BUTTON_WIDTH / 1.5
MM_CY = SCREEN_HEIGHT * 5 / 8